import speech_recognition as sr
#this is used to recognise the speech in the video
import moviepy.editor as mp
#this splits the videos in small cuts
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#Extract the sound from a video file and save it in outputfile . 

num_seconds_video= 88*60
#deciding the size of the video
print("The video is {} milliseconds".format(num_seconds_video))

l=list(range(0,num_seconds_video+1,60))
#using the range function to break the video in parts of 
#60 seconds each.

diz={}
for i in range(len(l)-1):
  #breaking the video into sub parts 
  #and storing them in the folder called chunks.
  #cut{}.mp4".format(i+1)----the files are named in this format 
  #for example cut1.mp4,cut2.mp4-----cutn.mp4.
    ffmpeg_extract_subclip("videol.mp4", l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
    clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i+1)) 
    clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
    #converting the video subparts to audio files and writing them in the converted folder 
    r = sr.Recognizer()
    audio = sr.AudioFile("converted/converted{}.wav".format(i+1))
    #speech recognition 
    with audio as source:
      r.adjust_for_ambient_noise(source)
      #to check if there is any spoken phrase during silence or 
      # if there is any spoken phase during background lines.  
      audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    diz['chunk{}'.format(i+1)]=result

    l_chunks=[diz['chunk{}'.format(i+1)] for i in range(len(diz))]
    text='\n'.join(l_chunks)

    #writing the recognized text from the converted audio..
    #in the text file 
    #which is named as recognized.txt
    with open('recognized.txt',mode ='w') as file: 
    #opening the file in write mode.
      file.write("Recognized Speech:") 
    #writing the text in the file 
      file.write("\n") 
      file.write(text) 
      print("Finally ready!")