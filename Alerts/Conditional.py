# Update send_alert() to include conditional logic; 
def send_alert(message):
    send_email_alert(message, recipient_email="user@example.com")
    send_slack_alert(message, slack_token="your_slack_token", channel="#security-alerts")  

# Note to Self
# Install the packages (smtplib, slack_sdk) using pip
pip install smtplib slack_sdk
