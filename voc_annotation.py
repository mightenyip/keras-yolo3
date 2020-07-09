import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2020', 'train')] #, ('2020', 'val'), ('2020', 'test')]

# classes = ["neuron","aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes = ["neuron"]

def convert_annotation(image_id, list_file):
    in_file = open('C:/Users/might/Dropbox (GaTech)/Shared folders/AND_Project/slice_images_raw/annotation_data/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('C:/Users/might/Documents/GitHub/AND_Project/keras-yolo3/model_data/train.txt').read().strip().split()
    print(image_ids)
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('C:/Users/might/Desktop/Neurons_raw/training_data/neuron/%s.tiff'%(image_id))
        # print(list_file)
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

