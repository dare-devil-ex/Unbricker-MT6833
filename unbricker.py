# Authour: dare_devil_ex

import os
from time import sleep as t
import subprocess
from mtkclient.Library.dare_devil_ex.downloader import downloader as dl
from mtkclient.Library.dare_devil_ex.wkaieUnzipper import Wkaie as FHandler

path = "./input-images"
requirements = ['boot.img', 'dpm.img', 'dtbo.img', 'gz.img', 'lk.img', 'logo.img', 'mcupm.img', 'md1img.img', 'pi_img.img', 'scp.img', 'spmfw.img', 'sspm.img', 'tee.img', 'vbmeta.img', 'vbmeta_system.img', 'vbmeta_vendor.img']



print("""Pick your board
1. Evergo
2. Evergreen
      """)

def romCheck(userIn):
    go = False; green = False
    for file in os.listdir("./"):
        if file.endswith(".tgz"):
            if file.startswith("evergo") and userIn == 1:
                go = True
                break
            elif file.startswith("evergreen") and userIn == 2:
                green = True
                break
    if go:
        t(0.1)
        print("=======================================")
        print("[", file, "] ✅")
        print("=======================================")
        FHandler.worker(file)
        
    elif green:
        t(0.1)
        print("=======================================")
        print("[", file, "] ✅")
        print("=======================================")
        os.rename(file, "evergreen.tgz")
    else:
        t(0.1)
        print("=======================================")
        print("[ ROM ISN'T FOUND ] ❌")
        print("=======================================")
        downloaderRom(userIn)

def wkaie(hw):
    os.system("cls")
    t(0.5)
    print("=======================================")
    print("Checking begins ❄️    Dare Devil Ex 🦋")
    print("=======================================")
    for filename in requirements:
        bin_filename = filename.replace(".bin", ".img")
        bin_path = os.path.join(path, bin_filename)
        img_path = os.path.join(path, filename)

        if os.path.exists(bin_path):
            print(f"\033[00;32m{bin_filename}\033[00;00m already exists ✅. Skipping {filename}.")
            t(0.1)
            continue
            
        file_found = False
        for _, _, filenames in os.walk(path):
            if filename in filenames:
                file_found = True
                break
        
        if file_found:
            base_name = filename.replace(".img", "")
            new_filename = f"{base_name}_a"
            command = [
                "python3", "mtk.py", "w", new_filename, filename,
                "--preloader", f"./input-images/preloader_{hw}.bin"
            ]

            try:
                subprocess.run(command, check=True)
                t(0.1)
            except subprocess.CalledProcessError:
                print(f"❌ Error running command for \033[00;31m{filename}\033[00;00m")
                t(0.1)
                continue
            except KeyboardInterrupt:
                print("⚠️ Program terminated.")
                t(0.1)
                break
            
        if file_found:
            base_name = filename.replace(".img", "")
            new_filename = f"{base_name}_a"
            command = [
                "python3", "mtk.py", "w", new_filename, filename,
                "--preloader", f"./input-images/preloader_{hw}.bin"
            ]

            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError:
                print(f"❌ Error running command for {filename}")
                continue
            except KeyboardInterrupt:
                print("⚠️ Program terminated.")
                break
            os.rename(img_path, bin_path)
            print("=======================================")
            print(f"{filename} ✅ renamed to {bin_filename}")
            print("=======================================")
        
        else:
            if os.path.exists(bin_path):
                print(f"{filename} ❌ missing, but {bin_filename} ✅ exists. Skipping.")
                t(0.1)
                continue
            print(f"{filename} ❌\nWe need this \033[00;31m{filename}\033[00;00m file to continue the process")
            t(0.1)
            break
            
            
        
def downloaderRom(wk):
    inp = str(input("You wanna download the rom? Y / N: "))
    if inp.lower() == "y":
        dl.wkaiedl(wk)
    else:
        pass

    
userInput = int(input("Enter the choice: "))

if userInput == 1:
    romCheck(1)
    wkaie("evergo")
elif userInput == 2:
    romCheck(2)
    wkaie("evergreen")
    
else:
    print("Invaild input")