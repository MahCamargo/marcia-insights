from typing import Union, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salary_list = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isnumeric()
        ]

        return max(salary_list) if salary_list else 0

    def get_min_salary(self) -> int:
        salary_list = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"].isnumeric()
        ]

        return min(salary_list) if salary_list else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(
                "Dicionário de job deve conter min_salary e max_salary"
            )

        if not (
            str(job["min_salary"]).isdigit()
            and str(job["max_salary"]).isdigit()
        ):
            raise ValueError(
                "Os valores de min_salary e max_salary devem ser numéricos."
            )

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError("min_salary deve ser menor que max_salary")

        if not (
            isinstance(salary, int)
            or (isinstance(salary, str) and str(salary).isdigit())
        ):
            raise ValueError("salary deve ser um valor numérico")

        return min_salary <= int(salary) <= max_salary
