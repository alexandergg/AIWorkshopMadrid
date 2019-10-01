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
    
    def extractWordsBoudings(self, line_infos):
        word_infos = []
        for line in line_infos:
            for word_metadata in line:
                for word_info in word_metadata["words"]:
                    word_infos.append(word_info)
        return word_infos
    
    def extractTextFromOCR(self, line_infos):
        text = []
        for line in line_infos:
            for word_metadata in line:
                for i in range(len(word_metadata["words"])):
                    text.append(word_metadata["words"][i]['text'])
        return text
    
    def showResultOnImage(self, word_infos, blob_url, filename):
        name = os.path.basename(filename)
        plt.figure(figsize=(50,50))
        b = self._storage.download_blob_bytes(self._settings.get_storage_documents(), filename)
        image = Image.open(BytesIO(b.content))
        ax = plt.imshow(image, alpha=0.5)
        for word in word_infos:
            bbox = [int(num) for num in word["boundingBox"].split(",")]
            text = word["text"]
            origin = (bbox[0], bbox[1])
            patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
            ax.axes.add_patch(patch)
            plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
        _ = plt.axis("off")
        plt.savefig('{}'.format(name))
        self._storage.upload_file(container_name=self._settings.get_storage_ocr(),
                                filename=name,
                                local_file='./{}'.format(name),
                                delete_local_file=True)