import os
from datetime import date
import moviepy.editor



today = date.today()
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")



path         = r'C:\Users\punee\Desktop\ielts_studies\Vocabulary\Udemy - Everyday English Brush Up On Your English Grammar'
extention    = 'mp4'
out_text     = 'Udemy - Everyday English Brush Up On Your English Grammar.txt'


# Converts into more readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds




def write_text(msg):
    filename = out_text
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    textFile = open(filename,append_write)
    textFile.write(msg)
    textFile.close()



write_text( str(d4) + 5*"\n" + 30*" - " + 2*"\n" )


for root, dirs, files in os.walk(path):
    write_text(str(root) +" and "+ str(dirs) +" and "+ str(files) + 2*"\n")
    for file in files:
        if file.endswith(".{}" .format(extention) ):
            mp4_file_path = os.path.join(root, file)
            write_text(file + 1*"\n")
            # Create an object by passing the location as a string
            video = moviepy.editor.VideoFileClip(mp4_file_path)

            # Contains the duration of the video in terms of seconds
            video_duration = int(video.duration)

            hours, mins, secs = convert(video_duration)
            vid_dur = "Vedio Duration = " +str(hours) + "hrs:" + str(mins) + "mins:" +   str(secs) + "secs\n"
            write_text( vid_dur + 2*"\n")
    write_text( 30*" - " + 5*"\n")



os.system("pause")



