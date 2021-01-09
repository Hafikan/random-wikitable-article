import requests
from bs4 import BeautifulSoup
import webbrowser 

while True:
    link = "https://tr.wikipedia.org/wiki/Special:Random"
    req = requests.get(link)
    soup = BeautifulSoup(req.content,"html.parser") 
    title = soup.title.text
    
    if req.status_code == 200:

        
        try:

            print("*********************\n",title,"\n*********************")
            sel=input("One more?[Y/N}\n Open This?[O]")
            sel = sel.lower()
            if sel == "y":
                pass

            elif sel == "o":
                print(title)
                webbrowser.open("https://tr.wikipedia.org/wiki/"+title)
                break

            elif sel == "n":
                print("Good Bye")
                break

            else:
                print("Try again, wrong choose!")
                break
        except:
            print("Unknown Error!")
            break

    else:
        print("Connection Failed!")
        break