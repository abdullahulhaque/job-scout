from scraper import fetch_jobs
from filter import apply_filters
from dedup import filter_new
from emailer import send_email
from config import PROFILES


def run_profile(profile: dict):
    name = profile["name"]
    print(f"\n{'='*50}")
    print(f"Running profile: {name}")
    print(f"{'='*50}")

    jobs = fetch_jobs(profile)
    if jobs.empty:
        print(f"  [{name}] No jobs returned. Skipping.")
        return

    jobs = apply_filters(jobs, profile)
    if jobs.empty:
        print(f"  [{name}] No jobs passed filter. Skipping.")
        return

    new_jobs = filter_new(jobs, profile)
    if new_jobs.empty:
        print(f"  [{name}] No new jobs since last run. Nothing to send.")
        return

    send_email(new_jobs, profile)


def main():
    for profile in PROFILES:
        run_profile(profile)

    print("\nAll profiles done.")


if __name__ == "__main__":
    main()
