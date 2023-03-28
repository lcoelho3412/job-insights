from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    highest_salary = []

    for job in data:
        if job["max_salary"] and job["max_salary"] != "invalid":
            highest_salary.append(int(job["max_salary"]))
    return max(highest_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    lowest_salary = []

    for job in data:
        if job["min_salary"] and job["min_salary"] != "invalid":
            lowest_salary.append(int(job["min_salary"]))
    return min(lowest_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    try:
        minimum_salary = int(job["min_salary"])
        maximum_salary = int(job["max_salary"])
        int(salary)
    except Exception:
        raise ValueError

    if minimum_salary > maximum_salary:
        raise ValueError
    return minimum_salary <= int(salary) <= maximum_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_by_salary.append(job)
        except ValueError:
            continue
    return filtered_by_salary
