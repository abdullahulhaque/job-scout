# ─── Search Settings ───────────────────────────────────────────────────────────

# Terms sent to each job board
SEARCH_TERMS = [
    "software engineer",
    "software developer",
    "SDE",
    "ML engineer",
    "machine learning engineer",
    "AI engineer",
    "new grad software engineer",
]

# Locations to search
LOCATIONS = ["United States", "Remote"]

# Job boards to hit
JOB_SITES = ["linkedin", "indeed", "zip_recruiter", "glassdoor"]

# Only fetch jobs posted within the last N hours (2 = safe overlap for hourly runs)
HOURS_OLD = 2

# Max results per search term per location per site
RESULTS_PER_QUERY = 20

# ─── Title Filters ─────────────────────────────────────────────────────────────

# Job title must contain at least one of these
TITLE_INCLUDE = [
    "software",
    "sde",
    "swe",
    "engineer",
    "developer",
    "ml ",
    "machine learning",
    "ai engineer",
]

# Job title must NOT contain any of these
TITLE_EXCLUDE = [
    "senior",
    "sr.",
    "sr ",
    "staff",
    "principal",
    "lead",
    "manager",
    "director",
    "vp ",
    "head of",
    "hardware",
    "electrical",
    "mechanical",
    "civil",
    "chemical",
    "network engineer",
    "devops",          # remove if you want devops roles
    "embedded",
]

# ─── Email Config (set these as GitHub Secrets, not here) ──────────────────────
# Secrets needed:
#   EMAIL_SENDER       - your Gmail address
#   EMAIL_RECIPIENT    - where to send the digest (can be same address)
#   GMAIL_APP_PASSWORD - Gmail app password (not your regular password)
#                        Generate at: myaccount.google.com/apppasswords
