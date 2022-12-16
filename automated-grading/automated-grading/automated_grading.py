from googleapiclient.discovery import build
from google.oauth2 import service_account
from sheetshuttle import github_interaction


# generate all the proper credentials needed to fetch info
SERVICE_ACCOUNT_FILE = "n_key.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
BASE_REPO_NAME = "/gradebook-"

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# The ID sample spreadsheet we want to read and write to
SAMPLE_SPREADSHEET_ID = "1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA"
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()


def get_grades():
  # Call the Sheets API
  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range="Sheet1!A1:AM38").execute()
  values = result.get('values', [])
  student_grade_data = []
  for row in values:
    # Print the row, with each column separated by a comma
    l = []
    student_grades = (','.join(row))
    l.append(student_grades)
    student_grade_data.append(l)
  return student_grade_data
  

def format_for_markdown(grade_data):
  """Format student grade data for printing to a markdown.
  Args:
    grade_data: List of student grade data.
  """
  headers = []
  formatted_grade_data = []
  # iterate through each row, and
  # --> return a string containing each grade as well as the assignment name
  for element in grade_data[0]:
    headers.append(element)
  grade_data.remove(headers)
  print(grade_data)


def main():
  my_manager = github_interaction.GithubManager()
  my_manager.collect_config()

  # All collected entries can be posted at once
  my_manager.post_all()
  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range="Sheet1!A1:AM").execute()
  values = result.get('values', [])

  # OR they can be posted individually by type
  my_manager.post_issues()
  my_manager.post_pull_requests()
  my_manager.post_files()

format_for_markdown(get_grades())