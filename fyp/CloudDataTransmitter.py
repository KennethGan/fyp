#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyimagesearch.firebasecloud import firebasecloud
from pyimagesearch.dashingrequest import dashingrequest
from imutils.video import FPS

import numpy as np
import argparse
import time
import cv2
import os
import csv
import subprocess
import requests

firebasecloud = firebasecloud()
dashingrequest = dashingrequest()
status = 'Unavailable'
cycle = 0

print("[ INFO ] Starting data transmission to Cloud Server...")
time.sleep(3)
print("[ INFO ] Transmission Started. To close the application, press 'CTRL+C' in terminal")
time.sleep(1)
while True:
    try:
        fps = FPS().start()

        with open('Data_File.csv', 'r') as readfile:
            output_reader = csv.reader(readfile)
            last_line = list(output_reader)
        

        cycle += 1
        print("[ INFO ] Update Cycle: " + str(cycle))
        print(last_line)
        print("")

        cartotalplus = int(last_line[0][0])
        cartotalminus = int(last_line[0][1])
        persontotalplus = int(last_line[0][2])
        persontotalminus = int(last_line[0][3])
        biketotalplus = int(last_line[0][4])
        biketotalminus = int(last_line[0][5])
        detections = int(last_line[0][6])

        if detections > 10:
            status = 'Heavy'
        elif detections >= 5 and detections <= 10:
            status = 'Moderate'
        elif detections > 0 and detections < 5:
            status = 'Low'
        else:
            status = 'None'
            

        totalcount = cartotalplus + cartotalminus + persontotalplus \
            + persontotalminus + biketotalplus + biketotalminus

        firebasecloud.uploadstats(
            cartotalplus,
            cartotalminus,
            persontotalplus,
            persontotalminus,
            biketotalplus,
            biketotalminus,
            status,
            detections
            )

        dashingrequest.updatecarstats(cartotalplus, cartotalminus)
        dashingrequest.updatebikestats(biketotalplus, biketotalminus)
        dashingrequest.updatetotalcount(totalcount)
        dashingrequest.updatetrafficstatus(status)
        dashingrequest.updatetrafficvolume(detections)
        
        fps.update()

    except requests.exceptions.ConnectionError:

        pass
    except IndexError:

        pass
    except ValueError:

        pass
    except KeyboardInterrupt:
        fps.stop()
        break

print("[ INFO ] Elapsed Time: {:.2f}s".format(fps.elapsed()))
print("[ INFO ] Total Update Cycles: " + str(cycle))			
