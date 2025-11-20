class Recommender:

    def __init__(self):
        self.areas = {
            "Ciência de Dados": {
                "skills": ["python", "estatistica", "data", "analise"],
                "interests": ["Tecnologia", "Dados", "Pesquisa"]
            },
            "Inteligência Artificial": {
                "skills": ["python", "ia", "machine learning", "matematica"],
                "interests": ["Robótica", "Automação", "Tecnologia"]
            },
            "Desenvolvimento Web": {
                "skills": ["html", "css", "javascript", "logica"],
                "interests": ["Criatividade", "Tecnologia", "Web"]
            },
            "Design Digital": {
                "skills": ["ux", "ui", "criatividade", "figma"],
                "interests": ["Arte", "Design", "Experiências"]
            },
            "Gestão de Projetos": {
                "skills": ["comunicacao", "lideranca", "organizacao"],
                "interests": ["Gestão", "Negócios"]
            }
        }

    # Score geral baseado em habilidades + interesses
    def score_profile(self, profile_dict):
        skills = {k.lower(): v for k, v in profile_dict.get("skill_levels", {}).items()}
        interests = [i.title() for i in profile_dict.get("interests", [])]

        area_scores = {}

        for area, data in self.areas.items():
            score = 0

            # match de habilidades
            for skill_req in data["skills"]:
                if skill_req in skills:
                    score += skills[skill_req]

            # match de interesses
            for intr in data["interests"]:
                if intr in interests:
                    score += 3 

            area_scores[area] = score

        return area_scores

    # Recomendações principais
    def recommend(self, profile_dict, top_n=3):
        scores = self.score_profile(profile_dict)
        sorted_areas = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_areas[:top_n]

    # Trilhas de aprendizado
    def generate_learning_path(self, profile_dict):
        top_area = self.recommend(profile_dict, top_n=1)[0][0]

        trilhas = {
            "Ciência de Dados": [
                "Fundamentos de Python",
                "Estatística básica",
                "Análise de Dados",
                "Machine Learning"
            ],
            "Inteligência Artificial": [
                "Python avançado",
                "Redes neurais",
                "Deep Learning"
            ],
            "Desenvolvimento Web": [
                "HTML5 e CSS3",
                "JavaScript",
                "React básico"
            ],
            "Design Digital": [
                "Princípios de UX",
                "UI no Figma",
                "Design Systems"
            ],
            "Gestão de Projetos": [
                "Fundamentos de Scrum",
                "Kanban",
                "Certificação CAPM / PMP"
            ]
        }

        return trilhas[top_area]

    # Áreas para melhorar
    def areas_to_improve(self, profile_dict):
        skills = profile_dict.get("skill_levels", {})
        low = [skill for skill, lvl in skills.items() if lvl <= 2]
        return low if low else ["Nenhuma — bom equilíbrio de habilidades!"]
