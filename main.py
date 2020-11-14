import logging
import time
import os
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi_utils.tasks import repeat_every

from google_api import upload_file, get_files


logger = logging.getLogger(__name__)
app = FastAPI(title="ShuleSoft backup")

@app.post("/bucket")
async def create_bucket():
    return True

@app.get('/files')
async def get_file():
    return get_files()

@app.post("/buckup")
async def backup():
    return upload_file()


counter = 0
@app.on_event("startup")
@repeat_every(seconds=12000, logger=logger, wait_first=False)
def periodic():
    print(os.getcwd())
    if os.getcwd() != '/root/CORES/backup/docs':
        os.chdir("docs")
    upload_file()
   