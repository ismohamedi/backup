import logging
import time
import os
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi_utils.tasks import repeat_every

from tasks import upload_file, get_files, download_file, delete_file
base_dir = os.getcwd()

if os.getcwd() != 'root/CORES/backup':
     os.chdir("../backup")


logger = logging.getLogger(__name__)
app = FastAPI(title="ShuleSoft backup")


@app.get('/files', tags=['List of File from  Drive'])
async def get_file():
    return get_files()

@app.get('/delete-file', tags=['Delete file from Drive'])
async def delete_drive_file(file_id):
    return delete_file(file_id)

@app.get('/download-files', tags=['Download file from Drive'])
async def download_files(file_id):
    if os.getcwd() != '/root/CORES/backup/docs' and  os.getcwd() != '/root/CORES/backup':
        os.chdir("../docs")
    elif os.getcwd() == base_dir:
        os.chdir("docs")

    return download_file(file_id=file_id)

@app.post("/buckup", tags=['Upload file to Drive (Backup)'])
async def backup():
     if os.getcwd() != '/root/CORES/backup/docs' and  os.getcwd() != '/root/CORES/backup':
        os.chdir("../docs")
     elif os.getcwd() == base_dir:
        os.chdir("docs")
     return upload_file()



@app.on_event("startup")
@repeat_every(seconds=12000, logger=logger, wait_first=False)
def periodic():
    print(os.getcwd())
    if os.getcwd() != '/root/CORES/backup/docs':
        os.chdir("docs")
    upload_file()
   