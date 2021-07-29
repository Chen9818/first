from pytube import YouTube


def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')



if __name__ == "__main__":
    # Init
    url = 'https://www.youtube.com/watch?v=vynjxg1kDls&ab_channel=Sushi%5BHololiveandVtubers%5D'
    yt = YouTube(url, on_progress_callback=progress)
    video = yt.streams.first()
    
    # file_size
    file_size = video.filesize

    # Download
    video.download()