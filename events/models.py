from django.db import models


# 必要なヤツのインストール的なやつ


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}({self.event_title})"
