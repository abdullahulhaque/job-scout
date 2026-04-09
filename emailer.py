import os
import smtplib
import pandas as pd
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def _build_html(jobs: pd.DataFrame) -> str:
    """Build a clean HTML email table from the jobs DataFrame."""

    rows = ""
    for _, job in jobs.iterrows():
        title    = job.get("title", "N/A")
        company  = job.get("company", "N/A")
        location = job.get("location", "N/A")
        site     = str(job.get("site", "N/A")).capitalize()
        posted   = str(job.get("date_posted", "")).split(" ")[0]  # just the date
        url      = job.get("job_url", "#")
        remote   = "🌐 Remote" if job.get("is_remote") else ""

        rows += f"""
        <tr>
          <td style="padding:10px 8px;border-bottom:1px solid #eee;">
            <a href="{url}" style="font-weight:600;color:#0066cc;text-decoration:none;">{title}</a>
            {"<br><span style='font-size:11px;color:#27ae60;'>" + remote + "</span>" if remote else ""}
          </td>
          <td style="padding:10px 8px;border-bottom:1px solid #eee;font-size:13px;">{company}</td>
          <td style="padding:10px 8px;border-bottom:1px solid #eee;font-size:13px;">{location}</td>
          <td style="padding:10px 8px;border-bottom:1px solid #eee;font-size:12px;color:#888;">{site}</td>
          <td style="padding:10px 8px;border-bottom:1px solid #eee;font-size:12px;color:#888;">{posted}</td>
        </tr>
        """

    timestamp = datetime.now().strftime("%b %d, %Y — %I:%M %p")

    html = f"""
    <html>
    <body style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:20px;color:#333;">
      <h2 style="margin-bottom:4px;">🧭 Job Scout</h2>
      <p style="color:#888;margin-top:0;">{timestamp} &nbsp;·&nbsp; <strong>{len(jobs)}</strong> new postings</p>

      <table style="width:100%;border-collapse:collapse;margin-top:16px;">
        <thead>
          <tr style="background:#f7f7f7;text-align:left;font-size:12px;text-transform:uppercase;color:#999;">
            <th style="padding:8px;">Role</th>
            <th style="padding:8px;">Company</th>
            <th style="padding:8px;">Location</th>
            <th style="padding:8px;">Source</th>
            <th style="padding:8px;">Posted</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>

      <p style="color:#bbb;font-size:11px;margin-top:24px;">
        Job Scout runs hourly via GitHub Actions. 
        To stop emails, disable the workflow in your repo.
      </p>
    </body>
    </html>
    """
    return html


def send_email(jobs: pd.DataFrame):
    """Send the job digest email via Gmail SMTP."""
    sender    = os.environ["EMAIL_SENDER"]
    recipient = os.environ["EMAIL_RECIPIENT"]
    password  = os.environ["GMAIL_APP_PASSWORD"]

    count     = len(jobs)
    timestamp = datetime.now().strftime("%b %d %I:%M %p")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Job Scout — {count} new posting{'s' if count != 1 else ''} ({timestamp})"
    msg["From"]    = sender
    msg["To"]      = recipient

    msg.attach(MIMEText(_build_html(jobs), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

    print(f"Email sent to {recipient} with {count} jobs")
