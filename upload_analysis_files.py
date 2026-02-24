import os
import glob
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import httplib2

credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/drive']
)
service = build('drive', 'v3', credentials=credentials)

FOLDER_ID = '17Y2SZHGgd9FUbv0gmS9HKLjAzqdKOdAZ'

def upload_or_update(filename, folder_id, retries=3, delay=15):
    name = os.path.basename(filename)
    
    results = service.files().list(
        q=f"name='{name}' and '{folder_id}' in parents and trashed=false",
        fields="files(id, name)"
    ).execute()
    existing = results.get('files', [])

    for attempt in range(1, retries + 1):
        try:
            # resumable=True handles large files and is more resilient to timeouts
            media = MediaFileUpload(filename, resumable=True)

            if existing:
                file_id = existing[0]['id']
                service.files().update(fileId=file_id, media_body=media).execute()
                print(f"Updated {name}")
            else:
                metadata = {'name': name, 'parents': [folder_id]}
                service.files().create(body=metadata, media_body=media).execute()
                print(f"Created {name}")
            break  # success

        except Exception as e:
            print(f"Attempt {attempt} failed for {name}: {e}")
            if attempt < retries:
                print(f"Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"All {retries} attempts failed for {name}. Raising.")
                raise

for txt_file in sorted(glob.glob('race*.txt')):
    upload_or_update(txt_file, FOLDER_ID)

for csv_file in sorted(glob.glob('*_all_races.csv')):
    upload_or_update(csv_file, FOLDER_ID)

print("Analysis files uploaded successfully!")
