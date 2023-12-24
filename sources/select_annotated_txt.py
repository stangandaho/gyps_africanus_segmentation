from pathlib import Path
import shutil
from ultralytics.data.converter import convert_coco

## Root for coco format files
annot_train_dir = "./annotation/train"
annot_val_root = "./annotation/val"
## Create directories for split
split_dir = ["train", "val", "test"]
for dr in split_dir:
    Path("./dataset", "images", dr).mkdir(exist_ok=True, parents=True)
for dr in split_dir:
    Path("./dataset", "labels", dr).mkdir(exist_ok=True, parents=True)


## Convert coco format to .txt - Training label
if Path("./coco_converted").exists():
    shutil.rmtree(Path("./coco_converted"))

convert_coco(labels_dir = str(annot_val_root),  use_segments=True)

lbl_path = Path("./coco_converted/labels/default")
for lbl in lbl_path.iterdir():
    shutil.copy(lbl, Path("./dataset/labels/train", lbl.name))

## Populate images/train
train_lbl_dir = Path("./dataset/labels/train")
train_image_src = [x for x in Path("./image_src/train").iterdir()]

for tr in train_lbl_dir.iterdir():
     to_copy_name , to_copy_ext = tr.stem, tr.suffix
     for j in train_image_src:
          if to_copy_name in str(j):
               new_file = Path("./dataset/images/train", j.name)
               shutil.copy(j, new_file)


## Convert coco format to .txt - Val label
if Path("./coco_converted").exists():
    shutil.rmtree(Path("./coco_converted"))

convert_coco(labels_dir = str(annot_val_root),  use_segments=True)
## Copy txt file to appropriate folder
lbl_path = Path("./coco_converted/labels/default")
for lbl in lbl_path.iterdir():
    shutil.copy(lbl, Path("./dataset/labels/val", lbl.name))

## Populate images/train
val_lbl_dir = Path("./dataset/labels/val")
val_image_src = [x for x in Path("./image_src/val").iterdir()]

for tr in val_lbl_dir.iterdir():
     to_copy_name , to_copy_ext = tr.stem, tr.suffix
     for j in val_image_src:
          if to_copy_name in str(j):
               new_file = Path("./dataset/images/val", j.name)
               shutil.copy(j, new_file)

