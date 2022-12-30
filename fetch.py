import requests
import json
from termcolor import colored

# Set the GitHub API endpoint and headers
endpoint = "https://api.github.com/search/repositories"
headers = {"Accept": "application/vnd.github+json"}

# Set the search query and number of results to fetch
query = "hacking termux"
num_results = 200

# Send the request to the GitHub API
response = requests.get(f"{endpoint}?q={query}&per_page={num_results}", headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, parse the JSON data
    data = json.loads(response.text)

    print("You can use these tools:")
    # Print the names of the repositories in a numbered list
    for i, repository in enumerate(data["items"], start=1):
        print(f"{i}. {colored(repository['name'], 'red')}")
else:
    # If the request was not successful, print an error message
    print("An error occurred while fetching the data from the API.")