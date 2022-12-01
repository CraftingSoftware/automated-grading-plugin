from sheetshuttle import sheet_collector
from sheetshuttle import util
from sheetshuttle import github_interaction
from sheetshuttle import github_objects

import yaml

def extract_sheet_data():
    """Extract the sheet data and dump it into a config file."""
    sheets_id = input("Input Google Sheets ID: ")
    # TODO: dump ID into a YAML file
    # reference for YAML format: SheetShuttle/config/sheet_sources/sample_config.yml
    sheet_collector.collect_files(
        # TODO: add YAML file created as input for this method
        )
    # TODO: collect region data with respect to the individual student
    # TODO: get collected regions using sheet_collector.get_regions() method
    # TODO: assign values to:
        # region data
        # region dimensions
        # set default value types to string
    # TODO: print region in markdown table format using print_region() method
    # TODO: write printed region to a markdown file
    #TODO: remove this line after completion:
    return None


def gh_verification():
    """Verify permissions for GitHub interaction."""
    # TODO: check github token
    # TODO: calculate dimensions of regions and fill empty cells
    # TODO: remove this line after completion:
    return None


def gh_pushfile():
    """Push markdown files to individual students' repositories."""
    # TODO: parse through the config file
    # TODO: check if the markdown file already exists in the repo
    # TODO: add files as input to the following functions
    if github_objects.exists():
        github_objects.update_file()
    else:
        github_objects.create_file()
    github_objects.post() # post the file to GitHub repository
    return None

if __name__ == "__main__":
    # Call procedures
    extract_sheet_data()
    gh_verification()
    gh_pushfile()