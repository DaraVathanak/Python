from pytube import YouTube

link = input('Enter YouTube Video URL: ')
yt = YouTube(link)

# Get highest resolution progressive stream (video + audio)
stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

if stream:
    stream.download()
    print('Downloaded:', yt.title)
else:
    print('No suitable stream found.')
