import os

GA_CONFIG = {
    'api_name': 'analytics',
    'api_version': 'v3',
    'scope': ['https://www.googleapis.com/auth/analytics.readonly'],
    'service_account_email': 'your_acc_email.iam.gserviceaccount.com',
    'key_file_location': os.getcwd() + '/client_secrets.p12',
}


PROFILE_ID = 'ga:12345678'
