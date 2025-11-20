import json
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

def load_skills_map(csv_filename="skills_map.csv"):
    path = DATA_DIR / csv_filename
    df = pd.read_csv(path)
    skills_map = {}
    for _, row in df.iterrows():
        skill = row['skill'].strip()
        area = row['area'].strip()
        weight = float(row['weight'])
        course = row.get('course', "")
        skills_map.setdefault(skill, []).append((area, weight, course))
    return skills_map

def load_profile(json_path):
    path = DATA_DIR / json_path
    with open(path, encoding='utf-8') as f:
        return json.load(f)
