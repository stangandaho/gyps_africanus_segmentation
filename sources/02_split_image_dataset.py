from pathlib import Path
import shutil

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
    shutil.copy(file, Path(file.parent, "train", file.name))
for file in val_img:
    shutil.copy(file, Path(file.parent, "val", file.name))
for file in test_img:
    shutil.copy(file, Path(file.parent, "test", file.name))
