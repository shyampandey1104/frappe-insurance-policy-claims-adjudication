# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "insurance"
app_title = "Frappe Insurance Policy Claims Adjudication"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Insurance Policy Claims Adjudication - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/insurance/css/insurance.bundle.css"
app_include_js = "/assets/insurance/js/insurance.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Insurance Policy Claims Adjudication Entry": {
        "validate": "insurance.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "insurance.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "insurance.tasks.hourly_sync"
    ],
    "daily": [
        "insurance.tasks.daily_reconciliation"
    ],
    "weekly": [
        "insurance.tasks.weekly_digest"
    ]
}
