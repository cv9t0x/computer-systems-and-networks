import requests, json, sys

def readFileText(url):
	return open(str(url), "r").read()

def writeFileText(url, data):
	with open(url, 'w') as output:
				output.write(data)

def fetchTranslatedText(data, lang):
	API_URL = "https://api.cognitive.microsofttranslator.com/translate"
	API_KEY = "9bf007a897f54e4a94203f8aa88cd2b1"
	region = "westeurope"

	headers = {
		'Ocp-Apim-Subscription-Key': API_KEY,
		'Ocp-Apim-Subscription-Region': region,
		'Content-type': 'application/json',
	}

	params = {
		'api-version': '3.0',
		'to': lang
	}

	try:
		response = requests.post(API_URL, params=params, headers=headers, json=data)
		return response.json()
	except Exception as e:
		return None

def main(lang, source, output = "output.txt"):
	try:
		text = readFileText(source)
	except Exception as e:
		print('Error, cannot read file')
		return

	data = [{
		'text': text
	}]
	response = fetchTranslatedText(data, lang)

	if(response):
		translatedText = response[0]['translations'][0]['text']

		try:
			writeFileText(output, translatedText)
		except Exception as e:
			print('Error, cannot write text to output')
			return

		print('Success')
	else:
		print('Error, could not get response from server (check language)')


if __name__ == "__main__":
	if(len(sys.argv) > 2 and len(sys.argv) < 5):
		if(len(sys.argv) == 4):
			main(sys.argv[1], sys.argv[2], sys.argv[3])
		else:
			main(sys.argv[1], sys.argv[2])
	else:
		print('Error, check input parameters (lang source.txt output.txt)')