import os
from moviepy.editor import *

video_name = 'ssni-497.mp4'
video = VideoFileClip(video_name)

output = video.copy()
output.write_videofile(os.path.join('Video',video_name.split('.')[0] + '.mov'),temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


os.remove(video_name)