from pydrive.auth import GoogleAuth,ServiceAccountCredentials
from pydrive.drive import GoogleDrive
from googleapiclient.discovery import build 
import os, glob

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key/system-backup-1-53687ddf7502.json"
google_login = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
google_login.credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
drive = GoogleDrive(google_login)





def create_cloud_bucket():
    pass
    #  drive = build('drive','v3',http=http_auth)

    #  response = drive.files().list().execute()


def upload_file():
    message = ""
    for doc in glob.glob("*"):
    #Uploads a file to the bucket.
        source_file_name = os.getcwd()+"/"+str(doc)
        print(source_file_name)

        with open(source_file_name,"r") as f:
            file_name = os.path.basename(f.name)

            file_drive = drive.CreateFile({'title': file_name })  
            file_drive.SetContentFile(source_file_name) 
            file_drive.Upload()
            if file_drive:
                message = message + "," + file_name
            else:
                message = "failed"
            file_drive = None
            

    return "The files: " + message + " has been uploaded"


def get_files():
    service = build('drive', 'v3', credentials=google_login.credentials) 
    resource = service.files()
    result = resource.list(pageSize=1000, fields="files(id, name)").execute() 
    return result