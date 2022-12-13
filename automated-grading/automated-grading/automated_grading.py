from googleapiclient.discovery import build
from google.oauth2 import service_account

# generate all the proper credentials needed to fetch info
SERVICE_ACCOUNT_FILE = 'n_key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID sample spreadsheet we want to read and write to
SAMPLE_SPREADSHEET_ID = '1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="JJ_Sample!A1:A16").execute()
#values = result.get('values', [])
print(result)