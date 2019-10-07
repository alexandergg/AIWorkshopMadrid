import logging, shutil
import os, datetime, requests
import azure.functions as func

from ..shared_code.storage import storage
from .preprocessing.preprocess import CognitiveServices
from ..shared_code.config.setting import Settings

def main(mytimer: func.TimerRequest):
    setttings = Settings()
    cs = CognitiveServices()

    st = storage.BlobStorageService(setttings.get_storage_account(), setttings.get_storage_key())
    utc_timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    try:
        docs = st.download_blobs(setttings.get_storage_documents())
        list(map(lambda doc: cs.checkDatetime(utc_timestamp, doc.properties.last_modified, doc), docs))
    except Exception as e:
        error = str(e)
        logging.info(f'{e}')
    logging.info(f'Process finish succesfully')