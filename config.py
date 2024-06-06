import os
import base64

class Config:
    ZENDESK_SUBDOMAIN = 'YOUR_ZENDESK_SUBDOMAIN'
    ZENDESK_USER_EMAIL = 'YOUR_ZENDESK_EMAIL_ADDRESS'
    ZENDESK_API_TOKEN = 'YOUR_ZENDESK_API_TOKEN'
    ZENDESK_TOKEN = base64.b64encode(f"{ZENDESK_USER_EMAIL}/token:{ZENDESK_API_TOKEN}".encode('utf-8')).decode('utf-8')

    ZENDESK_HEADERS = {
        "Authorization": f"Basic {ZENDESK_TOKEN}",
        "Accept": "application/json"
    }

    ZENDESK_BASE_URL = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2"
    PAGE_SIZE = 100

JIRA_URL = "YOUR_JIRA_URL"
JIRA_EMAIL = "YOUR_EMAIL"
JIRA_API_KEY = "YOUR_API_KEY"
JIRA_TOKEN = base64.b64encode(f"{JIRA_EMAIL}:{JIRA_API_KEY}".encode('utf-8')).decode('utf-8')

JIRA_HEADERS = {
    "Authorization": f"Basic {JIRA_TOKEN}",
    "Accept": "application/json"
}
