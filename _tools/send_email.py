#!/usr/bin/env python3
"""Send email via SMTP. Configure via environment variables."""

import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.hostinger.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")

def send_email(to_addr: str, subject: str, body_html: str):
    if not SMTP_USER or not SMTP_PASS:
        print("Erro: Configure SMTP_USER e SMTP_PASS no ambiente ou .env")
        sys.exit(1)

    msg = MIMEMultipart("alternative")
    msg["From"] = f"OpenPRD <{SMTP_USER}>"
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html", "utf-8"))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, to_addr, msg.as_string())
    print(f"Email sent to {to_addr}")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        send_email(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: SMTP_USER=x SMTP_PASS=y python send_email.py <to> <subject> <body_html>")
