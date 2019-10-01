import sys, time, wget, os

from settings.settings import Settings
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

class CustomVision():
    def __init__(self):
        self._settings = Settings()
        self._endpoint = self._settings.get_endpoint()
        self._sample_project_name = self._settings.get_project_name()
        self._publish_iteration_name = "Iteration1"
        self._prediction_resource_id = self._settings.get_prediction_resource_id()
        self._subscription_training_key = self._settings.get_subscription_training_key()
        self._subscription_prediction_key = self._settings.get_subscription_prediction_key()
        self._images_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self._trainer = CustomVisionTrainingClient(self._subscription_training_key, endpoint=self._endpoint)
        self._predictor = CustomVisionPredictionClient(self._subscription_prediction_key, endpoint=self._endpoint)

if __name__ == "__main__":
    cv = CustomVision()


