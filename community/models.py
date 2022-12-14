from django.db import models
from django.conf import settings

# Create your models here.
class Community(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="addedcommunity",
        on_delete=models.CASCADE,
        default="",
    )
    mbti = models.CharField(max_length=10)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_article")
    image = models.ImageField(upload_to="media/images/", blank=True, null=True)


class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Community, related_name="comments", on_delete=models.CASCADE, default=""
    )
    comment_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="addedcomment",
        on_delete=models.CASCADE,
        default="",
    )
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="recomment", null=True
    )

class Notification(models.Model):
    community = models.ForeignKey(Community, related_name="noti_community", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="noti_comment", on_delete=models.CASCADE)
    send_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="send_user")
    receive_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receive_user")
    is_read = models.BooleanField(default=0)