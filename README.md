# CareerAssistant 

Este projeto tem como objetivo criar um Assistente de Carreira capaz de analisar o perfil de um usuário — incluindo suas habilidades, interesses, experiência e formação — e gerar recomendações personalizadas de carreiras, trilhas de aprendizado e áreas de melhoria.

O sistema processa os dados informados pelo usuário e retorna sugestões alinhadas ao seu perfil, simulando o funcionamento de uma ferramenta real de orientação profissional

## Estrutura
- `data/skills_map.csv` — mapeamento skill→area
- `data/sample_profile.json` — perfil de exemplo
- `src/recommender.py` — lógica de pontuação
- `src/app.py` — Flask (web + CLI)
- `src/utils.py` — carregamento de dados

## Como rodar (local)
1. criar venv:
-python -m venv venv
-source venv/bin/activate # Windows: venv\Scripts\activate
-pip install -r requirements.txt

2. rodar web:
python -m src.app
-abrir http://127.0.0.1:5000

3. rodar CLI com exemplo:
-python src/app.py --cli

## Estrutura de Arquivos

GS - PYTHON/
│
├── src/
│   ├── app.py               # Interface web 
│   ├── recommender.py       # Motor de recomendação
│   ├── models.py            # Classes e estrutura do perfil
│   └── __init__.py
│
├── data/
│   ├── skills_map.csv      
│   └── sample_profile.json  # Perfil de exemplo para testes
│
├── requirements.txt         # Bibliotecas
└── README.md                # Documentação do projeto

## Demonstração

**Tela Inicial**

<img width="794" height="535" alt="tela_inicial" src="https://github.com/user-attachments/assets/d095e788-d32f-4b1b-965f-c9f106885ec4" />


**Dados Preenchidos**

<img width="687" height="529" alt="dados" src="https://github.com/user-attachments/assets/8608be46-8782-4c88-84b4-0da456bc84ed" />


**Resultado**

<img width="1376" height="863" alt="image" src="https://github.com/user-attachments/assets/54e9b757-ff4c-47ec-b5f0-5fb7d8c4e0d8" />



## Observações
Documento referência: `/mnt/data/GS2025.2 - PCP(3).pdf`
