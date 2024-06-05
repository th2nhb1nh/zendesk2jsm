import os
import base64

ZENDESK_SUBDOMAIN = 'YOUR_ZENDESK_SUBDOMAIN'
ZENDESK_USER_EMAIL = 'YOUR_ZENDESK_EMAIL_ADDRESS'
ZENDESK_API_TOKEN = 'YOUR_ZENDESK_API_TOKEN'
TOKEN = base64.b64encode(f"{ZENDESK_USER_EMAIL}/token:{ZENDESK_API_TOKEN}".encode('utf-8')).decode('utf-8')

HEADERS = {
    "Authorization": f"Basic {TOKEN}",
    "Accept": "application/json"
}

BASE_URL = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2"
PAGE_SIZE = 100
