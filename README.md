# LinkedIn Job Scraper

<img src="media/logo.jpg" width="530" height="267">

**Program to scrape and store a constant stream of LinkedIn job postings and dozens of their respective attributes**

**Download the polished dataset and view insights at - https://www.kaggle.com/datasets/arshkon/linkedin-job-postings**

## User Configurations

### Required
- **```logins.csv```**
  - Populate with multiple LinkedIn logins
  - Specify the purpose of the login (search or detail retreiever)
  - I recommend 1-3 logins for search and the remaining for more expensive attribute retrieval
- **```search_retriever.py```**
## Optional
- **```details_retriever.py```**
  - **MAX_UPDATES**: - Number of job postings to look up before sleeping. Increase with more accounts/proxies (default = 25)
  - **SLEEP_TIME**: - Seconds to sleep between every iteration (default = 60)

## Running

This program consists of 2 main scripts, running in parallel.

```search_retriever.py``` - discovers new job postings and insert the most recent IDs and minimal attributes into the database

```details_retriever.py``` - populates tables with complete job attributes


It's important to note that while ```search_retriever.py``` typically runs smoothly, even through your personal IP and a singular account, ```details_retriever.py``` can be a bit finicky. Each search generates approximately 25-50 results, all of which must be individually queried to obtain their attributes. To enhance its performance, I recommend the following strategies:

- Utilize multiple proxies and accounts when running details_retriever.py.
- Experiment with different time delays to find the optimal settings.
- Run details_retriever.py during periods of lower online activity, such as late-night hours and weekends, to catch up with the progress of search_retriever.py. This will ensure that both processes remain synchronized and up to date.

## Database Structure

### JOBS

| Column | Description |
| --- | --- |
| job_id | The job ID as defined by LinkedIn (https://www.linkedin.com/jobs/view/{job_id}) |
| company_id | Identifier for the company associated with the job posting (maps to companies.csv) |
| title | Job title |
| description | Job description |
| max_salary | Maximum salary |
| med_salary | Median salary |
| min_salary | Minimum salary |
| pay_period | Pay period for salary (Hourly, Monthly, Yearly) |
| formatted_work_type | Type of work (Fulltime, Parttime, Contract) |
| location | Job location |
| applies | Number of applications that have been submitted |
| original_listed_time | Original time the job was listed |
| remote_allowed | Whether job permits remote work |
| views | Number of times the job posting has been viewed |
| job_posting_url | URL to the job posting on a platform |
| application_url | URL where applications can be submitted |
| application_type | Type of application process (offsite, complex/simple onsite) |
| expiry | Expiration date or time for the job listing |
| closed_time | Time to close job listing |
| formatted_experience_level | Job experience level (entry, associate, executive, etc) |
| skills_desc | Description detailing required skills for job |
| listed_time | Time when the job was listed |
| posting_domain | Domain of the website with application |
| sponsored | Whether the job listing is sponsored or promoted |
| work_type | Type of work associated with the job |
| currency | Currency in which the salary is provided |
| compensation_type | Type of compensation for the job |
| scraped | Has been scraped by ```details_retriever``` |
| inferred_benefits | EMPTY |
| years_experience | EMPTY |
| job_region | EMPTY |
| degree | EMPTY |

### SALARIES
| Column | Description |
| --- | --- |
| salary_id | The salary ID |
| job_id | The job ID (references jobs table) |
| max_salary | Maximum salary |
| med_salary | Median salary |
| min_salary | Minimum salary |
| pay_period | Pay period for salary (Hourly, Monthly, Yearly) |
| currency | Currency in which the salary is provided |
| compensation_type | Type of compensation for the job (Fixed, Variable, etc) |

### BENEFITS
| Column | Description |
| --- | --- |
| job_id | The job ID |
| type | Type of benefit provided (401K, Medical Insurance, etc) |
| inferred | Whether the benefit was explicitly tagged or inferred through text by LinkedIn |

### COMPANIES
| Column | Description |
| --- | --- |
| company_id | The company ID as defined by LinkedIn |
| name | Company name |
| description | Company description |
| company_size | Company grouping based on number of employees (0 Smallest - 7 Largest) |
| country | Country of company headquarters |
| state | State of company headquarters |
| city | City of company headquarters |
| zip_code | ZIP code of company's headquarters |
| address | Address of company's headquarters |
| url | Link to company's LinkedIn page |

### EMPLOYEE_COUNTS
| Column | Description |
| --- | --- |
| company_id | The company ID |
| employee_count | Number of employees at company |
| follower_count | Number of company followers on LinkedIn |
| time_recorded | Unix time of data collection |

### SKILLS
| Column | Description |
| --- | --- |
| skill_abr | The skill abbreviation (primary key) |
| skill_name | The skill name |

### JOB_SKILLS
| Column | Description |
| --- | --- |
| job_id | The job ID (references jobs table and primary key) |
| skill_abr | The skill abbreviation (references skills table) |

### INDUSTRIES
| Column | Description |
| --- | --- |
| industry_id | The industry ID (primary key) |
| industry_name | The industry name |

### JOB_INDUSTRIES
| Column | Description |
| --- | --- |
| job_id | The job ID (references jobs table and primary key) |
| industry_id | The industry ID (references industries table) |

### COMPANY_SPECIALITIES
| Column | Description |
| --- | --- |
| company_id | The company ID (references companies table and primary key) |
| speciality | The speciality ID |

### COMPANY_INDUSTRIES
| Column | Description |
| --- | --- |
| company_id | The company ID (references companies table and primary key) |
| industry | The industry ID |


