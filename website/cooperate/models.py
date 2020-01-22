from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse
# Create your models here.
class quaries(models.Model):
    author = models.CharField(max_length=200)
    subject = models.CharField(max_length=400)
    email = models.EmailField()
    contact = models.PositiveIntegerField()
    text = models.TextField()
    created_data = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("cooperate:ack")

    def __str__(self):
        return self.subject

class faculties(models.Model):
    name = models.CharField(max_length=250)
    collegename = models.CharField(max_length=300)
    subject = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="facultypic/")
    contact = models.CharField(max_length=10)
    email = models.EmailField(default="not@provided.com")
    address = models.TextField(default="NOT_PROVIDED")
    position = models.CharField(max_length=150)
    salary = models.PositiveIntegerField(default=0)
    qualification = models.CharField(max_length=300, default="B.tech")
    center = models.CharField(max_length=250, default="Jamshedpur")

    def get_absolute_url(self):
        return reverse("cooperate:faculties_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class students(models.Model):
    name = models.CharField(max_length=250)
    pic = models.ImageField(upload_to="studentpic/")
    fathername = models.CharField(max_length=300)
    contact = models.CharField(max_length =10)
    address = models.TextField()
    email = models.EmailField()
    program = models.CharField(max_length=300)
    joinyear = models.PositiveIntegerField()
    pyear = models.PositiveIntegerField()
    feestatus = models.CharField(max_length=50, default="Not paid")
    fee = models.PositiveIntegerField()
    center = models.CharField(max_length=250)
    def get_absolute_url(self):
        return reverse("cooperate:students_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class rankers(models.Model):
    name = models.CharField(max_length=250)
    pic = models.ImageField(upload_to="studentpic/")
    achievement = models.TextField()
    rank = models.CharField(max_length=100)
    program = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("cooperate:rankers_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class centers(models.Model):
    name = models.CharField(max_length=400)
    place = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("cooperate:centers_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + self.place

class fee(models.Model):
    course = models.CharField(max_length=300)
    years  = models.PositiveIntegerField()
    fees = models.PositiveIntegerField()
    type = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("cooperate:fee_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.course
