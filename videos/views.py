import json
import subprocess
import threading
from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .tasks import add, convert_video_resolution
import time


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        video_file = request.data['file']
        video = Video(filename=video_file)
        video.save()
        print(str(video_file))
        new_res = request.data["new-resolution"]

        extension = str(video_file).split(".")[-1]
        output_filename = str(time.time()).split(".")[0] + new_res + "." + extension
        print(output_filename)

        # convert_video_resolution.delay(video_file, output_filename, new_res)
        convert_video_resolution.apply_async(args=(video.id, output_filename, new_res))

        # new_res = request.data["new-resolution"]
        # print(new_res)
        # convert_thread1 = threading.Thread(target=self.convert_video_resolution, args=[video, new_res])
        # convert_thread1.start()

        # new_format = request.data['new-format']
        # convert_thread2 = threading.Thread(target=self.convert_video_format, args=[video, new_format])
        # convert_thread2.start()

        return Response(data={'message': 'file saved'}, status=status.HTTP_201_CREATED)

    # def convert_video_resolution(self, video, new_res):
    #     cmd_output = subprocess.run(["ffmpeg", "-i", str(video.filename), "-s", new_res, "media/Mars2" + new_res + ".mp4"])
    #     print('Anmol')
    #     print(cmd_output)
    #     print(type(cmd_output))
    #     print(cmd_output.returncode)

    def convert_video_format(self, video, new_format):
        cmd_output = subprocess.run(["ffmpeg", "-i", str(video.filename), "media/Marvelz" + "." + new_format])


class VideoDetail(APIView):

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        video = self.get_object(pk)
        video_serializer = VideoSerializer(video)
        return Response(video_serializer.data)

    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CeleryDemo(APIView):

    def get(self, request):
        add.delay()
        # add.apply_async(countdown=10)
        print('Before')
        return Response({"message": "OK"})
