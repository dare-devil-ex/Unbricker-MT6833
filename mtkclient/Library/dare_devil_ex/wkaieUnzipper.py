# Authour: @dare_devil_ex

import os
import tarfile
import shutil as shu
from time import sleep as t

class Wkaie:
    def worker(rom):
        print("=======================================")
        print("Extraction started 💀")
        print("=======================================")
        with tarfile.open(rom, 'r:gz') as tar:
            tar.extractall()        
        print("=======================================")
        print("Moving files ✅")
        print("=======================================")
        contents = [item for item in os.listdir(".") if os.path.isdir(item) and "images" in item.lower()]
        if contents:
            extracted_folder = contents[0] + "/images/"
            destination_path = "./input-images"
            for wk in os.listdir(extracted_folder):
                shu.move(f"{extracted_folder}{wk}", destination_path)
        else:
            print("No extracted folder found!")
        t(2)
        