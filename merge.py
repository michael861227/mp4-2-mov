import os
import time
# from typing import Concatenate
from moviepy.editor import *

def mergeMp4(folderPath, tsList, videoPath):
	# 開始時間
    start_time = time.time()
    print('開始合成影片..')

    
    for i in range(len(tsList)):
        file = tsList[i].split('/')[-1][0:-3] + '.mp4'
        full_path = os.path.join(folderPath, file)
        video_name = folderPath.split(os.path.sep)[-1]
        final_video = os.path.join(videoPath, video_name + '.mp4')
        if os.path.exists(full_path):
            with open(full_path, 'rb') as f1:
                with open(final_video, 'ab') as f2:
                    f2.write(f1.read())
        else:
            print(file + " 失敗 ")

     
    video = VideoFileClip(final_video)
    output = video.copy()
    output.write_videofile(os.path.join(videoPath, video_name + '.mov'), temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
    os.remove(final_video)
    
    end_time = time.time()
    print('花費 {0:.2f} 秒合成影片'.format(end_time - start_time))
    print('下載完成!')
