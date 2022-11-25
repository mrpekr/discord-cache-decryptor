import filetype, os, getpass
from pathlib import Path
import shutil
import time, sys

keep_mpegs = False #Change to True if you want to keep Mpegs (Default: False)
auto_copy = True #Changes if cache files will be copied from default path or custom (Default: True)

png= []
jpeg= []
gif= []
webp= []
mp4= []
webm= []
mpeg= []
mp3= []

print("Welcome to Discord Cache Decryptor")

if auto_copy == True:
    loc = r'C:\Users\mrpek\AppData\Roaming\discord\Cache'
else:   
    input = input("Please Enter the Full Path to your Discord Cache Folder: ")
    loc = input.join(" %(getpass.getuser())")


print("Folder Found Making Copy for Decrypting...")
sys.stdout.flush()

if os.path.exists("decrypted"):
    shutil.rmtree("decrypted")

floc = os.getcwd() + "\decrypted"

src=r"C:\Users\%s\AppData\Roaming\discord\Cache" %(getpass.getuser())

def copyFile(src, floc):
    try:
        shutil.copytree(src, floc)
    # eg. src and dest are the same file
    except shutil.Error as e:
        return
    # eg. source or destination doesn't exist
    except IOError as e:
        return

copyFile(src, floc)

list = os.listdir("decrypted")

print("Files Copyed Searching for File Types...")
sys.stdout.flush()

for x in list:
    path = "./decrypted/filename"
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
sys.stdout.flush()

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

print("Done! Cache Files Decrypted! you can find them in: " + os.getcwd() + "\decrypted")