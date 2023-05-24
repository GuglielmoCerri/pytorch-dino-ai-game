import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

labels = []

dir = 'captures'  # directory to get the captured images from

# get the labels for each image in the directory

for f in os.listdir(dir):
    key = f.rsplit('.', 1)[0].rsplit(" ", 1)[1]

    if key == "n":
        labels.append({'file_name': f, 'class': 0})
    elif key == "space":
        labels.append({'file_name': f, 'class': 1})

field_names = ['file_name', 'class']

# write the labels to a csv file
with open('labels.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(labels)