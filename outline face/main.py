#from PIL import Image, ImageDraw

#with Image.open("img.jpg") as im:
#	draw = ImageDraw.Draw(im)
#	draw.line((100,200, 150, 300), fill=128, width=3)
#	im.save("1.jpg")
import requests, os, shutil, time
from PIL import Image, ImageDraw
from os import path


def fetchFaces(data):
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


def readImage(imagepath):
	with open(imagepath, 'rb') as im:
		return im.read()


def outlineFace(count, image, data, outputpath):
	for item in data:
		coordinate = item["faceRectangle"]
		top = coordinate["top"]
		left = coordinate["left"]
		width = coordinate["width"]
		height = coordinate["height"]

		draw = ImageDraw.Draw(image)
		draw.rectangle([(left - 30, top - 180), (width + left + 30, height + top + 30)], fill=None, outline="blue", width=2)
		image.save(outputpath + "/" + str(count) + ".jpg")


def cleanDir(dirpath):
	if(path.exists(dirpath)):
		shutil.rmtree(dirpath, ignore_errors=True)

	os.mkdir(dirpath)


def main():
	outputpath = "output"
	resourcepath = "resource"
	count = 0

	cleanDir(outputpath)

	for file in os.listdir(resourcepath):
		if(file.endswith(".jpg")):
			imagepath = resourcepath + '/' + file
			faces = fetchFaces(readImage(imagepath))

			if(faces):
				outlineFace(count, Image.open(imagepath), faces, outputpath)
				count += 1





if __name__ == "__main__":
	main()