import moviepy.editor

video = moviepy.editor.VideoFileClip("fav.mp4")


audio = video.audio
audio.write_audiofile("extractsong.mp3")








