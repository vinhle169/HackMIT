from detect_objects import detect_labels_local_file
from detect_text import detect_text
from googlesearch import search
import webbrowser
def main():
	bucket='itemstodetect'
	photo='cokeregular.jpeg'
	#photo='abc.jpg'
	text=detect_text(photo,bucket)
	manywords = False
	combinewords = 1
	print(text)
	if text==None or len(text)<1:
		labels=detect_labels_local_file(photo,bucket)
		try:
			print('hereeeee')
			print(labels)
			for i in labels:
				query = f"Amazon:{i[0]}"
				for j in search(query, tld="co.in",num=1,stop=1,pause=1):
					if j[0:22]!='https://www.amazon.com':
						continue
					print(i[0])
					print(j)
					webbrowser.open_new(j)
		except:
			print('oopsie doopsie')
	else:
		try:
			if manywords:
				print('nani')
				text = "Amazon:"+' '.join(text[0:combinewords])
				for j in search(text, tld="co.in",num=1,stop=1,pause=1):
						if j[0:22]!='https://www.amazon.com':
							continue
						print(j)
						#webbrowser.open_new(j)
			else:
				print('nuni')
				for i in text:
					query = f"Amazon:{i}"
					for j in search(query, tld="co.in",num=1,stop=1,pause=1):
						if j[0:22]!='https://www.amazon.com':
							continue
						print(i)
						print(j)
						webbrowser.open_new(j)
		except:
			print('ooooopsie doooooopsie')
if __name__ == "__main__":
	main()
####doesnt work when there are way too many words 
