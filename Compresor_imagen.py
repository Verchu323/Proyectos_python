from PIL import Image # python -m pip install Pillow

import os

downLoadsFolder = "/Users/El Fresno/Downloads/" #Esta es la sintaxis para entrar a la ruta que deseo
picturesFolder = "/Users/El Fresno/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downLoadsFolder):
        name, extension = os.path.splitext(downLoadsFolder + filename)
        
        if extension in [".jpg", ".jpeg", ".png"]:
            os.rename(downLoadsFolder + filename, picturesFolder + filename)
            print(name + ": " + extension)
            
        if extension in [".mp3"]:
            musicFolder = "/Users/El Fresno/Music/"
            os.rename(downLoadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)
        
        if extension in [".mp4"]:
            videoFolder = "/Users/El Fresno/Videos/"
            os.rename(downLoadsFolder + filename, videoFolder + filename)
            print(name + ": " + extension)
            
        if extension in [".pdf"]:
            pdfFolder = "/Users/El Fresno/Documents/"
            os.rename(downLoadsFolder + filename, pdfFolder + filename)
            print(name + ": " + extension)
        