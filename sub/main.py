import os
import re

vod_link = input("Enter the VOD link or ID : ")

vod_id = vod_link.split("/")[-1]

url = "https://vod.544146.workers.dev/" + vod_id

os.system(f"curl {url} > test.txt")

# Create a regex to find all <a> tags
regex = r"<a.*?>"

file_path = "./test.txt"

href = []

# Use regex to find all <a> tags
with open(file_path, "r") as f:
    for line in f:
        if re.search(regex, line):
            # Get the href attribute
            href.append(re.findall(r'href="(.*?)"', line)[0])

os.system(f"start vlc {href[0]}")