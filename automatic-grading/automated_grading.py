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
    # TODO: