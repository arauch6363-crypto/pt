from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

# Load credentials
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

download_file('1diodI8USw9TgMqTVWJHzEG7P3rkBZOL_', 'races.parquet')
download_file('1Tv20gDn7EWZMNIc0Nu9KRFJk-NM8OVgT', 'runners.parquet')
download_file('1-1dPegROQWIMhEHb8y2PezKfrLiE1x-6', 'reload_tracker.csv')
download_file('1DrevoYuGIcfq_4rYfz11H44pnANOnN1B', 'webTips.parquet')
download_file('1HG6V24mn9y_0uJH-13HIWxpcFwwE59ws', 'odds.parquet')
download_file('1-3OHnFfuM7qgJuq329gFa22jACuPGIeU', 'dividends.parquet')
download_file('1tS8DsbCzeTUMj-DsB8A7bvM-XSCFa537', 'races_tdy.parquet')
download_file('19g1udGm83tmRNTr10v598jtRox-bOWxq', 'runners_tdy.parquet')
download_file('1fqLUYNF1nfaCsw2K95fi-bWj4Jg0qdDo', 'webTips_tdy.parquet')
download_file('1Cx_juo4BT97gAqFysRQZyu8si_kb-zaU', 'odds_tdy.parquet')
download_file('1m3rf0xZxKqIQejHYXWLkL1Dx7NDzNbZD',   'df_with_ratings.parquet')
download_file('1LG2GvIrv84popZCY9jKJ8YX0Yjq-NUGL',     'ratings_state.json')
download_file('1O_36ELAU98GPvOBKs-ltdB_Z6bqkjK78', 'ratings_last_date.txt')
download_file('10jQphIJOxNiOXp4CHIInQXLQ_aSyADDX', 'pt_model.pkl')
download_file('1Nix6vb-UsDSWAZQKsOoKjAZjuZFQo8rb', 'pt_scaler.pkl')
download_file('1XhLgKqCrr6u0sPgmGHeR9UOwbBUcGJo3', 'pt_features.pkl')

print("All files downloaded successfully!")
