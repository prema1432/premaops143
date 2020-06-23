from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from datetime import datetime

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
gustatus_choice = (
    ('Accept','Accept'),
    ('Pending', 'Pending'),
    ('Reviewing', 'Reviewing'),
    ('Rejected', 'Rejected'),
    ('Contact Faculty', 'Contact Faculty'),

)
ptype_choice = (
    ('Major Project', 'Major Project'),
    ('Minor Project', 'Minor Project'),
('Mini Project', 'Mini Project'),
('Self Project', 'Self Project'),
('Others Project', 'Others Project'),

)
course_choice = (
    ('MCA', 'MCA'),

)
semester_choice = (
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
    ('Fifth', 'Fifth'),
    ('Six', 'Six'),

)

from django.contrib.auth.models import User


class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_guide(self):
        if hasattr(self, 'guide'):
            return True
        return False


    @property
    def is_hod(self):
        if hasattr(self, 'hod'):
            return True
        return False

class Hod(models.Model):

    user = models.OneToOneField(User,related_name='hod' ,on_delete=models.CASCADE, null=True)
    designatation = models.CharField(max_length=100)
    degrees = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='Hodimages/')
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')


    def __str__(self):
        return str(self.user)

class Guide(models.Model):
    user = models.OneToOneField(User,related_name='guide', on_delete=models.CASCADE, null=True)
    designatation = models.CharField(max_length=100)
    degrees = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='Guideimages/')
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')


    def __str__(self):
        return str(self.user)

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student',on_delete=models.CASCADE, null=True)
    batch = models.CharField(max_length=50)
    hallticket = models.BigIntegerField()
    course = models.CharField(max_length=200,choices=course_choice,default='MCA')
    semester = models.CharField(max_length=200, choices=semester_choice, default='Fourth')
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')
    phone = models.BigIntegerField()
    technology=models.CharField(max_length=200)
    photo = models.ImageField(upload_to='Stuimages/')


    def __str__(self):
        return str(self.user)

class pupload(models.Model):
    user = models.ForeignKey(Student,related_name='pupload',on_delete=models.CASCADE)
    ptitle = models.CharField(max_length=200,verbose_name='PROJECT TITLE')
    pdescription = models.TextField(verbose_name='PROJECT DESCRIPTION')
    ptype =  models.CharField(max_length=50, choices=ptype_choice, default='Minor Project',verbose_name='PROJECT TYPE')
    guide = models.ForeignKey(Guide,related_name='guide',on_delete=models.CASCADE,verbose_name='UNDER THE GUIDENCE OF ')
    hod = models.ForeignKey(Hod,related_name='hod',on_delete=models.CASCADE,verbose_name='H O D Sir')

    pphoto = models.ImageField(upload_to='Projects/photos/',verbose_name='PROJECT PHOTO')
    pabstract = models.FileField(upload_to='Project/Abstracts/',verbose_name='PROJECT ABSTRACT FILE')
    ereport = models.FileField(upload_to='Project/Ereports/',verbose_name='PROJECT E-DOCUMENTATION')

    plive = models.URLField(max_length=250,blank=True,verbose_name='PROJECT LIVE SHARE LINK')
    pshare = models.URLField(max_length=250,verbose_name='PROJECT DRIVE LINK')
    photo_1 = models.ImageField(upload_to='Projects/photos/%Y/%m/%d/', blank=True,verbose_name='SCREENSHOTS 1')
    photo_2 = models.ImageField(upload_to='Projects/photos/%Y/%m/%d/', blank=True,verbose_name='SCREENSHOTS 2')
    photo_3 = models.ImageField(upload_to='Projects/photos/%Y/%m/%d/', blank=True,verbose_name='SCREENSHOTS 3')
    photo_4 = models.ImageField(upload_to='Projects/photos/%Y/%m/%d/', blank=True,verbose_name='SCREENSHOTS 4')
    pdate = models.DateTimeField(default=datetime.now,blank=True)
    gustatus = models.CharField(max_length=250,choices=gustatus_choice, default='Pending',verbose_name='PROJECT GUIDE APPROVAL')
    hostatus = models.CharField(max_length=250,choices=gustatus_choice, default='Pending',verbose_name='PROJECT HOD APPROVAL')

    gucomments = models.TextField(default=' No Comments ',verbose_name='GUIDE COMMENTS / SUGGESTIONS')
    hocomments = models.TextField(default=' No Comments ',verbose_name='HOD COMMENTS / SUGGESTIONS')
    rating = models.IntegerField(default='0',verbose_name='PROJECT RATING')

    def __str__(self):
        return self.ptitle
#
# class gstatus(models.Model):
#     user = models.ForeignKey(pupload,related_name='gstatus',on_delete=models.CASCADE)
#     pstatus = models.CharField(max_length=250,default='Pending')
#     comments = models.TextField()
#     about = models.TextField()
#     rating= models.CharField(max_length=250)
#
#     def __str__(self):
#         return str(self.user)