import json
import pandas as pd
from pathlib import Path

SEEN_FILE = Path("seen_jobs.json")

# cap how many URLs we store so the file doesn't grow forever (~30 days of runs)
MAX_SEEN = 50_000


def load_seen() -> set:
    """Load previously seen job URLs from disk."""
    if SEEN_FILE.exists():
        with open(SEEN_FILE) as f:
            return set(json.load(f))
    return set()


def save_seen(seen: set):
    """Persist seen URLs back to disk, capped at MAX_SEEN."""
    seen_list = list(seen)
    if len(seen_list) > MAX_SEEN:
        # keep the most recent entries (rough trim — order not guaranteed in a set)
        seen_list = seen_list[-MAX_SEEN:]
    with open(SEEN_FILE, "w") as f:
        json.dump(seen_list, f)


def filter_new(jobs: pd.DataFrame) -> pd.DataFrame:
    """
    Return only jobs we haven't seen before.
    Updates and saves the seen set as a side effect.
    """
    seen = load_seen()

    # identify new jobs
    new_jobs = jobs[~jobs["job_url"].isin(seen)].reset_index(drop=True)

    # add ALL current job URLs to seen (new + old), then save
    seen.update(jobs["job_url"].tolist())
    save_seen(seen)

    print(f"New jobs (not seen before): {len(new_jobs)}")
    return new_jobs
