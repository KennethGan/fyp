#!/usr/bin/python
# -*- coding: utf-8 -*-
from firebase import firebase
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="pyimagesearch/GOOGLE_APPLICATION_CREDENTIALS/my-fyp2-ncs2project-857f1-8f70f97f70f3.json"

firebase = \
    firebase.FirebaseApplication('https://my-fyp2-ncs2project-857f1.firebaseio.com/'
                                 , None)
client = storage.Client()
bucket = client.get_bucket('my-fyp2-ncs2project-857f1.appspot.com')
#imageBlob = bucket.blob("snapshot/")

class firebasecloud:

    def uploadstats(
        self,
        cartotalplus,
        cartotalminus,
        persontotalplus,
        persontotalminus,
        biketotalplus,
        biketotalminus,
        status,
        detections
        ):

        cardata = {'Total_Car_Plus': int(cartotalplus),
                   'Total_Car_Minus': int(cartotalminus),
                   'Total_Car_Count': int(cartotalplus + cartotalminus)}

        persondata = {'Total_Person_Plus': int(persontotalplus),
                      'Total_Person_Minus': int(persontotalminus),
                      'Total_Person_Count': int(persontotalplus
                      + persontotalminus)}

        bikedata = {'Total_Bike_Plus': int(biketotalplus),
                    'Total_Bike_Minus': int(biketotalminus),
                    'Total_Bike_Count': int(biketotalplus
                    + biketotalminus)}

        trafficdata = {'Status': status,
                        'Detections': int(detections)}
        
        firebase.put('/Stats/', 'Car', cardata)
        firebase.put('/Stats/', 'Person', persondata)
        firebase.put('/Stats/', 'Bike', bikedata)
        firebase.put('/Stats/', 'Traffic', trafficdata)
        
        if os.path.exists('snapshot/1.jpg') == True:

            imagePath = "snapshot/1.jpg"
        else:
            imagePath = "snapshot/sub1.jpg"

        imageBlob = bucket.blob("1.jpg")
        imageBlob.upload_from_filename(imagePath)		
