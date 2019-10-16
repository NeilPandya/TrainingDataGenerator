#https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
#https://docs.python.org/2/library/xml.etree.elementtree.html#treebuilder-objects

import cv2
import random
import xml.etree.ElementTree as ET
import os

NumberOfImages = 100

def DrawLesion(x,y,radius,lesion):

    if lesion == "1":
        color = (0,0,255)
        name = string(blue)
    elif lesion == "2":
        color = (0,255,0)
        name = string(green)
    elif lesion == "3":
        color = (255,0,0)
        name = string(red)
    elif lesion == "4":
        color = (122,122,122)
        name = string(grey)

    #Draw circle
    center=(x,y)
    cv2.circle(im, center, radius, color,-1)

    # Draw rectangle
    top_left= (x-radius, y-radius)
    bottom_right= (x+radius, y+radius)
    thickness=1
    cv2.rectangle(im, top_left, bottom_right, (255,0,0), thickness)



for Image_Number in range(1,NumberOfImages+1):
    im = cv2.imread('Image_Example.jpg')
    y_Max, x_Max, channels = im.shape
    #print('x_Max =',x_Max)
    #print('y_Max =',y_Max)

    output_filename_xml = 'Output_Annotations/' + str(Image_Number) + '.xml'
    output_filename_image = 'Output_Images/' + str(Image_Number) + '.jpg'

    NumberOfLesions = random.randint(1,10)
    print('Image Number: ',Image_Number)
    print('Number of Lesions: ',NumberOfLesions)

    annotation = ET.Element('annotation')
    filename = ET.SubElement(annotation, 'filename').text = str(Image_Number) + '.jpg'
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width').text = str(x_Max)
    height = ET.SubElement(size, 'height').text = str(y_Max)
    depth = ET.SubElement(size, 'depth').text = str(channels)

    for n in range(NumberOfLesions):
        r = random.randint(10,50)
        x = random.randint(r,x_Max-r)
        y = random.randint(r,y_Max-r)

        lesion = str(random.randint(1,4))

        object = ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name').text = lesion
        bndbox = ET.SubElement(object, 'bndbox')

        xmin = ET.SubElement(bndbox, 'xmin').text = str(x-r)
        ymin = ET.SubElement(bndbox, 'ymin').text = str(y-r)
        xmax = ET.SubElement(bndbox, 'xmax').text = str(x+r)
        ymax = ET.SubElement(bndbox, 'ymax').text = str(y+r)

        DrawLesion(x,y,r,lesion)



    print(output_filename_image)
    cv2.imwrite(output_filename_image,im)

    #Write the accompanying xml file.
    tree = ET.ElementTree(annotation)
    #tree.write(output_filename_xml)
    tree.write(output_filename_xml)
