import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import load_model
from imutils.video import FileVideoStream,VideoStream, FPS
import time
import cv2
import argparse
import matplotlib.pyplot as plt
import numpy as np
from warnings import filterwarnings as w; w('ignore')

video_file_path = "Videos\Video001-Scene-001.mp4"
save_path = "Generated\Frames\img_"


#vs = cv2.VideoCapture(video_file_path)
vs = FileVideoStream(video_file_path).start()	#load/capture video
time.sleep(1.0)

fourcc = cv2.VideoWriter_fourcc(*'avc1')		#define encoding format

fps = FPS().start()

i = 0	#for first loop to create video

while vs.more():

	i+=1
	#grabbed, frm = vs.read()
	frm = vs.read()

	if frm is None:
		print("NO MORE FRAMES")
		break
	
	cv2.imwrite(save_path+str(i)+".png", frm)

	fps.update()	#newly added

fps.stop()
cv2.destroyAllWindows()
vs.stop()







