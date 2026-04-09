import pandas as pd
from jobspy import scrape_jobs
from config import JOB_SITES, HOURS_OLD, RESULTS_PER_QUERY


def fetch_jobs(profile: dict) -> pd.DataFrame:
    """
    Scrape all job boards for a given profile's search terms and locations.
    Returns a deduplicated DataFrame.
    """
    all_jobs = []
    name = profile["name"]

    for term in profile["search_terms"]:
        for location in profile["locations"]:
            try:
                print(f"  [{name}] Scraping: '{term}' in '{location}'...")
                jobs = scrape_jobs(
                    site_name=JOB_SITES,
                    search_term=term,
                    location=location,
                    results_wanted=RESULTS_PER_QUERY,
                    hours_old=HOURS_OLD,
                    country_indeed="USA",
                    linkedin_fetch_description=False,
                )
                if not jobs.empty:
                    all_jobs.append(jobs)
                    print(f"    → {len(jobs)} results")
            except Exception as e:
                print(f"    → ERROR: {e}")

    if not all_jobs:
        return pd.DataFrame()

    combined = pd.concat(all_jobs, ignore_index=True)
    combined = combined.drop_duplicates(subset=["job_url"])
    combined = combined.reset_index(drop=True)

    print(f"  [{name}] Total unique jobs fetched: {len(combined)}")
    return combined
