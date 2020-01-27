from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []

prediction_key = "ad273d97ad1d48fdb9683d313914d4b1"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "f748a99d-17e5-47a8-83f6-9ed503834ba7"
publish_iteration_name = "lalit123"

base_image_url = "C:/Users/Lalit Ak Radadiya/Desktop/RSU/test/123.jpg"


# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open(base_image_url, "rb") as image_contents:
    results = predictor.classify_image(
        Project_id, publish_iteration_name, image_contents.read())

# Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name)
        break
