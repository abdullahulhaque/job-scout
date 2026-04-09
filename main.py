from scraper import fetch_jobs
from filter import apply_filters
from dedup import filter_new
from emailer import send_email


def main():
    print("=" * 50)
    print("Job Scout starting...")
    print("=" * 50)

    # 1. scrape all job boards
    jobs = fetch_jobs()

    if jobs.empty:
        print("No jobs returned from any source. Exiting.")
        return

    # 2. filter by title (remove senior/irrelevant roles)
    jobs = apply_filters(jobs)

    if jobs.empty:
        print("No jobs passed title filter. Exiting.")
        return

    # 3. remove jobs we've already seen
    new_jobs = filter_new(jobs)

    if new_jobs.empty:
        print("No new jobs since last run. Nothing to send.")
        return

    # 4. send email digest
    send_email(new_jobs)

    print("=" * 50)
    print(f"Done. {len(new_jobs)} new jobs sent.")
    print("=" * 50)


if __name__ == "__main__":
    main()
