import pandas as pd


def apply_filters(jobs: pd.DataFrame, profile: dict) -> pd.DataFrame:
    """
    Keep only jobs whose title contains an include keyword
    and does NOT contain any exclude keyword.
    """
    if jobs.empty:
        return jobs

    title_include = profile["title_include"]
    title_exclude = profile["title_exclude"]
    name = profile["name"]

    titles = jobs["title"].str.lower().fillna("")

    include_mask = titles.apply(lambda t: any(kw in t for kw in title_include))
    exclude_mask = titles.apply(lambda t: any(kw in t for kw in title_exclude))

    filtered = jobs[include_mask & ~exclude_mask].reset_index(drop=True)
    print(f"  [{name}] After filter: {len(filtered)} jobs (removed {len(jobs) - len(filtered)})")
    return filtered
