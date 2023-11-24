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
## Optional
- **```details_retriever.py```**
  - **MAX_UPDATES**: - Number of job postings to look up before sleeping. Increase with more accounts/proxies (default = 25)
  - **SLEEP_TIME**: - Seconds to sleep between every iteration (default = 60)

## Running

This program consists of 2 main scripts, running in parallel.

```python search_retriever.py``` - discovers new job postings and insert the most recent IDs and minimal attributes into the database

```python details_retriever.py``` - populates tables with complete job attributes


It's important to note that while ```search_retriever.py``` typically runs smoothly, even through your personal IP and a singular account, ```details_retriever.py``` can be a bit finicky. Each search generates approximately 25-50 results, all of which must be individually queried to obtain their attributes. To enhance its performance, I recommend the following strategies:

- Utilize multiple proxies and accounts when running details_retriever.py.
- Experiment with different time delays to find the optimal settings.
- Run details_retriever.py during periods of lower online activity, such as late-night hours and weekends, to catch up with the progress of search_retriever.py. This will ensure that both processes remain synchronized and up to date.

## Converting Database to CSV

```python to_csv.py --folder <destination folder> --database <linkedin_jobs.db>```

Creates a CSV file for each database, along with minimal preprocessing


## Database Structure

[You can find the structure of the database here](DatabaseStructure.md)
