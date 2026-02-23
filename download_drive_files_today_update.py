from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io, os

credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/drive']
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

download_file('1tS8DsbCzeTUMj-DsB8A7bvM-XSCFa537', 'races_tdy.parquet')
download_file('19g1udGm83tmRNTr10v598jtRox-bOWxq', 'runners_tdy.parquet')
download_file('1fqLUYNF1nfaCsw2K95fi-bWj4Jg0qdDo', 'webTips_tdy.parquet')
download_file('1Cx_juo4BT97gAqFysRQZyu8si_kb-zaU', 'odds_tdy.parquet')
print("Today update files downloaded successfully!")
