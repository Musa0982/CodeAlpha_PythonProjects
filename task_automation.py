# Task 3: Task Automation Scripts
import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

print("Task Automation Menu:")
print("1. Move all .jpg files to 'images' folder")
print("2. Extract emails from a text file")
print("3. Scrape title of a webpage")
choice = input("Choose task (1/2/3): ")

if choice == "1":
    src = input("Enter source folder path: ")
    dest = os.path.join(src, "images")
    os.makedirs(dest, exist_ok=True)

    for file in os.listdir(src):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(src, file), os.path.join(dest, file))
    print("All .jpg files moved to 'images' folder")

elif choice == "2":
    filename = input("Enter text file name: ")
    with open(filename, "r") as f:
        text = f.read()

    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    with open("extracted_emails.txt", "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Extracted {len(emails)} emails into 'extracted_emails.txt'")

elif choice == "3":
    url = input("Enter webpage URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No Title Found"

    with open("webpage_title.txt", "w") as f:
        f.write(f"Title: {title}\n")

    print(f"Webpage title saved in 'webpage_title.txt' → {title}")

else:
    print("Invalid choice")
