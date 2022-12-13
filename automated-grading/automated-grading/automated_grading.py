"""This file when put into `sheetshuttle/plugins`, can run to display the student grades whenever an update is made."""
from sheetshuttle import sheet_collector
from sheetshuttle import util
from sheetshuttle import github_interaction
from sheetshuttle import github_objects

import yaml

# file that has authentication info, don't push `"n_key.json"` to Github!
key_file = "n_key.json"
# Directory containing config info for our sheets
src_directory = "config.yml"


def collect(sheets_keys_file, sheets_config_directory, **kwargs):
    """This function collects and fetches information from google sheets."""
    # has_credentials = google_credentials(key_file)
    # if has_credentials:
    #     raise Exception(f"ERROR: No credentials found in {key_file}")
    collector = sheet_collector.SheetCollector(key_file, src_directory)
    # sheet collector object called collector with args key_file and src_dir
    collector.collect_files()
    old_data_dict = {}
    # TODO: collect region data with respect to the individual student
    for region_data in collector.sheets_data["config"].regions:
        print(region_data.data)
        # TODO:iterate through diff regions
        # covert region data into a dictionary so as to assign keys and values
        my_data = region_data.data
        new_data_dict = my_data.to_dict()
        old_data_dict.update(new_data_dict)

    # set default value types to string
    # TODO: print region in markdown table format using print_region() method
    # TODO: write printed region to a markdown file
    # TODO: remove this line after completion:
    return None

def gh_verification(username, access_token):
    """Verify permissions for GitHub interaction."""
  # Set up the API endpoint and authorization headers
      # TODO: check github token
    endpoint = "https://api.github.com/user/repos"
    headers = {
    "Authorization": "Bearer {}".format(access_token)
    }

    # Send a GET request to the API endpoint to retrieve the user's repositories
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful and the user has permission to interact with GitHub
    if response.status_code == 200 and response.json()[0]["owner"]["login"] == username:
        return True
    else:
        return False
    # TODO: calculate dimensions of regions and fill empty cells
    # TODO: remove this line after completion:
    # return None

def gh_pushfile():
    """Push markdown files to individual students' repositories."""
    # TODO: parse through the config file
    # TODO: check if the markdown file already exists in the repo
    # TODO: add files as input to the following functions
    if github_objects.exists():
        github_objects.update_file()
    else:
        github_objects.create_file()
    github_objects.post()  # post the file to GitHub repository
    return None


if __name__ == "__main__":
    # Call procedures
    extract_sheet_data()
    gh_verification()
    gh_pushfile()

# sheetshuttle -pd /Users/rawlings/Desktop/Software class/automated-grading-plugin/automated-grading/automated-grading -pn automated_grading

# sheetshuttle -pd plugin -pn automated-grading -cd plugin_config
# sheetshuttle -pd /Users/rawlings/Desktop/Software class/automated-grading-plugin/automatic-grading/automatic-grading -pn APR_Generator

# /Users/rawlings/Desktop/Software class/automated-grading-plugin/automatic-grading/automatic-grading