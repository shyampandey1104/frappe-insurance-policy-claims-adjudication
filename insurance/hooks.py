# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "insurance"
app_title = "Frappe Insurance Policy Claims Adjudication"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Insurance Policy Claims Adjudication for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/insurance/css/insurance.bundle.css"
app_include_js = "/assets/insurance/js/insurance.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "insurance.engine.on_document_submit",
        "on_cancel": "insurance.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "insurance.engine.daily_scheduled_sync"
    ]
}
