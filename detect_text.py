import boto3

def detect_text(photo, bucket):
    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})                       
    textDetections=response['TextDetections']
    items = []
    print(textDetections,'textDetections')
    for text in textDetections:
            if (text['Type']=='LINE') and (text['Confidence']>=85): items.append(text['DetectedText'])
    numdetected = len(textDetections)
    return items

def main():
    bucket='itemstodetect'
    photo='cokeregular.jpeg'
    #photo='abc.jpg'
    text=detect_text(photo,bucket)
    print(text)

if __name__ == "__main__":
    main()