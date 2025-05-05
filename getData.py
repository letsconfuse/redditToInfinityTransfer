import json
import requests

# Step 1: Read subreddit names from file
with open("subreddits.txt", "r") as file:
    subreddit_names = [line.strip() for line in file if line.strip()]

# Step 2: Function to fetch subreddit info
def fetch_subreddit_info(subreddit_name):
    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "favorite": False,
            "iconUrl": data['data'].get('icon_img', ''),
            "id": data['data']['name'],  # e.g., t5_xxxxx
            "name": data['data']['display_name'],
            "username": "-"
        }
    else:
        print(f"Error fetching data for: {subreddit_name}")
        return None

# Step 3: Fetch info for all subreddits
subreddits_info = []
for name in subreddit_names:
    info = fetch_subreddit_info(name)
    if info:
        subreddits_info.append(info)

# Step 4: Write to JSON
with open("subreddits.json", "w") as outfile:
    json.dump(subreddits_info, outfile)

print("✅ subreddits.json created successfully.")
