# Deep learning on White-backed Vulture (_Gyps africanus_)

## Why Deep Learning for this Species?
White-backed Vultures (WBV) are an ecologically important scavenger species, but their populations are threatened by habitat loss and human persecution. Monitoring their numbers and distribution is crucial for conservation efforts. Traditional methods like manual observation are time-consuming and expensive especially in large areas.

This project, my third MSc objective proposes using deep learning on images from camera traps and drones to automatically segment and identify WBV within the images. Deep learning can efficiently analyze large datasets of images, making it a promising tool for wildlife monitoring.

## Data Acquisition and Processing
Comprehensive image acquisition and preprocessing were essential to establish a robust dataset for training the deep learning model. We leveraged two primary sources: iNaturalist, a reliable wildlife database, and Google Search, using [rinat](https://github.com/ropensci/rinat) R package and [Download all Images](https://chromewebstore.google.com/detail/download-all-images/nnffbdeachhbpfapjklmpnmjcgamcdmm) Chrome plugin. Images were initially stored in separate folders for clarity, followed by rigorous quality control to remove any unsuitable images. The remaining 3,266 images were consolidated into a single folder, each assigned a unique identifier.

Strategic data splitting and meticulous annotation paved the way for effective model training and evaluation. The dataset was partitioned into a training set (60%) for model learning, a validation set (25%) for hyperparameter tuning and overfitting prevention, and a test set (15%) for unbiased performance assessment. Images in the training and validation sets were carefully annotated using CVAT, an open-source annotation tool. Annotations were exported in COCO format and subsequently converted to a text file compatible with the YOLO model's input requirements.
