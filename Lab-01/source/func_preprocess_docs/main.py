import logging, shutil
import os, datetime, requests
import azure.functions as func

from ..shared_code.storage import storage
from .preprocessing.preprocess import CognitiveServices
from ..shared_code.config.setting import Settings

def main(mytimer: func.TimerRequest):
    logging.info(f'Process finish succesfully')