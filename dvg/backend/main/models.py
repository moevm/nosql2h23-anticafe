from django.db import models

from django.conf import settings


Guest = settings.AUTH_USER_MODEL

class Employee(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1488, blank=True)
    perdission = models.CharField(max_length=100, choices=(("АДМ", "администратор"), ("ОФФ", "оффициант")))


class Profile(models.Model):
    user = models.OneToOneField(
        Guest,
        on_delete=models.PROTECT,
    )
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    table = models.ManyToManyField(Table, blank=True)


