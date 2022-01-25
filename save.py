import csv
from indeed import extract_jobs


def save_csv_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "url", "explanation"])
    for job in jobs:
        writer.writerow(list(job.values()))


save_csv_file(extract_jobs("reactjs", "서울"))
