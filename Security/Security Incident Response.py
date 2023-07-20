# Python script to automate security incident response
import requests

# Define API endpoint for security incident management system
incident_management_api = "https://api.securityincidents.com"

# Define authentication credentials
api_key = "your_api_key"

# Define function to create a new incident
def create_incident(title, description, severity):
    payload = {
        "title": title,
        "description": description,
        "severity": severity
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{incident_management_api}/incidents", json=payload, headers=headers)
    
    if response.status_code == 201:
        incident_id = response.json()["id"]
        print(f"Incident created with ID: {incident_id}")
    else:
        print("Failed to create incident")

# Define function to update incident status
def update_incident_status(incident_id, status):
    payload = {
        "status": status
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{incident_management_api}/incidents/{incident_id}", json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Incident status updated to: {status}")
    else:
        print("Failed to update incident status")

# Example usage
incident_title = "Unauthorized Access Attempt"
incident_description = "A user attempted unauthorized access to the system."
incident_severity = "High"

# Create a new incident
create_incident(incident_title, incident_description, incident_severity)

# Update incident status
incident_id = "incident_id_here"
new_status = "Under Investigation"
update_incident_status(incident_id, new_status)
