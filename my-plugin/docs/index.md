## Description

This plugin utilizes the tools provided by SheetShuttle to automatically push
grades obtained from a Google Sheet to each individual student's gradebook
GitHub repository. We decided to use Python to program this plugin as it
provides the framework for GitHub interaction and other dependencies with PyPI.
Certain challenges popped up along the way due to most of us not having any experience
with API usage. Also a github token had to be created and we did not have a bunch of
experience with creating and using those. In the future of this project, we wish
to add a feature that will allow us to automate being able to push information into individual
student repositories.

## How to Install and Run the Plugin

The first step in the process of installing this plugin is to run the command `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib` which will allow you to download all of the imports and packages needed in order for the code to function. If python 3 is installed change the `pip` to `pip3` in order to download properly. In order to get the code to print the results from the data sheet, you will want to run the command `python automated-grading` or `python3 automated-grading` depending on what version of python is installed.

You will also want to create an environment by running `poetry install`.

## To run this code, you will need to follow these steps

1)Install the required libraries by running pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client in your terminal.

2)Create a service account and download the private key file. You can do this by following the instructions here: <https://developers.google.com/identity/protocols/oauth2/service-account>.

3)Replace "n_key.json" in the code with the path to the private key file you just downloaded.

4)Replace "/gradebook-" with the base name of the repository you want to use.

5)Replace "1vbO2uR_nJv15Ev5LrcVaBl2FY0A37b3CHj1ABrQhaFA" with the ID of the spreadsheet you want to access.

6)Run the code by calling fetch_info with the appropriate arguments. For example:

```python
fetch_info(
    "/path/to/private_key.json",
    ["https://www.googleapis.com/auth/spreadsheets"],
    "/gradebook-",
    "1234567890abcdefghijklmnopqrstuvwxyz",
)

This will authenticate your service account using the private key file, build a service object using the Google Sheets API, and create a sheet object that you can use to access the specified spreadsheet. You can then use the service and sheet objects to fetch information from the spreadsheet as needed.
```

## How to Use this Plugin

For this plugin to work properly a few steps need to be taken carefully. First you will want to visit `https://console.cloud.google.com/apis/dashboard?project=thematic-bloom-370120`. On this source you will want to click where it says `Create new project` and give it a name. Once created, you will want to activate it. Open your project and scroll until you find `Explore and enable API's` and click on it. Once opened, find the option for the Google Sheets API, open and enable this. Next, a service account will need to be created. Find credentials on the left side bar, and click where it says `Manage service accounts`, then click `CREATE SERVICE ACCOUNT`. Give the account a name which will be assigned as an email. Just think of this as creating a new email. Then permissions will need to be assigned. Make this email the role of the `Editor`. Once this is created, go to the spreadsheet that is going to have information pulled from it, and share the email under the `Share` button. Go back to where the service account was created and select on the account itself, which should look like an email. Then find the button that gives you an option to create a key. It should just say `ADD KEY`. This key will basically act as an account password to be able to login in. Select `CREATE NEW KEY` and select the option that says `JSON`. Place the JSON file in the same folder as where your code is, this will create the actual service account.

## Contributors

Bill, Nic, Brock, Aveet
