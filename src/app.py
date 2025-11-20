from flask import Flask, request
from src.recommender import Recommender
from src.models import Perfil

app = Flask(__name__)
recommender = Recommender()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Career Assistant</title>
    <style>
        body {
            background: #111;
            color: #fff;
            font-family: Arial, sans-serif;
            padding: 40px;
        }
        h1 {
            text-align: center;
            color: #00e0ff;
        }
        .box {
            background: #1b1b1b;
            padding: 20px;
            margin: auto;
            width: 500px;
            border-radius: 10px;
            box-shadow: 0 0 10px #000;
        }
        label {
            font-size: 14px;
            margin-top: 10px;
            display: block;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            border-radius: 6px;
            margin-top: 5px;
            border: none;
            background: #222;
            color: #fff;
        }
        button {
            margin-top: 20px;
            padding: 12px;
            width: 100%;
            background: #00e0ff;
            border: none;
            color: #000;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
        }
        .result-box {
            margin-top: 30px;
            background: #202020;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>

<h1>Career Assistant</h1>

<div class="box">
    <form method="POST" action="/">
    <label>Nome:</label>
    <input type="text" name="name" placeholder="Ex.: Ana Souza" required>

    <label>Experiência (meses):</label>
    <input type="number" name="experience" placeholder="Ex.: 12" required>

    <label>Educação:</label>
    <input type="text" name="education" placeholder="Ex.: Ensino Superior em Andamento">

    <label>Habilidades (use formato: python=4, lógica=5, html=2):</label>
    <input type="text" name="skills" placeholder="Ex.: python=4, estatistica=3, html=2">

    <label>Interesses (separe por vírgula):</label>
    <input type="text" name="interests" placeholder="Ex.: Dados, Tecnologia, UX Design">

    <button type="submit">Gerar Recomendação</button>
</form>

</div>

{result_section}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result_section = ""

    if request.method == "POST":

        # Construindo Perfil
        nome = request.form.get("name")
        experiencia = int(request.form.get("experience") or 0)
        educacao = request.form.get("education") or ""

        # separa skills "python=3,logica=5"
        skills_input = request.form.get("skills")
        skill_levels = {}

        if skills_input:
            for item in skills_input.split(","):
                if "=" in item:
                    chave, valor = item.split("=")
                    skill_levels[chave.strip().lower()] = int(valor)

        # interesses
        interests_input = request.form.get("interests", "")
        interests = [i.strip().title() for i in interests_input.split(",") if i.strip()]

        perfil = Perfil(
            name=nome,
            skill_levels=skill_levels,
            interests=interests,
            experience_months=experiencia,
            education=educacao
        )
        # Recomendações
     
        recs = recommender.recommend(perfil.to_dict(), top_n=5)
        trilhas = recommender.generate_learning_path(perfil.to_dict())
        melhorias = recommender.areas_to_improve(perfil.to_dict())

        # Montar HTML do resultado
       
        html_list = "<ul>"
        for area, score in recs:
            html_list += f"<li><b>{area}</b> — Pontuação: {score}</li>"
        html_list += "</ul>"

        trilhas_list = "<ul>" + "".join([f"<li>{t}</li>" for t in trilhas]) + "</ul>"
        melhorias_list = "<ul>" + "".join([f"<li>{m}</li>" for m in melhorias]) + "</ul>"

        result_section = f"""
        <div class="result-box">
            <h2>Recomendações para {nome}</h2>
            <h3>Carreiras sugeridas:</h3>
            {html_list}

            <h3>Trilhas de aprendizado:</h3>
            {trilhas_list}

            <h3>Áreas a melhorar:</h3>
            {melhorias_list}
        </div>
        """

    return HTML_TEMPLATE.replace("{result_section}", result_section)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", action="store_true")
    args = parser.parse_args()

    if args.cli:
        print("CLI não implementado neste arquivo — use `src/cli.py`.")
    else:
        app.run(debug=True)
