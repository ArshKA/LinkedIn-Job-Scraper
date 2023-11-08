from scripts.create_db import create_tables
from scripts.database_scripts import insert_job_postings
from scripts.fetch import JobSearchRetriever
import sqlite3
import time
from collections import deque
import pandas as pd


sleep_times = deque(maxlen=5)
first = True
sleep_factor = 3

conn = sqlite3.connect('linkedin_jobs.db')
cursor = conn.cursor()

create_tables(conn, cursor)


job_searcher = JobSearchRetriever()

while True:
    all_results = job_searcher.get_jobs()

    query = "SELECT job_id FROM jobs WHERE job_id IN ({})".format(','.join(['?'] * len(all_results)))
    cursor.execute(query, list(all_results.keys()))
    result = cursor.fetchall()
    result = [r[0] for r in result]
    new_results = {job_id: job_info for job_id, job_info in all_results.items() if job_id not in result}
    insert_job_postings(new_results, conn, cursor)
    total_non_sponsored = len([x for x in all_results.values() if x['sponsored'] is False])
    new_non_sponsored = len([x for x in new_results.values() if x['sponsored'] is False])
    print('{}/{} NEW RESULTS | {}/{} NEW NON-PROMOTED RESULTS'.format(
        len(new_results), len(all_results), new_non_sponsored, total_non_sponsored))
    if not first:
        seconds_per_job = sleep_factor/max(len(new_results), 1)
        sleep_factor = min(seconds_per_job * total_non_sponsored * .75, 200)
    first = False

    print('Sleeping For {} Seconds...'.format(min(200, sleep_factor)))
    time.sleep(min(200, sleep_factor))
    print('Resuming...')
