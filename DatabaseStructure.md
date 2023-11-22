# Database Structure

### JOBS

| Column | Description |
| --- | --- |
| job_id | The job ID as defined by LinkedIn (https://www.linkedin.com/jobs/view/{ job_id }) |
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
