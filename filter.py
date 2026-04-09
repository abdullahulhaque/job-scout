import pandas as pd
from config import TITLE_INCLUDE, TITLE_EXCLUDE


def apply_filters(jobs: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only jobs whose title contains an include keyword
    and does NOT contain any exclude keyword.
    """
    if jobs.empty:
        return jobs

    # normalize title to lowercase for case-insensitive matching
    titles = jobs["title"].str.lower().fillna("")

    # must contain at least one include keyword
    include_mask = titles.apply(
        lambda t: any(kw in t for kw in TITLE_INCLUDE)
    )

    # must not contain any exclude keyword
    exclude_mask = titles.apply(
        lambda t: any(kw in t for kw in TITLE_EXCLUDE)
    )

    filtered = jobs[include_mask & ~exclude_mask].reset_index(drop=True)
    print(f"After title filter: {len(filtered)} jobs (removed {len(jobs) - len(filtered)})")
    return filtered
