from django.db import models


STATUS_CHOICES = {
    ("PROCESSING", "PROCESSING"),
    ("COMPLETED", "COMPLETED"),
    ("FAILED", "FAILED")
}


class Video(models.Model):
    title = models.CharField(max_length=100, default=None, null=True)
    filename = models.FileField(upload_to='media/', default=None, null=True)
    url360p = models.CharField(max_length=1000, default=None, null=True)
    url480p = models.CharField(max_length=1000, default=None, null=True)
    url720p = models.CharField(max_length=1000, default=None, null=True)
    url1080p = models.CharField(max_length=1000, default=None, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="PROCESSING")
    message = models.CharField(max_length=1000, default=None, null=True)
    original_res = models.CharField(max_length=20, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Format(models.Model):
#     name = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class VideoUrl(models.Model):
#     video = models.ForeignKey()
#     format = models.ForeignKey()
#     url360p = models.CharField(max_length=1000)
#     url480p = models.CharField(max_length=1000)
#     url720p = models.CharField(max_length=1000)db.sqlite3
#     url1080p = models.CharField(max_length=1000)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

