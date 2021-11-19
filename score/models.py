from django.db import models


class Score(models.Model):
    score_1 = models.SmallIntegerField(null=True, blank=True)
    score_2 = models.SmallIntegerField(null=True, blank=True)
    score_3 = models.SmallIntegerField(null=True, blank=True)
    score_4 = models.SmallIntegerField(null=True, blank=True)

    score_1_created_at = models.DateTimeField(null=True, blank=True)
    score_2_created_at = models.DateTimeField(null=True, blank=True)
    score_3_created_at = models.DateTimeField(null=True, blank=True)
    score_4_created_at = models.DateTimeField(null=True, blank=True)
