from scripts.create_db import create_tables
from scripts.database_scripts import insert_data
from scripts.fetch import JobDetailRetriever
import sqlite3
from scripts.helpers import clean_job_postings
import time
import random

SLEEP_TIME = 60
MAX_UPDATES = 25

conn = sqlite3.connect('linkedin_jobs.db')
cursor = conn.cursor()

create_tables(conn, cursor)


job_detail_retriever = JobDetailRetriever()

while True:
    query = "SELECT job_id FROM jobs WHERE scraped = 0"
    cursor.execute(query)
    result = cursor.fetchall()
    result = [r[0] for r in result]

    details = job_detail_retriever.get_job_details(random.sample(result, min(MAX_UPDATES, len(result))))
    details = clean_job_postings(details)
    insert_data(details, conn, cursor)
    print('UPDATED {} VALUES IN DB'.format(len(details)))

    print('Sleeping For {} Seconds...'.format(SLEEP_TIME))
    time.sleep(SLEEP_TIME)
    print('Resuming...')
