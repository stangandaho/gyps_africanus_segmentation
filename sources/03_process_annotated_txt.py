from pathlib import Path
import shutil
from ultralytics.data.converter import convert_coco

## Root to coco format files
annot_train_dir = "./annotation/train"
annot_val_dir = "./annotation/val"

## Create directories that points to split parts
split_dir = ["train", "val", "test"]
for dr in split_dir:
    Path("./dataset", "images", dr).mkdir(exist_ok=True, parents=True)
    Path("./dataset", "labels", dr).mkdir(exist_ok=True, parents=True)

## Function to onverte coco format to text
def cf_to_text(coco_dir: str, dest_dir:str):
    """Convert coco format to text file

    Args:
        coco_dir (str): the directory that contain coco format
        dest_dir (str): the destination directory for text file
    """

    if Path("./coco_converted").exists():
        shutil.rmtree(Path("./coco_converted"))
    convert_coco(labels_dir = str(coco_dir),  use_segments=True)

    lbl_path = Path("./coco_converted/labels/default")
    for lbl in lbl_path.iterdir():
        shutil.copy(lbl, Path(dest_dir, lbl.name))

## Function to pupulate images/train; images/val
def populate_imfolder(image_src:str, label_dir:str, dest_dir:str):
    """Populate the train or validation directory basing on label files.

    Args:
        image_src (str): the directory where to copy images from
        label_dir (str): the directory that contains label file (.txt), ideally the output of `cf_to_text`
        dest_dir (str): the destination directory for image relatives to each text file
    """

    train_lbl_dir = Path(label_dir)
    train_image_dir = [x for x in Path(image_src).iterdir()]

    for tr in train_lbl_dir.iterdir():
        to_copy_name = tr.stem
        for j in train_image_dir:
            if to_copy_name in str(j):
                new_file = Path(dest_dir, j.name)
                shutil.copy(j, new_file)
     

# Convert coco format to .txt --> Training label
cf_to_text(coco_dir=annot_train_dir, dest_dir="./dataset/labels/train")
# Convert coco format to .txt --> Validation label
cf_to_text(coco_dir=annot_val_dir, dest_dir="./dataset/labels/val")


## Populate images/train folder basing on label files
populate_imfolder(image_src = "./image_src/train", label_dir="./dataset/labels/train", \
                dest_dir = "./dataset/images/train")
## Populate images/val folder basing on label files
populate_imfolder(image_src = "./image_src/val", label_dir="./dataset/labels/val", \
                dest_dir = "./dataset/images/val")