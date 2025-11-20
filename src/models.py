from typing import Dict, List

class Competencia:
    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = max(0, min(5, int(level)))

    def to_dict(self):
        return {"name": self.name, "level": self.level}

    def __repr__(self):
        return f"Competencia({self.name}:{self.level})"

class Perfil:
    def __init__(self, name: str, skill_levels: Dict[str,int]=None,
                 interests: List[str]=None, experience_months: int = 0,
                 education: str = ""):
        self.name = name
        self.skill_levels = dict(skill_levels or {})
        self.interests = [i.title() for i in (interests or [])]
        self.experience_months = int(experience_months)
        self.education = education

    def add_skill(self, skill: str, level: int):
        self.skill_levels[skill] = max(0, min(5, int(level)))

    def to_dict(self):
        return {
            "name": self.name,
            "skill_levels": self.skill_levels,
            "interests": self.interests,
            "experience_months": self.experience_months,
            "education": self.education
        }

    @staticmethod
    def from_dict(d):
        return Perfil(
            name=d.get("name",""),
            skill_levels=d.get("skill_levels",{}),
            interests=d.get("interests",[]),
            experience_months=d.get("experience_months",0),
            education=d.get("education","")
        )

    def __repr__(self):
        return f"Perfil({self.name})"

class Carreira:
    def __init__(self, name: str, description: str = "", suggested_courses: List[str]=None):
        self.name = name
        self.description = description
        self.suggested_courses = suggested_courses or []

    def to_dict(self):
        return {"name": self.name, "description": self.description, "suggested_courses": self.suggested_courses}

    def __repr__(self):
        return f"Carreira({self.name})"
