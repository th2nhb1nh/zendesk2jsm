This is the script to migrate Zendesk to Jira Service Management (JSM)

# Usage
```sh
git clone https://github.com/th2nhb1nh/zendesk2jsm.git
cd zendesk2jsm
python3 -m venv .
source .venv/bin/activate
pip3 install -r requirements.txt
```

In `config.py`, replace all the placeholders of `ZENDESK_SUBDOMAIN`, `ZENDESK_USER_EMAIL`, and `ZENDESK_API_TOKEN` with your real redentials. Then run files matching your needs.
