import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf8") as file:
        data_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in data_reader]


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    jobs = {}
    for row in data:
        current_job = row["job_type"]
        if current_job not in jobs:
            jobs[current_job] = 1
        else:
            jobs[current_job] += 1
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    data = []
    for job in jobs:
        if job["job_type"] == job_type:
            data.append(job)
    return data
