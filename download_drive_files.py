from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/drive']  # full read/write
)

service = build('drive', 'v3', credentials=credentials)

def download_file(file_id, filename):
    request = service.files().get_media(fileId=file_id)
    with open(filename, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Downloading {filename}: {int(status.progress() * 100)}%")

# Add your files here — get the file ID from the Google Drive share link
# e.g. https://drive.google.com/file/d/THIS_PART_IS_THE_ID/view
download_file('your_file_id_here', 'myfile.csv')
download_file('your_file_id_here', 'anotherfile.xlsx')
```

To get your **file ID**, right-click the file in Google Drive → **"Share"** → **"Copy link"**. The link looks like:
```
https://drive.google.com/file/d/1aBcDeFgHiJkLmNoPqRsTuVwXyZ/view
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
                                  This is your file ID
