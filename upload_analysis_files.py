import os
import glob
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/drive']
)
service = build('drive', 'v3', credentials=credentials)

# ── Set this to your PT folder ID in Google Drive ────────────────────────────
# Get it from the URL when you open the folder: drive.google.com/drive/folders/<FOLDER_ID>
FOLDER_ID = '17Y2SZHGgd9FUbv0gmS9HKLjAzqdKOdAZ'

def upload_or_update(filename, folder_id):
    """Upload a file to Drive, overwriting if a file with the same name exists."""
    name = os.path.basename(filename)
    
    # Check if file already exists in the folder
    results = service.files().list(
        q=f"name='{name}' and '{folder_id}' in parents and trashed=false",
        fields="files(id, name)"
    ).execute()
    existing = results.get('files', [])
    
    media = MediaFileUpload(filename, resumable=False)
    
    if existing:
        # Update existing file
        file_id = existing[0]['id']
        service.files().update(fileId=file_id, media_body=media).execute()
        print(f"Updated {name}")
    else:
        # Create new file in folder
        metadata = {'name': name, 'parents': [folder_id]}
        service.files().create(body=metadata, media_body=media).execute()
        print(f"Created {name}")

# Upload all race .txt files
for txt_file in sorted(glob.glob('race*.txt')):
    upload_or_update(txt_file, FOLDER_ID)

# Upload consolidated CSVs
for csv_file in sorted(glob.glob('*_all_races.csv')):
    upload_or_update(csv_file, FOLDER_ID)

print("Analysis files uploaded successfully!")
