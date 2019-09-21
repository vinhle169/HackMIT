# HackMIT
First AWS project, there is no UI or direct interaction with it since there wasn't enough time to implement it in time as this was a solo project for a hackathon.

## Item Shopper
<p>Takes an image that is stored in Amazon Web Service R3 Storage and scans that image looking for text or labels and then searches for it on Amazon automatically.</p>

### main.py
<p>The main code that imports from <strong>detect_text</strong> and <strong>detect_objects</strong>. Takes an image by the name it is stored in R3 Storage, and depending on if there are multiple words on the image or if there are multiple words that combine to make the brand name it will organize the data that needs to be searched accordingly. </p>

### detect_text.py

<p> Runs Amazon 'Rekognition' Text detection on the image, and depending on the confidence of the image it returns the text it detects. For the purpose of the project the minimum confidence required is 85%.</p>

### detect_object.py
<p> Runs Amazon 'Rekognition' Label detection on the image(only if no text is detected). Again will only return labels with >=85% confidence, and will search the labels if text isn't found. </p>
