# ─── Global Settings ───────────────────────────────────────────────────────────

# Job boards to hit
JOB_SITES = ["linkedin", "indeed", "zip_recruiter", "glassdoor"]

# Only fetch jobs posted within the last N hours (2 = safe overlap for hourly runs)
HOURS_OLD = 2

# Max results per search term per location per site
RESULTS_PER_QUERY = 20

# ─── Profiles ──────────────────────────────────────────────────────────────────
# Each profile is an independent search with its own keywords, filters, and recipient.
# Add as many profiles as you want.

PROFILES = [
    {
        "name": "Abdullah",
        "recipient": "ulhaqueabdullah773@gmail.com",

        "search_terms": [
            "new grad software engineer",
            "entry level software engineer",
            "software engineer intern",
            "SWE intern",
            "SDE intern",
            "software engineering internship",
            "co-op software engineer",
            "fall internship software engineer",
            "spring internship software engineer",
            "new graduate software developer",
            "university grad software engineer",
            "early career software engineer",
            "new grad ML engineer",
            "entry level machine learning engineer",
            "new grad AI engineer",
        ],

        "locations": ["United States", "Remote"],

        # title must contain at least one of these
        "title_include": [
            "software",
            "sde",
            "swe",
            "engineer",
            "developer",
            "ml",
            "machine learning",
            "ai engineer",
            "intern",
            "co-op",
            "coop",
            "new grad",
            "entry level",
            "early career",
            "university grad",
            "college grad",
        ],

        # title must NOT contain any of these
        "title_exclude": [
            "senior",
            "sr.",
            "sr ",
            "staff",
            "principal",
            "lead",
            "manager",
            "director",
            "vp ",
            "svp",
            "head of",
            "hardware",
            "electrical",
            "mechanical",
            "civil",
            "chemical",
            "network engineer",
            "embedded",
            "sales intern",
            "marketing intern",
            "finance intern",
            "hr intern",
        ],
    },

    {
        "name": "Imran",
        "recipient": "ulhaque1@yahoo.com",

        "search_terms": [
            "director supply chain",
            "senior director supply chain",
            "VP supply chain",
            "SVP supply chain",
            "head of supply chain",
            "director supply chain transformation",
            "director business applications supply chain",
            "director ERP supply chain",
            "director supply chain technology",
            "VP supply chain operations",
            "director supply chain planning",
            "director IT supply chain",
        ],

        "locations": ["United States", "Remote"],

        # title must contain at least one of these
        "title_include": [
            "director",
            "senior director",
            "vp",
            "svp",
            "vice president",
            "head of",
            "chief supply chain",
        ],

        # title must NOT contain any of these
        "title_exclude": [
            "manager",
            "analyst",
            "associate",
            "coordinator",
            "specialist",
            "intern",
            "assistant",
            "entry level",
            "junior",
            "clinical",
            "sales director",
            "marketing director",
            "finance director",
        ],
    },
]
