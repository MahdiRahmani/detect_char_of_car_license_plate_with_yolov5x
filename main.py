import torch
import cv2 as cv


def detect(model, img_path, conf_th, char_id_dict):
    det = model(img_path)
    det = (det.pred[0]).tolist()
    plate_img = cv.imread(img_path)
    sorted_det = sorted(det, key=lambda x: (x[0]))
    plate_char = ''
    for k in sorted_det:
        conf = k[4]
        if conf > conf_th:
            plate_char += char_id_dict[str(int(k[5]))]
            x1, y1, x2, y2 = (int(k[0]), int(k[1]), int(k[2]), int(k[3]))

            label = char_id_dict[str(int(k[5]))]
            cv.rectangle(plate_img, (x1, y1), (x2, y2), (0, 255, 0), 1)
            labelSize = cv.getTextSize(label, cv.FONT_ITALIC, 0.5, 2)

            _x1 = x1
            _y1 = y1
            _x2 = _x1 + labelSize[0][0]
            _y2 = y1 - int(labelSize[0][1])
            cv.rectangle(plate_img, (_x1, _y1), (_x2, _y2), (0, 255, 0), cv.FILLED)
            cv.putText(plate_img, label, (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    return plate_char, sorted_det, plate_img


char_dict = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
             'الف': '10', 'ب': '11', 'پ': '12', 'ت': '13', 'ث': '14', 'ج': '15', 'چ': '16', 'ح': '17', 'خ': '18',
             'د': '19', 'ذ': '20', 'ر': '21', 'ز': '22', 'ژ': '23', 'س': '24', 'ش': '25', 'ص': '26', 'ض': '27',
             'ط': '28', 'ظ': '29', 'ع': '30', 'غ': '31', 'ف': '32', 'ق': '33', 'ک': '34', 'گ': '35', 'ل': '36',
             'م': '37', 'ن': '38', 'ه‍': '39', 'و': '40', 'ی': '41', 'ژ (معلولین و جانبازان)': '42'}

char_id_dict = {v: k for k, v in char_dict.items()}

model_path = r'yolov5-xl/weights/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

img_path = r'image_test_input/t (9).jpg'

plate_string, char_detected, out_img = detect(model, img_path, 0.6, char_id_dict)

cv.imwrite('image_test_output/out-{}.png'.format(img_path.split('.')[0].split('/')[-1]), out_img)
