from pathlib import Path
import shutil

## Select non-dodgy images
spc_name = "Gyps africanus"
img_src = ["from_google", "from_inaturalist"]

all_img = [] # to store images path
for sub_img_src in img_src:
    img_paths = Path.cwd()/sub_img_src
    for img in Path.iterdir(img_paths):
        img_st = Path.stat(img)
        img_size = img_st.st_size/1000
        img_suffix = img.suffix
        
        if img_size >= 5 and img_suffix in [".jpeg", ".jpg", ".png"]:
            all_img.append(img)

len(all_img)

## rename and sotre image in data folder
## Create the folder
Path(Path.cwd()/"data").mkdir(exist_ok=True)
## Move file into data folder
img_number = 0
for img_file in all_img:
    img_number += 1
    prt_folder = img_file.parent
    suffixe = img_file.suffix
    new_name = Path.cwd()/ "data"/ \
        f"{spc_name} {str(img_number).zfill( len(str(len(all_img))) )}{suffixe}"
    shutil.copy(img_file, new_name)
