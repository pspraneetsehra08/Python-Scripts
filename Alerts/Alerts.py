import re
import datetime
import smtplib
from slack_sdk import WebClient

# Regular expressions for detecting suspicious activities
suspicious_patterns = [
    r'(?i)login failed',
    r'(?i)brute force',
    r'(?i)unauthorized access',
    r'(?i)SQL injection'
]

# Function to parse and analyze logs
def analyze_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
        for log in logs:
            log_timestamp, log_message = log.split('|')
            log_timestamp = datetime.datetime.strptime(log_timestamp.strip(), '%Y-%m-%d %H:%M:%S')
            
            for pattern in suspicious_patterns:
                if re.search(pattern, log_message):
                    # Suspicious activity detected
                    alert_message = f"Potential security incident detected:\nTimestamp: {log_timestamp}\nMessage: {log_message}\n"
                    send_alert(alert_message)

# Function to send alerts via email
def send_email_alert(message, recipient_email):
    # Replace the placeholders with your SMTP server details
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "sender@example.com"
    sender_password = "password"
    
    subject = "Security Alert"
    body = message
    
    # Create SMTP connection and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        
        email_message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, email_message)

# Function to send alerts via Slack
def send_slack_alert(message, slack_token, channel):
    client = WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)

# Log file to be analyzed
log_file = "logs.txt"

# Analyze the logs
analyze_logs(log_file)
