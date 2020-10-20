import subprocess

def get_length(filename):
    print(filename)
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of",
                            "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


# print( get_length('1') )


import moviepy.editor

# Converts into more readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds


# Create an object by passing the location as a string
video = moviepy.editor.VideoFileClip("1.mp4")

# Contains the duration of the video in terms of seconds
video_duration = int(video.duration)

hours, mins, secs = convert(video_duration)

print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", secs)