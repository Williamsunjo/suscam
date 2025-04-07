from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course/<str:pk>/', views.course, name='course'),
    path('search_results/', views.search_results, name='search_results'),
    path('courses/', views.courses, name='courses'),
    path('products/', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('profile/<str:pk>/', views.profile, name='profile'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('contact/', views.contact_us, name='contact'),

    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('comments/', views.comments, name='comments'),
]