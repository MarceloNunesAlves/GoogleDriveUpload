from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os

path_credentials = os.getenv("PATH_GOOGLE_CREDENTIALS", os.path.expanduser('~') + "/Documentos/credentials.json")

def upload_to_drive(file_path, file_name):
    flow = InstalledAppFlow.from_client_secrets_file(path_credentials, scopes=['https://www.googleapis.com/auth/drive.file'])

    credentials = flow.run_console()

    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path,
                            mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(F'Arquivo {file_name} salvo com sucesso no drive com o id: {file.get("id")}')

upload_to_drive(os.path.expanduser('~') + "/arquivo.txt", "nome_do_arquivo.txt")
