from create_db import create_tables
from database_scripts import insert_data, insert_job_postings
from fetch import JobSearchRetriever, JobDetailRetriever
import sqlite3
from helpers import clean_job_postings
import time

SLEEP_TIME = 60

conn = sqlite3.connect('linkedin_jobs.db')
cursor = conn.cursor()

create_tables(conn, cursor)


job_detail_retriever = JobDetailRetriever()

while True:
    query = "SELECT job_id FROM jobs WHERE scraped = 0"
    cursor.execute(query)
    result = cursor.fetchall()
    result = [r[0] for r in result]

    details = job_detail_retriever.get_job_details(result[:25])
    details = clean_job_postings(details)
    insert_data(details, conn, cursor)
    print('Updated {} results in DB. Sleeping'.format(len(details)))
    time.sleep(SLEEP_TIME)

