import json
from google.oauth2 import service_account
import googleapiclient.discovery

# Scopes required by this endpoint ->  https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

# Service Account Credentials to be used. How to create at https://developers.google.com/workspace/guides/create-credentials#service-account
SERVICE_ACCOUNT_FILE = 'SERVICE_ACCOUNT_CREDENTIALS.json'

# Super Admin account to be impersonated by the Service account created
DELEGATE = 'SUPERADMIN@YOURDOMAIN.COM'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials_delegated = credentials.with_subject(DELEGATE)

service = googleapiclient.discovery.build(
    'admin', 'directory_v1', credentials=credentials_delegated)

# JSON template to be used for user creation. Additional fields can be found at https://developers.google.com/admin-sdk/directory/reference/rest/v1/users#User
newUserInfo = {
    "name": {
        "familyName": "Doe",
        "givenName": "John"
    },
    "password": "A_SECURE_PASSWORD**",
    "primaryEmail": "USERNAME@YOURDOMAIN.COM",
}
response = service.users().insert(body=newUserInfo).execute()

print(response)
