import pandas as pd
from jobspy import scrape_jobs
from config import SEARCH_TERMS, LOCATIONS, JOB_SITES, HOURS_OLD, RESULTS_PER_QUERY


def fetch_jobs() -> pd.DataFrame:
    """
    Hit all configured job boards for every search term + location combo.
    Returns a deduplicated DataFrame of all results.
    """
    all_jobs = []

    for term in SEARCH_TERMS:
        for location in LOCATIONS:
            try:
                print(f"  Scraping: '{term}' in '{location}'...")
                jobs = scrape_jobs(
                    site_name=JOB_SITES,
                    search_term=term,
                    location=location,
                    results_wanted=RESULTS_PER_QUERY,
                    hours_old=HOURS_OLD,
                    country_indeed="USA",
                    linkedin_fetch_description=False,  # faster, description not needed
                )
                if not jobs.empty:
                    all_jobs.append(jobs)
                    print(f"    → {len(jobs)} results")
            except Exception as e:
                # don't crash the whole run if one query fails
                print(f"    → ERROR scraping '{term}' in '{location}': {e}")

    if not all_jobs:
        return pd.DataFrame()

    # combine all results and drop duplicate URLs across queries
    combined = pd.concat(all_jobs, ignore_index=True)
    combined = combined.drop_duplicates(subset=["job_url"])
    combined = combined.reset_index(drop=True)

    print(f"\nTotal unique jobs fetched: {len(combined)}")
    return combined
