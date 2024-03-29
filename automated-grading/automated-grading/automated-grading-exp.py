import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from sheetshuttle import github_interaction, sheet_collector, util


# generate all the proper credentials needed to fetch info
SERVICE_ACCOUNT_FILE = "n_key.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# The ID sample spreadsheet we want to read and write to
SAMPLE_SPREADSHEET_ID = "1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA"

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:AM38").execute()
values = result.get('values', [])

# Get the column headers from the first row of the spreadsheet
headers = values[0]

# Create a dictionary to store the data for each row, with the keys being the column headers
rows = []
for row in values[1:]:
  row_data = {}
  for i, header in enumerate(headers):
    row_data[header] = row[i]
  rows.append(row_data)

# User defined folder to store the markdown files
folder = "student_grades"


# Create the folder if it does not exist
if not os.path.exists(folder):
  os.makedirs(folder)

# Prompt the user to enter the name of the repository and the access token
#nrepository = input("Enter the name of the repository: ")
# access_token = input("Enter the access token for your GitHub account: ")

# Iterate over the rows and create a markdown file for each one
for row in rows:
  # Get the name for the file from the first column of the row
  filename = row[headers[0]] + ".md"
  # Specify the path to the markdown file
  filepath = os.path.join(folder, filename)
  with open(filepath, "w") as f:
    # Write the contents of each column to the file as markdown
    for header in headers:
      f.write("**" + header + ":** " + row[header] + "\n")

  # push the file to the GitHub repository
  # github_interaction.push_to_github(filename, repository, access_token)
