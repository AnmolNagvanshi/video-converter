# Create your tasks here

from celery import shared_task
from .models import Video
import time
import subprocess


@shared_task
def add():
    # a = 0
    # for i in range(0, 1000):
    #     a += 1
    # # time.sleep(10)
    # print("Celery Working")
    # print(f"Value of a is {a}")
    print("Start")
    v = Video.objects.get(id=1)
    v.url360p = "Anmol Sujeet"
    v.save(update_fields=['url360p'])
    print('Stop...')
    raise Exception("Exception sattu..............")
    return "OK"


@shared_task
def convert_video_resolution(video_id, file_name, new_res):
    video = Video.objects.get(id=video_id)
    print("File Path = ", video.filename)
    file_path = str(video.filename)
    cmd_output = subprocess.run(["ffmpeg", "-i", file_path, "-s", new_res, "converted_media/"+file_name])
    print('Anmol')
    print(cmd_output)
    print(type(cmd_output))
    print(cmd_output.returncode)

