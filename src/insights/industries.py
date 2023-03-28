from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industry_data = read(path)
    industries = set()

    for industry in industry_data:
        if industry["industry"]:
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    data = []
    for job in jobs:
        if job["industry"] == industry:
            data.append(job)
    return data
