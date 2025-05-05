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
   `Hamburger Menu > Settings > Advanced > Backup Settings`
3. A backup ZIP will be created (default password: `123321`).
4. Copy the backup ZIP file to your PC.

---

### 3️⃣ Generate Subreddit JSON



1. Place `subreddits.txt` and `getData.py` in the same folder.
2. Run:

```bash
python getData.py
```

✅ This will generate `subreddits.json`.

   ![Generated JSON](image-3.png)

---

### 4️⃣ Modify Infinity Backup

1. Extract the backup ZIP file (password: `123321`):

   ![Extract Backup](image-4.png)

2. Inside the extracted folder, open `anonymous_subscribed_subreddits.json`.

3. Replace its entire content with the JSON you copied from `subreddits.json` (created by getData.py).

4. Save the file.

---

### 5️⃣ Repackage and Restore Backup

1. Zip the folder back again (same structure, no extra folder levels):

   ![Zip Folder](image-5.png)

| File                                                                 | Description                   |
| -------------------------------------------------------------------- | ----------------------------- |
| `Infinity_For_Reddit_Settings_Backup_v7.5.0-192-20250505-121658.zip` | Original backup from Infinity |
| `7.5.0/`                                                             | Unzipped folder from backup   |
| `7.5.0.zip`                                                          | **Final zip** to import back  |

2. Copy the final zip back to your phone.
3. Open the **Infinity app** → Go to `Hamburger Menu > Settings > Advanced > Restore Settings`.
4. Select your modified ZIP file to restore.

Done! Now your Infinity app will show your subscribed subreddits — without logging into Reddit.
