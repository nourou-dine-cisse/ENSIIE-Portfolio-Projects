from email.message import EmailMessage
import smtplib

SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "9eaf0548073a88"
SMTP_PASS = "5ea779ecf03885"

# adresse que tu veux faire apparaître comme expéditeur
from_address = "pref@hotmail.com"
# adresse qui reçoit (ex: Mailinator ou Mailtrap inbox)
to_address = "ncisse03@gmail.com"
subject = "Test: expéditeur choisi"
body = "Ceci est un test. From header forcé."

msg = EmailMessage()
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject
msg.set_content(body)

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
    s.starttls()
    s.login(SMTP_USER, SMTP_PASS)
    s.send_message(msg)

print("Envoyé.")
