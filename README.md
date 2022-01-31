# Detect Char of Car License Plate with Yolo-v5x
Using Yolo-v5x trained model you can detect characters of car license plate.

## Confusion Matrix
<img src="https://github.com/MahdiRahmani/detect_char_of_car_license_plate_with_yolov5x/blob/master/yolov5-xl/confusion_matrix.png" width="800"/>

## Result
<img src="https://github.com/MahdiRahmani/detect_char_of_car_license_plate_with_yolov5x/blob/master/yolov5-xl/val_batch0_pred.jpg" width="800"/>
<img src="https://github.com/MahdiRahmani/detect_char_of_car_license_plate_with_yolov5x/blob/master/yolov5-xl/val_batch1_pred.jpg" width="800"/>
<img src="https://github.com/MahdiRahmani/detect_char_of_car_license_plate_with_yolov5x/blob/master/yolov5-xl/val_batch2_pred.jpg" width="800"/>

## Run project
This code deploy with 'python==3.9'
1. Within the project directory, create a Python virtual environment by typing:
- `virtualenv myprojectenv`
2. For install our project’s Python requirements, we need to activate the virtual environment. You can do that by typing:
- Linux: `source myprojectenv/bin/activate` or Windows: `myprojectenv/Scripts/activate`
- `pip install -r req.txt`
3. Download pretraind model from <a href="https://drive.google.com/u/0/uc?id=1qmRyXvcNS_PGhomRK1tT_nslnBmM5OHZ&export=download" target="_blank">LINK</a> and set address of this model to main.py:
- `model_path = r'.../best.pt'`
4. Finally, you can run 'main.py'
###### MAHDI RAHMANI
