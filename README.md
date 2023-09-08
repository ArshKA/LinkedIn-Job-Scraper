# LinkedIn-Job-Scraper

## An un-documented and un-polished repository to help others scrape LinkedIn job postings

```search_retriever.py``` - discovers new job postings and insert the most recent IDs into the database

```details_retriever.py``` - populates table with individual job attributes


It's important to note that while ```search_retriever.py``` typically runs smoothly, even through your personal IP and a singular account, ```details_retriever.py``` can be a bit finicky. Each search generates approximately 25-50 results, all of which must be individually queried to obtain their attributes. To enhance its performance, I recommend the following strategies:

- Utilize multiple proxies and accounts when running details_retriever.py.
- Experiment with different time delays to find the optimal settings.
- Run details_retriever.py during periods of lower online activity, such as late-night hours and weekends, to catch up with the progress of search_retriever.py. This will ensure that both processes remain synchronized and up to date.
