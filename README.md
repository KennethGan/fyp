# Realtime Vehicle Classification and Counting

Download the "fyp-master.zip" and extract "fyp" file to desktop

# Video sample link
https://youtu.be/hbZ9GSciQGo, download the video file then rename the video file to "sample.mp4" and save to desktop

# Tutorial link
https://youtu.be/kt-TONPk8R4 

# Usage: (copy and paste command to terminal)
$ cd ~/Desktop/fyp

# (MYRIAD) video input and video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078.xml -i sample.mp4 -d MYRIAD -k 7 -o Output.avi

# (MYRIAD) video input and no video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078.xml -i sample.mp4 -d MYRIAD -k 7

# (MYRIAD) cam input and video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078.xml -i cam -d MYRIAD -k 7 -o Output.avi

# (MYRIAD) cam input and no video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078.xml -i cam -d MYRIAD -k 7

# (GPU) video input and video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078-fp32.xml -i sample.mp4 -d GPU -k 7 -o Output.avi

# (GPU) cam input and video output,
$ python3 main.py -m models/person-vehicle-bike-detection-crossroad-0078-fp32.xml -i cam -d GPU -k 7 -o Output.avi
