import moviepy.editor as mp
  
# Insert Local Video File Path 
clip = mp.VideoFileClip("Videos\Video001-Scene-019.mp4")
  
# Insert Local Audio File Path
clip.audio.write_audiofile("Generated\Audio\Audio_1.wav")