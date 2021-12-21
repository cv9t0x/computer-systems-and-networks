import requests, os, shutil
from PIL import Image


def openFile(path):
	with open(path, 'rb') as f:
		return f.read()


def fetchFacesCoordinates(data):
	API_URL = "https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true"
	API_KEY = "01f0026ec4bc4880b6b8713dbd581e97"

	headers = {
		"Content-Type": "application/octet-stream",
		"Ocp-Apim-Subscription-Key": API_KEY,
	}

	try:
		response = requests.post(API_URL, headers=headers, data=data)
		return response.json()
	except Exception as e:
		return None


def cropImage(image, data):
	outputpath = "./faces"
	cleanDir(outputpath)

	count = 0
	
	for item in data:
		coordinate = item["faceRectangle"]
		top = coordinate["top"]
		left = coordinate["left"]
		width = coordinate["width"]
		height = coordinate["height"]

		croppedImage = image.crop((left, top, width + left, height + top))
		croppedImage.save(outputpath + "/" + str(count) + ".jpg")
		count += 1


def cleanDir(path):
	shutil.rmtree(path, ignore_errors=True)
	os.mkdir(path)

def main():
	imagepath = "img.jpg"
	response = fetchFacesCoordinates(openFile(imagepath))

	print(response)

	if(response):
		cropImage(Image.open(imagepath), response)


if __name__ == "__main__":
	main()