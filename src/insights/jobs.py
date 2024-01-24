from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        self.jobs_list = []
        with open(path, "r") as f:
            open_file = csv.DictReader(f)
            self.jobs_list = list(open_file)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        return list(set(job["job_type"] for job in self.jobs_list))

    def filter_by_multiple_criteria(
        self, jobs_list, filter_criteria
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("The filter provided to the method is not a dict!")
        filtered_jobs = [
            job
            for job in jobs_list
            if all(job[key] == filter_criteria[key] for key in filter_criteria)
        ]

        return filtered_jobs
