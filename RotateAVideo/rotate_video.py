

video_dir = input("Enter path to video: ")
degrees_to_rotate = input("Enter degrees to rotate the video(ex. -90): ")

# Import everything needed to edit video clips 
from moviepy.editor import *
  
# loading video dsa gfg intro video 
clip = VideoFileClip(video_dir) 

# rotating clip by
clip = clip.rotate(degrees_to_rotate) 

# showing clip 
clip.ipython_display() 