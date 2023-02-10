from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

path_credentials = os.getenv("PATH_GOOGLE_CREDENTIALS", os.path.expanduser('~') + "/Documentos/credentials_conta_servico.json")

def upload_to_drive(file_path, file_name):
    credentials = service_account.Credentials.from_service_account_file(
        path_credentials, scopes=['https://www.googleapis.com/auth/drive.file'])

    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {'name': file_name, 'parents': ['ID_FOLDER_DRIVER_URL']}

    media = MediaFileUpload(file_path,
                            mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print(F'Arquivo {file_name} salvo com sucesso no drive com o id: {file.get("id")}')

upload_to_drive(os.path.expanduser('~') + "/git/detect_person/attach_file/teste_1.MOV", "teste_1.MOV")
