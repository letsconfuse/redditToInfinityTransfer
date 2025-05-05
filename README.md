# 📥 Transfer Your Reddit Subscriptions to Infinity (Without Login)

This guide allows you to transfer your Reddit subscribed subreddits to the **Infinity for Reddit** app **without logging in**, using your exported subreddit list and a simple JSON replacement.

---

## ✅ Overview

We’ll export your subreddit list from Reddit’s website, convert it to JSON, and inject it into Infinity’s settings backup file.

No Reddit API keys, no OAuth — just basic file editing!

---

## 🚀 Steps

### 1️⃣ Export Your Subreddit List

1. Open [https://old.reddit.com/subreddits/mine/](https://old.reddit.com/subreddits/mine/) in your browser.

2. Select the list of your subscribed subreddits (as shown in the screenshot):

   ![Select Subreddits](image.png)

3. Paste this list into a new file called `subreddits.txt` in **VS Code** or any text editor.

4. Use **Find and Replace** to remove unwanted prefixes (like `leave`):

   ![Find and Replace](image-2.png)

✅ You should now have a **clean list** of subreddit names, one per line.

---

### 2️⃣ Export Infinity Settings

1. On your mobile device, open the **Infinity** app.
2. Go to:
   `Hamburger Menu > Settings > Advanced > Restore Settings`
3. A backup ZIP will be created (default password: `123321`).
4. Copy the backup ZIP file to your PC.

---

### 3️⃣ Generate Subreddit JSON

#### `getData.py` script:

```python
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
```

1. Place `subreddits.txt` and `getData.py` in the same folder.
2. Run:

```bash
python getData.py
```

✅ This will generate `subreddits.json`.

3. Open `subreddits.json` and **copy everything inside**:

   ![Generated JSON](image-3.png)

---

### 4️⃣ Modify Infinity Backup

1. Extract the backup ZIP file (password: `123321`):

   ![Extract Backup](image-4.png)

2. Inside the extracted folder, open `anonymous_subscribed_subreddits.json`.

3. Replace its contents with the copied JSON from `subreddits.json`.

4. Save the file.

---

### 5️⃣ Repackage Backup

1. Zip the folder back again (same structure, no extra folder levels):

   ![Zip Folder](image-5.png)

| File                                                                 | Description                   |
| -------------------------------------------------------------------- | ----------------------------- |
| `Infinity_For_Reddit_Settings_Backup_v7.5.0-192-20250505-121658.zip` | Original backup from Infinity |
| `7.5.0/`                                                             | Unzipped folder from backup   |
| `7.5.0.zip`                                                          | **Final zip** to import back  |

✅ Now restore this modified backup in the **Infinity app** → Settings → Restore Settings.

Enjoy your subscribed subreddits without logging in! 🎉
