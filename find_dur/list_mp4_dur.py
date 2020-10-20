import os
from datetime import date
import moviepy.editor




# Converts into more readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds




def write_text(msg):
    filename = 'Log.txt'
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    textFile = open(filename,append_write)
    textFile.write(msg)
    textFile.close()


today = date.today()
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")


write_text( str(d4) + 5*"\n" + 30*" - " + 2*"\n" )


path         = r'C:\Users\punee\Desktop\ielts_studies\Vocabulary\Udemy - Everyday English Brush Up On Your English Grammar'
extention    = 'mp4'


for root, dirs, files in os.walk(path):
    write_text(str(root) +" and "+ str(dirs) +" and "+ str(files) + 2*"\n")
    for file in files:
        if file.endswith(".{}" .format(extention) ):
            mp4_file_path = os.path.join(root, file)
            write_text(mp4_file_path + 1*"\n")
            # Create an object by passing the location as a string
            video = moviepy.editor.VideoFileClip(mp4_file_path)

            # Contains the duration of the video in terms of seconds
            video_duration = int(video.duration)

            hours, mins, secs = convert(video_duration)
            vid_dur = "Vedio Duration = " +str(hours) + ":" + str(mins) + ":" +   str(secs) + "\n"
            write_text( vid_dur + 2*"\n")
    write_text( 30*" - " + 5*"\n")



os.system("pause")



