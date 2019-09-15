import boto3
import os
from googlesearch import search

def detect_labels_local_file(photo):
	client = boto3.client('rekognition')
	items=[]
	with open(photo, 'rb') as image:
		response = client.detect_labels(Image={'Bytes': image.read()})
	for label in response['Labels']:
		#items=items.append((label['Name'],label['Confidence']))
		items.append(label['Name'])
	print(items,'items')
	return (len(response['Labels']),items)
def main():
	photo = 'thinking.png'
	photo = "C:\\Users\\Vinh Le\\Pictures\\cat.jpg"
	detected_labels =detect_labels_local_file(photo)
	label_count = detected_labels[0]
	for i in detected_labels[1]:
		query = f"Amazon:{i}"
		for j in search(query, tld="co.in",num=1,stop=1,pause=1):
			print(j)
	print("Labels detected: " + str(label_count))
if __name__ == "__main__":
	main()
