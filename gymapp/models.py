from django.db import models
import datetime
from embed_video.fields import EmbedVideoField
# Create your models here.

# Category of courses


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(default=False)
    descr_short = models.CharField(max_length=350, default=False)
    slug = models.CharField(max_length=100, null=True)
    images = models.ImageField(null=True, blank=True)

    @staticmethod
    def get_all_categories():
        try:
            return Category.objects.all()
        except:
            return False

    def __str__(self):
        return self.name

# Pricing Category


class Pricing(models.Model):
    duration = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    item = models.CharField(max_length=25, default=False)
    offer = models.CharField(max_length=25, null=True)
    offerprice = models.CharField(max_length=25, null=True)

    @staticmethod
    def get_all_prices():
        try:
            return Pricing.objects.all()
        except:
            return False

    def __str__(self):
        return self.duration


class Features(models.Model):
    name = models.CharField(max_length=25)

    @staticmethod
    def get_all_features():
        try:
            return Features.objects.all()
        except:
            return False

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=10, default='Us')
    descriptionOne = models.TextField()
    descriptionTwo = models.TextField()

    @staticmethod
    def get_all_descriptions():
        try:
            return About.objects.all()
        except:
            return False

    def __str__(self):
        return self.name


class SelfInformation(models.Model):
    name = models.CharField(max_length=10, default='GymHut')
    locationTitle = models.CharField(max_length=80, null=True)
    locationDesc = models.TextField(null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    time = models.CharField(max_length=50, default=False)
    maps = models.URLField()

    @staticmethod
    def get_all_information():
        try:
            return SelfInformation.objects.all()
        except:
            return False

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    concern = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=30)
    images = models.ImageField(null=True, blank=True)

    @staticmethod
    def get_all_galleries():
        try:
            return Gallery.objects.all()
        except:
            return False

    def __str__(self):
        return self.name


class SubGallery(models.Model):
    name = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    imagename = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def isEmailExists(self):
        try:
            if Customer.objects.filter(email=self.email):
                return True
            else:
                return False
        except:
            return False

    def isUserExists(self):
        try:
            if Customer.objects.filter(name=self.name):
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def get_customer_by_username(userName):
        try:
            return Customer.objects.get(name=userName)
        except:
            return False


class Video(models.Model):
    video = EmbedVideoField()

    @staticmethod
    def get_all_videos():
        try:
            return Video.objects.all()
        except:
            return False


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=350, default=False)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.datetime.today)
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_all_blogs():
        try:
            return Blog.objects.all()
        except:
            return False

    def __str__(self):
        return self.title


class Member(models.Model):
    customer = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    price = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer

    @staticmethod
    def get_requests_by_customer(username):
        try:
            return Member.objects.filter(customer=username).order_by('-date')
        except:
            return False


class Activity(models.Model):
    customer = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    types = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.customer

    @staticmethod
    def get_activities_by_customer(username):
        try:
            return Activity.objects.filter(customer=username).order_by('-date')
        except:
            return False
