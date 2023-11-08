import time


def insert_data(data, conn, cursor):
    for job_id, job_info in data.items():
        if 'error' in job_info:
            cursor.execute(f"UPDATE jobs SET scraped = -1 WHERE job_id = ?", (job_id,))
            continue
        company_id = job_info['jobs'].get('company_id')
        for table_name in job_info:
            if len(job_info[table_name]) > 0:
                if table_name == 'jobs':
                    column_names = list(job_info[table_name].keys())
                    values = tuple(job_info[table_name][column] for column in column_names)
                    set_clause = ", ".join([f"{column} = ?" for column in column_names])
                    set_clause += ", scraped = ?"
                    values_for_update = values + (round(time.time()), job_id)  # Adding the job_id as the last value
                    query = f"UPDATE {table_name} SET {set_clause} WHERE job_id = ?"
                    cursor.execute(query, values_for_update)

                elif table_name == 'benefits':
                    if 'listed_benefits' in job_info[table_name]:
                        for benefit in job_info[table_name]['listed_benefits']:
                            cursor.execute(
                                f'INSERT OR REPLACE INTO {table_name} (job_id, inferred, type) VALUES (?, ?, ?)',
                                (job_id, 0, benefit))
                    if 'inferred_benefits' in job_info[table_name]:
                        for benefit in job_info[table_name]['inferred_benefits']:
                            cursor.execute(
                                f'INSERT OR IGNORE INTO {table_name} (job_id, inferred, type) VALUES (?, ?, ?)',
                                (job_id, 1, benefit))

                elif table_name == 'industries' and 'industry_ids' in job_info[table_name]:
                    for industry_index in range(len(job_info[table_name]['industry_ids'])):
                        industry_id = job_info[table_name]['industry_ids'][industry_index]
                        industry_name = job_info[table_name]['industry_names'][industry_index] if 'industry_names' in job_info[table_name] and len(job_info[table_name]['industry_names']) == len(job_info[table_name]['industry_ids']) else None

                        cursor.execute(
                            'INSERT OR REPLACE INTO industries (industry_id, industry_name) VALUES (?, COALESCE((SELECT industry_name FROM industries WHERE industry_id=?), ?))',
                            (industry_id, industry_id, industry_name))
                        # cursor.execute('INSERT OR IGNORE INTO job_industries (job_id, industry_id, industry_name) VALUES (?, ?, ?)',
                        #                (job_id, industry_id, industry_name))
                        cursor.execute('INSERT OR IGNORE INTO job_industries (job_id, industry_id) VALUES (?, ?)',
                                       (job_id, industry_id))


                elif table_name == 'skills' and 'skill_abrs' in job_info[table_name]:
                    for industry_index in range(len(job_info[table_name]['skill_abrs'])):
                        skill_abr = job_info[table_name]['skill_abrs'][industry_index]
                        skill_name = job_info[table_name]['skill_name'][industry_index] if 'skill_name' in job_info[table_name] and len(job_info[table_name]['skill_name']) == len(job_info[table_name]['skill_abrs']) else None
                        cursor.execute(
                            'INSERT OR REPLACE INTO skills (skill_abr, skill_name) VALUES (?, COALESCE((SELECT skill_name FROM skills WHERE skill_abr=?), ?))',
                            (skill_abr, skill_abr, skill_name))
                        # cursor.execute('INSERT OR IGNORE INTO job_skills (job_id, skill_abr, skill_name) VALUES (?, ?, ?)', (job_id, skill_abr, skill_name))
                        cursor.execute('INSERT OR IGNORE INTO job_skills (job_id, skill_abr) VALUES (?, ?)', (job_id, skill_abr))

                elif table_name == 'salaries':
                    for compensation_type, values in job_info[table_name].items():
                        for compensation in values:
                            cursor.execute(
                                'INSERT INTO salaries (job_id, max_salary, med_salary, min_salary, pay_period, currency, compensation_type) VALUES (?, ?, ?, ?, ?, ?, ?)',
                                (
                                    job_id, compensation.get('maxSalary'), compensation.get('medianSalary'), compensation.get('minSalary'),
                                    compensation['payPeriod'],
                                    compensation['currencyCode'], compensation['compensationType']))

                elif table_name == 'companies' and company_id is not None:
                    column_names = list(job_info[table_name].keys())
                    values = tuple(job_info[table_name][column] for column in column_names)
                    query = f"INSERT OR REPLACE INTO {table_name} (company_id, {', '.join(column_names)}) VALUES ({company_id}, {', '.join(['?'] * len(column_names))})"
                    cursor.execute(query, values)

                elif table_name == 'employee_counts' and company_id is not None:
                    cursor.execute(f"INSERT OR IGNORE INTO {table_name} (company_id, employee_count, follower_count, time_recorded) VALUES (?, ?, ?, ?)", (company_id, job_info[table_name]['employee_count'], job_info[table_name]['follower_count'], round(time.time())))

                elif table_name == 'company_industries' and company_id is not None:
                    for industry in job_info[table_name]['industries']:
                        cursor.execute(f'INSERT OR IGNORE INTO {table_name} (company_id, industry) VALUES (?, ?)', (company_id, industry))

                elif table_name == 'company_specialities' and company_id is not None:
                    for speciality in job_info[table_name]['specialities']:
                        cursor.execute(f'INSERT OR IGNORE INTO {table_name} (company_id, speciality) VALUES (?, ?)', (company_id, speciality))

    conn.commit()
    return True


def insert_job_postings(job_ids, conn, cursor):
    for job_id, info in job_ids.items():
        cursor.execute('INSERT OR IGNORE INTO jobs (job_id, title, sponsored) VALUES (?, ?, ?)', (job_id, info['title'], info['sponsored']))
    conn.commit()
    return True


