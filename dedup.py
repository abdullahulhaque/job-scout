import json
import pandas as pd
from pathlib import Path

MAX_SEEN = 50_000


def _seen_file(profile: dict) -> Path:
    """Each profile gets its own seen file so they don't interfere."""
    name = profile["name"].lower().replace(" ", "_")
    return Path(f"seen_jobs_{name}.json")


def load_seen(profile: dict) -> set:
    path = _seen_file(profile)
    if path.exists():
        with open(path) as f:
            return set(json.load(f))
    return set()


def save_seen(seen: set, profile: dict):
    seen_list = list(seen)
    if len(seen_list) > MAX_SEEN:
        seen_list = seen_list[-MAX_SEEN:]
    with open(_seen_file(profile), "w") as f:
        json.dump(seen_list, f)


def filter_new(jobs: pd.DataFrame, profile: dict) -> pd.DataFrame:
    """Return only jobs not seen before for this profile."""
    seen = load_seen(profile)
    new_jobs = jobs[~jobs["job_url"].isin(seen)].reset_index(drop=True)
    seen.update(jobs["job_url"].tolist())
    save_seen(seen, profile)
    print(f"  [{profile['name']}] New jobs: {len(new_jobs)}")
    return new_jobs
