import os

path = "./images/"
x = ['boot.img', 'dpm.img', 'dtbo.img', 'gz.img', 'lk.img', 'logo.img', 'mcupm.img', 'md1img.img', 'pi_img.img', 'scp.img', 'spmfw.img', 'sspm.img', 'tee.img', 'vbmeta.img', 'vbmeta_system.img', 'vbmeta_vendor.img']

for filename in x:
    file_found = False
    
    for dirpath, dirnames, filenames in os.walk(path):
        if filename in filenames:
            file_found = True
            break
        
    if file_found:
        old_file_path = os.path.join(path, filename)
        new_file_name = filename[:filename.rfind(".")] + ".bin"
        new_file_path = os.path.join(path, new_file_name)
        os.rename(old_file_path, new_file_path)
        print("=======================================")
        print(f"Renamed {filename} to {new_file_name}")
        print("=======================================")
        
    else:
        print(f"{filename} not found")