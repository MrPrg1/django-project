from django.db import models
CHOICES_NAME = [
    (1, 'rap'),
    (2, 'pap'),
]
class SingerModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    style = models.IntegerField(choices=CHOICES_NAME, default=1)

    def __str__(self):
        return self.name()


class MuzicModel(models.Model):
    name = models.CharField(max_length=50)
    Singer = models.ForeignKey(SingerModel, on_delete=models.CASCADE)
