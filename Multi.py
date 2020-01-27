from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import glob
files = []
data = []
files = ['data.json']


prediction_key = "b07c005ad5ad46ec937dcdd08486ba58"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "253ff62d-4245-486a-b41e-921e94379e3b"
publish_iteration_name = "kesha123"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

for file in glob.glob("C:/Users/Lalit Ak Radadiya/Desktop/Data/test/*"):
        base_image_url = file
        with open(base_image_url, "rb") as image_contents:
            results = predictor.classify_image(
                Project_id, publish_iteration_name, image_contents.read())

        # Display the results.
            for prediction in results.predictions:
                print("\t" + prediction.tag_name)
                t = prediction.tag_name
                data.append({
                    'name': t,
                    'price': "20rs"
                })
                break

        # end with
        with open('data.json', 'w+') as outfile:
          json.dump(data, outfile)

        # end with
        files = ['data.json']
