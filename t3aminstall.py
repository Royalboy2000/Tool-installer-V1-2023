import os
import sys
import subprocess
import requests
import pyfiglet
import time

def main():
  ascii_art = pyfiglet.figlet_format("team lzyy", font="slant")

  box_width = len(max(ascii_art.split("\n"), key=len)) + 4
  horizontal_rule = "+" + "-" * (box_width - 2) + "+"

  print("\033[95m" + horizontal_rule, end="")
  for line in ascii_art.split("\n"):
    print("\033[95m" + "\n| " + line.center(box_width - 3) + " |", end="")
    time.sleep(0.05)
  print("\033[95m" + "\n" + horizontal_rule + "\033[0m", end="")

  print("\nInstagram: s.a.m.i.r_012")
  print("GitHub:    dream-killer")

  tool = input("\033[94mEnter the name of the tool you want: \033[0m")

  query = f"{tool} in:name"
  headers = {
      "Accept": "application/vnd.github+json"
  }
  params = {
      "q": query
  }
  response = requests.get("https://api.github.com/search/repositories", headers=headers, params=params)
  result = response.json()

  if result["total_count"] == 0:
    print("Sorry, no repositories were found matching your search.")
    return

  best_match = result["items"][0]
  repository_name = best_match["name"]
  repository_url = best_match["html_url"]

  subprocess.run(["git", "clone", repository_url])

  tool_folder = f"tools/{tool}"
  if not os.path.exists(tool_folder):
    os.makedirs(tool_folder)

  subprocess.run(["mv", repository_name, tool_folder])

  print(f"Successfully fetched the best matching {tool} tool and saved it in the {tool_folder} directory.")

if __name__ == "__main__":
  main()