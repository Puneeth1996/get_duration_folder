import os
from datetime import date



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
            write_text(os.path.join(root, file) + 2*"\n")
    write_text( 30*" - " + 5*"\n")



os.system("pause")



