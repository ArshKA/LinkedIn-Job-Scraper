import sqlite3
import csv
import os
import pandas as pd
import argparse



parser = argparse.ArgumentParser()

parser.add_argument('-d', '--database', default='linkedin_jobs.db')
parser.add_argument('-f', '--folder', default='csv_files')
args = parser.parse_args()


folder_name = args.folder

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Connect to the SQLite database
conn = sqlite3.connect(args.database)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
table_names = [x[0] for x in cursor.fetchall()]

print(table_names)

for table_name in table_names:
  # Replace 'your_table' with the actual table name

  # Execute a query to fetch all rows from the table
  query = f'SELECT * FROM {table_name}'
  cursor.execute(query)
  rows = cursor.fetchall()

  # Replace 'output.csv' with the desired output CSV file name
  csv_filename = f'{folder_name}/{table_name}.csv'

  # Write the data to the CSV file
  with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
      csv_writer = csv.writer(csv_file)

      # Write header row with column names
      column_names = [description[0] for description in cursor.description]
      csv_writer.writerow(column_names)

      # Write data rows
      csv_writer.writerows(rows)

# Close the connection
conn.close()

jobs = pd.read_csv(f'{folder_name}/jobs.csv')
jobs = jobs[jobs['scraped'] > 0]

salaries = pd.read_csv(f'{folder_name}/salaries.csv')
salaries.drop(columns='salary_id', inplace=True)

merged_df = pd.merge(jobs, salaries, on='job_id', how='left')

# merged_df = merged_df.drop(columns='scraped')

col = ['job_id', 'company_id', 'title', 'description', 'max_salary', 'med_salary', 'min_salary', 'pay_period',
       'formatted_work_type', 'location',
       'applies', 'original_listed_time', 'remote_allowed', 'views','job_posting_url',
       'application_url', 'application_type', 'expiry',
       'closed_time', 'formatted_experience_level',
       'skills_desc',
       'listed_time', 'posting_domain', 'sponsored', 'work_type',
       'currency',
       'compensation_type', 'scraped']

merged_df = merged_df[col]

merged_df.to_csv(f'{folder_name}/job_postings.csv', index=False)

os.remove(f"{folder_name}/jobs.csv")
