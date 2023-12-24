from pathlib import Path
import random as rd

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
    Path.rename(img_file, new_name)

## Split data into train, val and test
split_folder = ["train", "val", "test"]
for folder in split_folder:
    spl_fld = Path(Path.cwd(), "data", folder)
    spl_fld.mkdir(exist_ok=True)

## Populate split folder from image in data randomly
# train ~ 60% = 2000 images; val ~ 30% = 800; test = 489
correct_img = [file for file in (Path.cwd()/"data").iterdir() if file.is_file()]

img_index = list(range(1, len(correct_img) + 1))

train_img = correct_img[:2000]
val_img = correct_img[2000:2800]
test_img = correct_img[2800:]

for file in train_img:
    Path.rename(file, Path(file.parent, "train", file.name))
for file in val_img:
    Path.rename(file, Path(file.parent, "val", file.name))
for file in test_img:
    Path.rename(file, Path(file.parent, "test", file.name))
