import cv2, os

classes = {"microphone": "0", "piano": "1", "guitar": "2"}

csv_file = "Microphone.csv"
folder_name = "microphone"
# folder_name = "test"

with open(csv_file, "r") as cf:
    lines =  cf.readlines()

# print(lines)

annotation = {}


for line in lines:

    boxes = []

    new_line = line.strip()
    line_items = new_line.split(",")
    file_url = line_items[-1]
    file_name = line_items[0]

    file_path = "%s/%s.jpg"%(folder_name, file_name)

    if os.path.exists(file_path):
        # print(file_path)
        try:
            # piexif.remove(file_path)
            image = cv2.imread(file_path)
            size = image.shape
        except AttributeError:
            if not os.path.exists("error_microphone"):
                os.mkdir("error_microphone")
            os.system("mv %s error_microphone"%file_path)
            continue
        
        H = size[0]
        W = size[1]

        # print(H,W, line_items)

        xmin_value = line_items[2]
        xmax_value = line_items[3]
        ymin_value = line_items[4]
        ymax_value = line_items[5]

        xmin = int(float(xmin_value) * W)
        xmax = int(float(xmax_value) * W)
        ymin = int(float(ymin_value) * H)
        ymax = int(float(ymax_value) * H)

        box_item = str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+","+classes[folder_name]
        # box_item = str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+","+classes["microphone"]


        # print(file_name+".jpg"+" "+box_item)
        boxes.append(box_item)

        if file_name in annotation.keys():
            annotation[file_name].append(box_item)
        else:
            annotation[file_name] = boxes


with open(folder_name+".txt", "a") as txt_file:

    for img in annotation.keys():
        boxes_str = ""
        # print(annotation[img])
        for box in annotation[img]:
            boxes_str += " " + box
        full_line = "\\" + img + ".jpg" + boxes_str
        print(full_line)
        txt_file.write(full_line+"\n")

