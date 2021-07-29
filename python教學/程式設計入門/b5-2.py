# from pytube import YouTube 
# yt=YouTube('https://www.youtube.com/watch?v=PrjjqkIWfUA&ab_channel=Choobie')
# print(yt.title)               #印出影片標題
# # print(yt.streams.all())     #印出影片全部的格式(多個影片)
# stream=yt.streams.filter(res='720p',video_codec='vp9')[1]   #選出特定影片格式
# stream.download()    #下載影片

import argparse
from pytube import YouTube

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('url',help='指定youtube網址')
    parser.add_argument('-sd',action='store_true', help='480p')
    parser.add_argument('-hd',action='store_true', help='720p')
    parser.add_argument('-fhd',action='store_true', help='1080p')
    parser.add_argument('-a',action='store_true', help='僅下載聲音')

    args=parser.parse_args()
    yt=YouTube(args.url,on_progress_callback=onProgress)
    download_video(yt,args)


def onProgress(stream,chunk,file_handle,remaining):
    total=stream.filesize
    percent=(total-remaining)/total*100
    print('下載中...{:05.2f}%'.format(percent),end='\r')



def download_video(yt,args):
    filter=yt.streams.filter
    if args.hd:
        target=filter(type='video',resolution='720p').first()
    elif args.fhd:
        target=filter(type='video',resolution='1080p').first()
    elif args.sd:
        target=filter(type='video',resolution='480p').first()
    elif args.a:
        target=filter(type='audio').first()
    else:
        target=filter(type='video').first()
    target.download(output_path=pyTube_folder())
import os
from os import path
import platform
def pyTube_folder():
    sys=platform.system()
    home=path.expanduser('~')

    if sys =='Windows':
        folder=path.join(home,'Video','PyTube')
    elif sys =='Darwin':
        folder=path.join(home,'Movies','PyTube')
  
    if not os.path.isdir(folder):
        os.mkdir(folder)

    return folder

