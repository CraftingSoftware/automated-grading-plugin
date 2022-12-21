"""This code is interacting with the Google Sheets API and the GitHub API to retrieve data from a Google Sheet and post it to GitHub."""
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import github

# Replace with your own service account key file and list of scopes
SERVICE_ACCOUNT_FILE = "n_key.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def fetch_info():
    """Authenticates with the Google Sheets API using a service account key file and
    a list of scopes, and then builds a service object that can be used to access the API.
    Returns the service object.
    """
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = googleapiclient.discovery.build("sheets", "v4", credentials=credentials)
    return service


def get_grades(service, spreadsheet_id, range_name):
    """Retrieves data from a specific sheet in a Google Sheet specified by its
    spreadsheet_id and range_name, and then formats the data as a list of strings,
    each containing the comma-separated values of a row. Returns the formatted data.
    """
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    rows = result.get("values", [])
    formatted_rows = []
    for row in rows:
        formatted_rows.append(",".join(row))
    return formatted_rows


def main():
    # Collect configuration information
    config = collect_config()

    # Retrieve values from the Google Sheet
    service = fetch_info()
    values = retrieve_spreadsheet_values(
        service, config["spreadsheet_id"], config["range_name"]
    )

    # Post entries to GitHub
    github_manager = create_github_manager(config)
    post_entries(github_manager, values)


def collect_config():
    """Collects configuration information such as the GitHub repository name and
    the Google Sheet spreadsheet_id and range_name. Returns the collected information
    as a dictionary.
    """
    config = {}
    config["repository_name"] = input("Enter the name of the GitHub repository: ")
    config["spreadsheet_id"] = input("Enter the spreadsheet_id of the Google Sheet: ")
    config["range_name"] = input(
        "Enter the range_name of the sheet in the Google Sheet: "
    )
    return config


def retrieve_spreadsheet_values(service, spreadsheet_id, range_name):
    """Retrieves values from a specific sheet in a Google Sheet specified by its
    spreadsheet_id and range_name. Returns the retrieved values.
    """
    return get_grades(service, spreadsheet_id, range_name)


def create_github_manager(config):
    """Creates an instance of the GithubManager class using the provided configuration
    information. Returns the instance.
    """
    return github_interaction.Github

    # we either polish the above code or use this below and delete the redundant parts ps both work


# generate all the proper credentials needed to fetch info
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
# def format_for_markdown(grade_data):
#     # Extract the headers from the first row of the grade data
#     headers = grade_data[0]
#     # Remove the first row (headers) from the grade data
#     grade_data = grade_data[1:]
#     # Initialize an empty list to store the formatted grade data
#     formatted_grade_data = []
#     # Iterate through each row in the grade data
#     for row in grade_data:
#         # Format the row as a string
#         row_string = ",".join(row)
#         # Add the formatted row to the list of formatted grade data
#         formatted_grade_data.append(row_string)
#     return formatted_grade_data
# extracts the headers from the first row of the grade data, removes the first row from the grade data, and
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


# we either polish the above code  or use this below
