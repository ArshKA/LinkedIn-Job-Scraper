import pandas as pd

variable_paths = pd.read_csv('json_paths/data_variables.csv')
included_paths = pd.read_csv('json_paths/included_variables.csv')

size_ranges = {(None, 10): 0, (11, 50): 1, (51, 200): 2, (201, 500): 3, (501, 1000): 4, (1001, 5000): 5, (5001, 10000): 6, (10001, None): 7}

def strip_val(val, cat):
    if cat == 0 or val == None:
        return val
    elif cat == 1:
        return val.split(':')[-1]
    elif cat == 2:
        return val.split('.')[-1]
    else:
        raise ValueError

def get_value_by_path(dictionary, path):
    keys = path.strip("[]'").split("']['")
    for key in keys:
        if not dictionary or key not in dictionary:
            return False
        dictionary = dictionary[key]
    return dictionary

def clean_job_postings(all_jobs):
    all_cleaned_postings = dict()
    for job_id, job_info in all_jobs.items():
        if job_info == -1:
            posting = {'error': job_info}
        else:
            posting = {'jobs': {}, 'companies': {}, 'salaries': {}, 'benefits': {}, 'industries': {}, 'skills': {}, 'employee_counts': {}, 'company_industries': {}, 'company_specialities': {}}
            for idx, row in variable_paths.iterrows():
                value = get_value_by_path(job_info, row['path'])
                if value:
                    posting[row['table']][row['name']] = strip_val(value, row['strip'])

            for idx, row in included_paths.iterrows():
                for into_type in job_info['included']:
                    if strip_val(into_type.get('$type'), 2) == row['type']:
                        if row['name'] == 'company_size':
                            company_size_info = get_value_by_path(into_type, row['path'])
                            if company_size_info:
                                posting[row['table']][row['name']] = size_ranges.get((company_size_info.get('start'), company_size_info.get('end')))
                        else:
                            value = get_value_by_path(into_type, row['path'])
                            posting[row['table']][row['name']] = strip_val(value, row['strip'])


        # posting['companies']['size_range'] = size_ranges.get(job_info['included'][-1])
        all_cleaned_postings[job_id] = posting

    return all_cleaned_postings

