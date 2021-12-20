import requests, os
from PIL import Image


def openFile(path):
	with open(path, 'rb') as f:
		return f.read()


def getFacesFromImage(data):
	API_URL = "https://bki-face.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true"
	API_KEY = "01f0026ec4bc4880b6b8713dbd581e97"

	headers = {
		"Content-Type": "application/octet-stream",
		"Ocp-Apim-Subscription-Key": API_KEY
	}

	try:
		response = requests.post(API_URL, headers=headers, data=data)
		return response.json()
	except Exception as e:
		return None


def cropImage(image, data):
	outputpath = "faces/"
	count = 0

	for item in data:
		coordinate = item["faceRectangle"]
		coordinates = {
			top: int(coordinate["top"]),
			left: int(coordinate["left"]),
			width: int(coordinate["width"]) + int(coordinate["top"]),
			height: int(coordinate["height"]) + int(coordinate["left"])
		}

		croppedImage = image.crop(coordinates.left, coordinates.top, coordinates.width, coordinates.height)
		croppedImage.save(outputpath + str(++count) + ".jpg")


def main():
	imagename = "img.jpg"
	path = "./" + imagename

	data = openFile(path)
	response = getFacesFromImage(data)

	if(response):
		cropImage(Image.open(imagename), response)


if __name__ == "__main__":
	main()