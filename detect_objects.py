import boto3
import os
from googlesearch import search
import webbrowser

def detect_labels_local_file(photo,bucket=None):
	client = boto3.client('rekognition')
	items=[]
	#with open(photo, 'rb') as image: ##if im importing from 
	#	response = client.detect_labels(Image={'Bytes': image.read()},MaxLabels=3,MinConfidence=90)
	response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
	MaxLabels=3,MinConfidence=85)
	for label in response['Labels']:
		items.append([label['Name'],label['Confidence']])
	numlabels = len(response['Labels'])
	return items
def main():
	bucket='itemstodetect'
	photo='sushiplushie.jpg'
	detected_labels =detect_labels_local_file(photo,bucket)
	#label_count = detected_labels[0]
	for i in detected_labels:
		query = f"Amazon:{i[0]}"
		for j in search(query, tld="co.in",num=1,stop=1,pause=1):
			print(j)
			webbrowser.open_new(j)
if __name__ == "__main__":
	main()
### currently vague responses as labels which is why we are using text as well