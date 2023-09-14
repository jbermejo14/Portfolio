from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Blog(models.Model):
    body = models.TextField()
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
