import requests,sys
from bs4 import BeautifulSoup
print("\033[1mMax 100 videos\033[0m(if there is more, i'll calculate length of first 100 videos)\n\tyoutube.com/playlist?list=\033[93mID \033[0m\n")
id=input("Enter \033[93m\033[1mID\033[0m: ")
while("youtube.com/playlist?list=" in id):
    print("\n\n\033[93mDon't enter full URL, i just need ID of playlist!\033[0m\n")
    id=input("Enter \033[93m\033[1mID\033[0m: ")
url="https://youtube.com/playlist?list="+id
hours=minutes=seconds=0
try:
    go=requests.get(url)
except:
    print("\n\033[91mCouldn't connect. Check your connection\033[0m")
    sys.exit(0)
if(go.url=="https://www.youtube.com/oops"):
    print("\033[91mPlaylist not found")
    sys.exit(0)
soup=BeautifulSoup(go.text,'html.parser')
dv=soup.find_all('div',class_='timestamp')
print("Number of available videos:",len(dv))
for i in range(len(dv)):
    if(len(dv[i].text)>5):
        hours+=int(dv[i].text.split(':')[0])
        minutes+=int(dv[i].text.split(':')[1])
        seconds+=int(dv[i].text.split(':')[2])
    else:
        minutes+=int(dv[i].text.split(':')[0])
        seconds+=int(dv[i].text.split(':')[1])
print("\033[94m\033[1mFull length of the playlist:\033[0m",hours+int(minutes/60),"hours,",(minutes+int(seconds/60))%60,"minutes",seconds%60,"seconds\n")
