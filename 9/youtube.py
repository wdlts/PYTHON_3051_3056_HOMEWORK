from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=Nrl0EAVHffY&list=PLSMETuURtTXA0nxGMwg6WDA4rmjjscWT8&index=50&ab_channel=VivaLaDirtLeague')
streams = yt.streams

video_480 = streams.filter(res='480p').desc().first()
audio_best = streams.filter(only_audio=True).desc().first()

video_480.download()
audio_best.download()