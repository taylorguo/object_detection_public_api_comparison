
import requests, os, threading

csv_file = "Piano.csv"
folder_name = "piano"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

with open(csv_file, "r") as cf:
    lines =  cf.readlines()

# print(lines)
# i=1

def download():
    i=1
    for line in lines:
        new_line = line.strip()
        line_items = new_line.split(",")
        file_url = line_items[-1]
        file_name = line_items[0]

        if not os.path.exists("%s/%s.jpg"%(folder_name, file_name)):

            print("下载第{}幅图像:{}.jpg".format(i, file_name))
            print("连接网络...")
            img_file = requests.get(file_url)
            print("保存图像...")
            with open("%s/%s.jpg"%(folder_name, file_name), "wb") as img_f:
                img_f.write(img_file.content)
        
        i += 1
    
# down_thread = threading.Thread(target=download)
# down_thread.start()


def down(line, i):
    new_line = line.strip()
    line_items = new_line.split(",")
    file_url = line_items[-1]
    file_name = line_items[0]

    if not os.path.exists("%s/%s.jpg"%(folder_name, file_name)):

        print("下载第{}幅图像:{}.jpg".format(i, file_name))
        print("连接网络...")
        img_file = requests.get(file_url)
        print("保存图像...")
        with open("%s/%s.jpg"%(folder_name, file_name), "wb") as img_f:
            img_f.write(img_file.content)

import multiprocessing

i = 1
for line in lines:
    p = multiprocessing.Process(target=down, args=(line, i))
    p.start()
    p.join()
    i += 1
