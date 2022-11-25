import filetype, os
from pathlib import Path

keep_mpegs = False #Change to True if you want to keep Mpegs (Default: False)

list = os.listdir("./files/")

png= []
jpeg= []
gif= []
webp= []
mp4= []
webm= []
mpeg= []
mp3= []

for x in list:
    path = "./files/filename"
    file = path.replace("filename", x)
    kind = filetype.guess(file)
    if kind is None:
        os.remove(file)
        continue
    
    if kind.mime == "image/png":
        png.append(file)
        
    if kind.mime == "image/jpeg":
        jpeg.append(file)
    
    if kind.mime == "image/gif":
        gif.append(file)
        
    if kind.mime == "image/webp":
        webp.append(file)
    
    if kind.mime == "video/mp4":
        mp4.append(file)
        
    if kind.mime == "video/webm":
        webm.append(file)
     
    if kind.mime == "audio/mpeg":
        if keep_mpegs == True:   
            mpeg.append(file)
        else:
            os.remove(file)
                
    if kind.mime == "audio/mp3":
        mp3.append(file)
    
    if kind.mime == "application/font-woff":
        os.remove(file)
        continue
        
print("Found File Types Converting...")

for x in png:
    p = Path(x)
    p.rename(p.with_suffix('.png'))
    
for x in jpeg:
    p = Path(x)
    p.rename(p.with_suffix('.jpg'))
    
for x in gif:
    p = Path(x)
    p.rename(p.with_suffix('.gif'))

for x in webp:
    p = Path(x)
    p.rename(p.with_suffix('.webp'))

for x in mp4:
    p = Path(x)
    p.rename(p.with_suffix('.mp4'))

for x in webm:
    p = Path(x)
    p.rename(p.with_suffix('.webm'))

for x in mpeg:
    p = Path(x)
    p.rename(p.with_suffix('.mpeg'))
    
for x in mp3:
    p = Path(x)
    p.rename(p.with_suffix('.mp3'))
