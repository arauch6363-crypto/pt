from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/drive']
)
service = build('drive', 'v3', credentials=credentials)

def upload_file(file_id, filename):
    if os.path.exists(filename):
        media = MediaFileUpload(filename)
        service.files().update(fileId=file_id, media_body=media).execute()
        print(f"Uploaded {filename} successfully!")
    else:
        print(f"Skipping {filename} - file not found")

upload_file('19g1udGm83tmRNTr10v598jtRox-bOWxq', 'runners_tdy.parquet')
upload_file('1fqLUYNF1nfaCsw2K95fi-bWj4Jg0qdDo', 'webTips_tdy.parquet')
upload_file('1Cx_juo4BT97gAqFysRQZyu8si_kb-zaU', 'odds_tdy.parquet')
upload_file('1m3rf0xZxKqIQejHYXWLkL1Dx7NDzNbZD',   'df_with_ratings.parquet')
upload_file('1LG2GvIrv84popZCY9jKJ8YX0Yjq-NUGL',     'ratings_state.json')
upload_file('1O_36ELAU98GPvOBKs-ltdB_Z6bqkjK78', 'ratings_last_date.txt')

print("Today update files uploaded successfully!")
