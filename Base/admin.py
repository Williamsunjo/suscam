from django.contrib import admin
from .models import *
from .models import Courses, Products, Profile, ContactUs, Comments


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_id', 'price','created']
    list_per_page = 5
    list_filter = ['course_name', 'course_category','course_id','price','created']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id', 'available', 'category','price', 'created']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_id','profile_img', 'country', 'city', 'date_of_birth']

    
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contactNumber', 'subject','sent_date']
    list_per_page = 5
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'id','message', 'comment_date',]

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'id','position', ]


admin.site.register(Courses, CourseAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ContactUs, ContactUsAdmin)

admin.site.register(Comments, CommentAdmin)
admin.site.register(Enrollment)
admin.site.register(Team, TeamAdmin)


