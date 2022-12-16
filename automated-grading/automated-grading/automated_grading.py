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

# This function definition creates a function called fetch_info that takes four parameters:
# service_account_file, scopes, base_repo_name, and spreadsheet_id. When you call the function,
# you can pass in the values for these parameters,
# and the function will use those values to generate the credentials and fetch the info


def fetch_info(service_account_file, scopes, base_repo_name, spreadsheet_id):
    creds = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    # other code to fetch info using the service and sheet objects goes here
    # You can call the function like this:
    fetch_info(
        "n_key.json",
        ["https://www.googleapis.com/auth/spreadsheets"],
        "/gradebook-",
        "1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA",
    )


# This will use the values "n_key.json", ["https://www.googleapis.com/auth/spreadsheets"], "/gradebook-", and "1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA" as the arguments
# for the service_account_file, scopes, base_repo_name, and spreadsheet_id parameters, respectively


def get_grades():
    # Call the Sheets API
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:AM38")
        .execute()
    )
    values = result.get("values", [])
    student_grade_data = [",".join(row) for row in values]
    return student_grade_data


# eliminates the inner loop and uses a list comprehension to create a list of strings,
# each containing the comma-separated values of a row.


def format_for_markdown(grade_data):
    # Extract the headers from the first row of the grade data
    headers = grade_data[0]
    # Remove the first row (headers) from the grade data
    grade_data = grade_data[1:]
    # Initialize an empty list to store the formatted grade data
    formatted_grade_data = []
    # Iterate through each row in the grade data
    for row in grade_data:
        # Format the row as a string
        row_string = ",".join(row)
        # Add the formatted row to the list of formatted grade data
        formatted_grade_data.append(row_string)
    return formatted_grade_data


# extracts the headers from the first row of the grade data, removes the first row from the grade data, and
or 
def get_grades():
    # Call the Sheets API
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:AM38")
        .execute()
    )
    values = result.get("values", [])
    student_grade_data = [",".join(row) for row in values]
    formatted_grade_data = format_for_markdown(student_grade_data)
    return formatted_grade_data
# then call the function as 
grade_data = get_grades()


# then uses a loop to iterate through the remaining rows and format each one as a string.


def main():
    my_manager = github_interaction.GithubManager()
    my_manager.collect_config()

    # All collected entries can be posted at once
    my_manager.post_all()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:AM")
        .execute()
    )
    values = result.get("values", [])

    # OR they can be posted individually by type
    my_manager.post_issues()
    my_manager.post_pull_requests()
    my_manager.post_files()


format_for_markdown(get_grades())


# Extract the code that interacts with the GitHub API into a separate function.
def collect_config():
    # Collect configuration information
    manager.collect_config()


# Extract the code that retrieves values from the spreadsheet into a separate function
def retrieve_spreadsheet_values():
    # Retrieve values from Sheet1 of the specified spreadsheet
    sheet_values = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:AM")
        .execute()
    )
    values = sheet_values.get("values", [])


# Extract the code that collects configuration information into a separate function
def post_entries():
    # Post all collected entries
    manager.post_all()


def create_github_manager():
    # Create a GithubManager object
    manager = github_interaction.GithubManager()
    return manager


def collect_and_post_data(manager):
    collect_config()
    post_entries()


def retrieve_spreadsheet_values():
    # Retrieve values from Sheet1 of the specified spreadsheet
    sheet_values = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:AM")
        .execute()
    )
    values = sheet_values.get("values", [])


def main():
    manager = create_github_manager()
    collect_and_post_data(manager)
    retrieve_spreadsheet_values()
