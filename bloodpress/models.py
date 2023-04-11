from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.question_text


class Response(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.question_text} - {self.response_text}"
