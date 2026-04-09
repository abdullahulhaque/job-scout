# Job Scout 🧭

Scrapes LinkedIn, Indeed, ZipRecruiter, and Glassdoor every hour and emails you new SWE/ML/SDE job postings. Zero maintenance once deployed.

---

## Setup (one time, ~10 minutes)

### 1. Fork / create this repo on GitHub

Push all these files to a new GitHub repo.

### 2. Get a Gmail App Password

You need an **App Password**, not your regular Gmail password.

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Select app: **Mail**, device: **Other** → name it "Job Scout"
3. Copy the 16-character password it generates

> If you don't see App Passwords, you need to enable 2FA on your Google account first.

### 3. Add GitHub Secrets

In your repo: **Settings → Secrets and variables → Actions → New repository secret**

Add these three secrets:

| Secret name | Value |
|---|---|
| `EMAIL_SENDER` | your Gmail address |
| `EMAIL_RECIPIENT` | where you want emails sent (can be same address) |
| `GMAIL_APP_PASSWORD` | the 16-char app password from step 2 |

### 4. Initialize seen_jobs.json

Create an empty `seen_jobs.json` in the repo root:

```bash
echo "[]" > seen_jobs.json
git add seen_jobs.json
git commit -m "init seen jobs"
git push
```

### 5. Enable GitHub Actions

Go to your repo's **Actions** tab and enable workflows if prompted.

---

## That's it

The workflow runs every hour automatically. First run will send everything found in the last 2 hours. After that, only truly new listings get emailed.

---

## Customization

Edit `config.py` to:
- Add/remove **search terms** (`SEARCH_TERMS`)
- Add/remove **title filters** (`TITLE_INCLUDE` / `TITLE_EXCLUDE`)
- Change **locations** (`LOCATIONS`)
- Adjust how fresh jobs need to be (`HOURS_OLD`)

---

## Trigger manually

Go to **Actions → Job Scout → Run workflow** to trigger it immediately without waiting for the next hour.
