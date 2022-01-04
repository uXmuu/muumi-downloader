import os
os.system("yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -f 18  https://youtube.com/playlist\?list\=PLrYFoqKfK4xA2fB_9neISqA26IlykR655")
os.system("sh deskissä.sh")
for i in os.popen("ls").read().split("\n"):
    if "[" in i:
        a=i[:-18]+".mp4"
        os.system("mv "+'"'+i+'"' +" "+'"'+a+'"')
        if "mp4" in i[:-4]:
            a=i[:-21]
            os.system("mv "+'"'+i+'"' +" "+'"'+a+'"')

    if "linkki" in i.lower():
        os.remove(i)



for i in os.popen("ls").read().split("\n"):
    a = i.replace("🇫","")
    a = a.replace("Muumilaakson tarinoita jakso ","")
    os.system("mv "+'"'+i+'"' +" "+'"'+a+'"')
