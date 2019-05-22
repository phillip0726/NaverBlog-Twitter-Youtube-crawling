#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import pandas as pd
import pytube

mp3_path = './mp3/'
video_path = './video/'
invalid_index = []
f = 0

def manual():
    print('*-------------------------------------------------------------------*')
    print('| 1. This program is video converter.                               |')
    print('| 2. Youtube video -> MP3 file                                      |')
    print('| 3. You have to insert [index][title][url]                         |')
    print('|    in ../data/youtube_url_collection.csv.                         |')
    print('| 4. The [title] value is the title of the YouTube video.           |')
    print('| 5. The [url] value is the url of the video to convert to mp3.     |')
    print('| 6. The mp3 files are stored in the "mp3" folder.                  |')
    print('*-------------------------------------------------------------------*')
    print()


def convertMP3(index_list):
    global invalid_index

    invalid_index = []
    for i in index_list:
        print("(video %03d) Converting..." % (i), end = '')
        try:
            url = f['url'][i]

            yt = pytube.YouTube(url)
            vids = yt.streams.all()[0]
            
            vids.download(video_path)
            mp3_filename = 'new.mp3'
            video_filename = '%03d ' % i + vids.default_filename

            os.rename(video_path + vids.default_filename, video_path + video_filename)
            
            subprocess.call(['ffmpeg', '-i', os.path.join(video_path, video_filename), os.path.join(mp3_path, mp3_filename)])

            os.rename(mp3_path + mp3_filename, mp3_path + video_filename[:-4] + '.mp3')
            print('Finish!')
            
        except Exception as e:
            print(e)
            invalid_index.append(i)
            continue


if __name__ == '__main__':

    manual()

    print('Read url data.....', end = '')
    f = pd.read_csv('../data/youtube_url_collection.csv', encoding = 'cp949')
    print('Finish!')
    
    print(f"Total {len(f['url'])} videos!")
    convertMP3(f.index)

    if len(invalid_index) != 0:
        print()
        print('<Test one more time for invalid url>')
        convertMP3(invalid_index)
        print()
        print('<Invalid url list>')
        for i in invalid_index:
            print('index = %03d, url = %s' %(i, f['url'][i]))

        print()
        
    print('Program Finish!')
