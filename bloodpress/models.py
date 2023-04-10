from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pressure_result = models.FloatField()

    def __str__(self):
        return f"{self.question.question_text} - {self.pressure_result}"
