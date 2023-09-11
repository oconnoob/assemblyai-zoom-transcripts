import os

from dotenv import load_dotenv
import assemblyai as aai

from utils.zoom import ZoomClient

load_dotenv()

ZOOM_ACCOUNT_ID = os.environ.get('ZOOM_ACCOUNT_ID')
ZOOM_CLIENT_ID = os.environ.get('ZOOM_CLIENT_ID')
ZOOM_CLIENT_SECRET = os.environ.get('ZOOM_CLIENT_SECRET')
aai.settings.api_key = os.environ.get('ASSEMBLYAI_API_KEY')

transcriber = aai.Transcriber()

a = ZoomClient(account_id=ZOOM_ACCOUNT_ID, client_id=ZOOM_CLIENT_ID, client_secret=ZOOM_CLIENT_SECRET)

recs = a.get_recordings()
if recs['meetings']:    
    rec_id = recs['meetings'][0]['id']
    my_url = a.get_download_url(rec_id)
    transcript = transcriber.transcribe(my_url)
    print(transcript.text)
    with open('transcript.txt', 'w') as f:
        f.write(transcript.text)
else:
    print('No meetings to transcribe.')