from detect_objects import detect_labels_local_file
from detect_text import detect_text
from googlesearch import search
import webbrowser
def main():
	bucket='itemstodetect'
	photo='cokeregular.jpeg'
	#photo='abc.jpg'
	text=detect_text(photo,bucket)
	if text==None:
		labels=detect_labels_local_file(photo,bucket)
	try:
		for i in text:
			query = f"Amazon:{i}"
			for j in search(query, tld="co.in",num=1,stop=1,pause=1):
				print(i)
				print(j)
				webbrowser.open_new(j)
	except TypeError:
		try:
			for i in labels:
				query = f"Amazon:{i[0]}"
				for j in search(query, tld="co.in",num=1,stop=1,pause=1):
					print(i[0])
					print(j)
					webbrowser.open_new(j)
		except TypeError:
			print('Sorry the image could not be accurately analyzed.')
if __name__ == "__main__":
	main()
