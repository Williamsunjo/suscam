
import uuid
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django_countries.field import CountryField
#from phonenumber_field.modelfields import PhoneNumberField

# def Validate_Course_id(value):
#     pattern = r'^(?!.*(.).*\1)[a-zA-Z0-9-]{36}$'
#     if not re.match(pattern, str(value)):
#         raise ValidationError('Course id must contains at least 4 different characters!')

# Create your models here.
class Courses(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=250)
    description = models.TextField()
    video_file = models.FileField(upload_to='Course_Videos/')
    paid = models.BooleanField(default=False)
    course_category = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField( default=1000, max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    course_img = models.ImageField(upload_to='CourseImage/', validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])], null=True, blank=True)
    created = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now=True)
    #ratings = models.
    model_type = 'Course'
    
    class Meta:
        ordering = ('created', 'updated')
    
    def save(self, *args, **kwargs):
        if not self.course_id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name

#create Products model
class Products(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.BigAutoField(primary_key=True)
    product_des = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)
    created = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='Product_Images', validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    model_type = 'Products'

    class Meta:
        ordering = ['-created', '-updated']
    #rating = models

#creating enrol
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, related_name='course_enrollment')
    
    
    def __str__(self):
        return self.user.username

    #rating = models


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField( primary_key=True)
    message = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-comment_date',]

    def __str__(self):
        return self.user.username
    
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(default=1)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="profile_Images", default="default.jpg",  validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    phone_number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    level_of_education = models.CharField(max_length=200, blank=True, null=True)
    courses_enroll = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    profile_img = models.ImageField(upload_to="profile_Images", default="default.png")
    #phone_number = models.PhoneNumberField(blank=True)
    #country = models.CountryField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username
    
class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    contactAddress = models.CharField(max_length=250, blank=True, null=True)
    contactNumber = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    sent_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-sent_date',)
    def __str__(self):

        return self.subject
    
#our team members
class Team(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length= 300)
    member_description = models.TextField()
    member_img = models.ImageField(upload_to="TeamImages", validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    facebook_url = models.URLField(max_length=1000, blank=True, null=True)
    linkedin_url = models.URLField(max_length=1000, blank=True, null=True)
    twitter_url = models.URLField(max_length=1000, blank=True, null=True)
    histogram_url = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

        return self.subject

