import logging, requests, json, os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from io import BytesIO
from matplotlib.patches import Rectangle
from ...shared_code.storage.storage import BlobStorageService
from ...shared_code.config.setting import Settings

class CognitiveServices():
    def __init__(self):
        self._settings = Settings()
        self._storage = BlobStorageService(self._settings.get_storage_account(), self._settings.get_storage_key())
        self._subscription_key = self._settings.get_cognitive_key()
        self._vision_base_url = self._settings.get_computer_vision_url()
        self._text_analytics_url = self._settings.get_text_analytics_url()