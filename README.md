# Automated Grading Tool for SheetShuttle

![Checks](https://camo.githubusercontent.com/84431507f786bfa8c0bff10a98b719e2d78ac35b51057b24898f57004bacf585/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636865636b732d7374617475732f434d5053432d3230332d416c6c656768656e792d436f6c6c6567652d46616c6c2d323032322f546965722d636f6d70617269736f6e2f30313464666263316265393038663633663836326630333964323637383133623237333464313837)
![License](https://img.shields.io/badge/license-MIT-blue)
![BuiltWith](https://img.shields.io/badge/Built%20With-Python-blue)

![AutomatedGradingTool](images/Logo.png)

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

## How to Use this Plugin

For this plugin to work properly a few steps need to be taken carefully. First you will want to visit `https://console.cloud.google.com/apis/dashboard?project=thematic-bloom-370120`. On this source you will want to click where it says `Create new project` and give it a name. Once created, you will want to activate it. Open your project and scroll until you find `Explore and enable API's` and click on it. Once opened, find the option for the Google Sheets API, open and enable this. Next, a service account will need to be created. Find credentials on the left side bar, and click where it says `Manage service accounts`, then click `CREATE SERVICE ACCOUNT`. Give the account a name which will be assigned as an email. Just think of this as creating a new email. Then permissions will need to be assigned. Make this email the role of the `Editor`. Once this is created, go to the spreadsheet that is going to have information pulled from it, and share the email under the `Share` button. Go back to where the service account was created and select on the account itself, which should look like an email. Then find the button that gives you an option to create a key. It should just say `ADD KEY`. This key will basically act as an account password to be able to login in. Select `CREATE NEW KEY` and select the option that says `JSON`. Place the JSON file in the same folder as where your code is, this will create the actual service account.

## Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/ningerson2002"><img src="https://avatars.githubusercontent.com/u/89281233?v=4" width="100px;" alt=""/><br /><sub><b>Nic Ingerson</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/BillOchieng"><img src="https://avatars.githubusercontent.com/u/79288574?v=4" width="100px;" alt=""/><br /><sub><b>Bill Ochieng</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/brum0505"><img src="https://avatars.githubusercontent.com/u/89416744?v=4" width="100px;" alt=""/><br /><sub><b>Brock Brumfield</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/aveetdesai"><img src="https://avatars.githubusercontent.com/u/54788544?v=4" width="100px;" alt=""/><br /><sub><b>Aveet Desai</b></sub></a><br /></td>
  </tr>
</table>

You could refactor the code to make it more modular and easier to understand. For example, you could create separate functions for each of the main steps (collecting configuration, posting all collected entries, and retrieving values from the spreadsheet). This would make it easier to test and debug the code, as well as make it more readable.

You could add error handling to the code. For example, you could use try-except blocks to handle any exceptions that might be raised when interacting with the GitHub API or Google Sheets API. This would make the code more robust and ensure that it continues to run smoothly even if something goes wrong.

You could add additional functionality to the code. For example, you might want to allow the user to specify the range of cells to retrieve from the spreadsheet, or add a feature that allows the user to post grades for a specific student rather than all students at once.

You could add more documentation to the code to explain what it does and how to use it. This would make it easier for other people to understand and use the code.

You could optimize the code to run more efficiently. For example, you could use techniques such as lazy loading or caching to reduce the number of API calls made or to improve the performance of the code.
