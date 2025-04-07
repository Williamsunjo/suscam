from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ContactForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Courses, Products, Profile, Comments
from django.db.models import Q
from django.core.paginator import Paginator



user_profile = Profile.objects.all()

# Create your views here.

#homepage
# @login_required(login_url='login')
def index(request):
    products = Products.objects.all()[::-1][0:4]
    # user_profile = Profile.objects.get(user = request.user)
    # user_object = User.objects.get(username = request.user.username)
    # user_profile = Profile.objects.get(user=user_object)
    comments = Comments.objects.all()[0:4]
    course  = Courses.objects.all()[::-1][0:4]
    form = CommentForm(request.POST or None)
    if form.is_valid():

        comment = form.save(commit=False)
        comment.user = request.user
        #comment.post = post
        comment.save()

        form.save()

        return redirect('index')
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)
    context = {
        'course': course,
        'products': products,
        'form': form,
        'comments': comments,

        'user_profile': user_profile,

        # 'search':search,
    }
    return render(request, 'Home/index.html', context)

#defining function to get a single course
@login_required(login_url='login')
def course(request, pk):
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)
    course = Courses.objects.get(course_id=pk)
    course2 = Courses.objects.all()[0:6][::-1]
    products = Products.objects.all()[0:6][::-1]
    # products = product[0::6]
    context = {
        'course': course,
        'course2': course2,
        'products': products,
        'user_profile': user_profile,
        # 'user_profile': user_profile,
        }
    return render(request, 'Courses/course.html', context)

def search_results(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create a new Profile object if it doesn't exist
        user_profile = Profile.objects.create(user=request.user)
    query = request.GET.get('query')
    referer = request.META.get('HTTP_REFERER') #get the referer url
    
    #check if query is empty or not
    if not query:
        if referer:
            return redirect(referer)
        else:
            return redirect('index')
    courses = Courses.objects.filter(
        Q(course_name__icontains=query) |
        Q(course_category__icontains=query) |
        Q(description__icontains=query) |
        Q(price__icontains=query)
    )
    products = Products.objects.filter(name__icontains=query)
    #print(query)
    
    search_results = list(products) + list(courses)
    total_found1 = courses.count()
    total_found2 = courses.count()
    total_found = total_found1 + total_found2
    context = {
        'search_results': search_results,
        'query': query,
        'total_found': total_found,
        'user_profile': user_profile,
    }
    return render(request, 'Search/search_result.html', context)

def courses(request):
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)

    course_list = Courses.objects.all()
    course_list = Courses.objects.all()[::-1]

    total = Courses.objects.all().count()
    
    #adding paginator to contains 8 items per page
    paginator = Paginator(course_list, 4)
    
    #get current page number from the request GET parameters
    page_number = request.GET.get('page')
    
    #get the page object from the current page
    page_obj = paginator.get_page(page_number)
    
    #get slice list of item for the current page
    slice_courses = page_obj.object_list
    context = {
        'course_list': slice_courses,
        'total': total,
        'page_obj' : page_obj,

        'user_profile' : user_profile,
        # 'user_profile' : user_profile,
    }
    return render(request, 'Courses/courses.html', context)

#products Page List
def products(request):
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)
    products = Products.objects.all()

    products = Products.objects.all()[::-1]

    total = Products.objects.all().count()
    #adding paginator to contains 8 items per page
    paginator = Paginator(products, 4)
    
    #get current page number from the request GET parameters
    page_number = request.GET.get('page')
    
    #get the page object from the current page
    page_obj = paginator.get_page(page_number)
    
    #get slice list of item for the current page
    slice_products = page_obj.object_list
    context = {
        'products': slice_products,
        'total': total,
        'page_obj' : page_obj,

        'user_profile' : user_profile,

        # 'user_profile' : user_profile,

    }
    return render(request, 'Products/products.html', context)

#function to get a Single Product
@login_required(login_url='login')
def product(request, pk):
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)
    product1 = Products.objects.all()[::-1]
    product_list = product1[:6]
    courses = Courses.objects.all()[::-1][0:6]
    product = Products.objects.get(product_id=pk)
    context = {
        'product': product,
        'product_list': product_list,
        'courses': courses,

        'user_profile': user_profile,

        # 'user_profile': user_profile,

        }
    return render(request, 'Products/product.html', context)

def about(request):
    # user_profile = Profile.objects.get(user=request.user)
    context = {
        # 'user_profile': user_profile,
    }
    return render(request, 'About/about.html', context)

def profile(request, pk):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create a new Profile object if it doesn't exist
        user_profile = Profile.objects.create(user=request.user)
        user = User.objects.get(id = pk)
    context = {
        # 'user': user,
        'user_profile': user_profile
    }
    return render(request, 'Profile/profile.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # try:
        #     user = User.objects.get(username=username, password=password)
            
        # except:
        #     messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            messages.error(request, "Wrong Username or Password, please try again!")
    context = {
        
    }
    return render(request, 'Authenticate/login.html', context)

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, "Email already Exist, used a different email address"
                )
                return redirect("register")
            
            if len(username) < 4:
                messages.info(request, "Username must be at least 4 characters")
                return redirect("register")
            # Get the email from the form
            # Save the email or perform any necessary operations
            user = form.save(commit=False)

            user.username = user.username.lower()

            user.email = email.lower()
            user.save()
            login(request, user)


            #create a Profile model for the new user
            # user_model = User.objects.get(username=username)
            # new_profile = Profile.objects.create(
            #     user=user_model, id=user_model.id
            # )
            # new_profile.save()
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration!')
            return redirect("register")
    return render(request, 'Authenticate/register.html', {'form': form, })



def logout_view(request):
    logout(request)
    return redirect('login')

#Creating the contact form view
def contact_us(request):
    courses = Courses.objects.all()[0:5][::-1]
    products = Products.objects.all()[0:5][::-1]
    # try:
    #     user_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     # Create a new Profile object if it doesn't exist
    #     user_profile = Profile.objects.create(user=request.user)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank You, Your Message was submitted Successfully!')
        return redirect('contact')
    context = {
        # 'user_profile': user_profile,
        'form': form,
        'courses': courses,
        'products': products,
    }
    return render(request, 'Contact/contact.html', context)

#function to display terms and conditions when logging in !
def terms_conditions(request):
    context = {}
    return render(request, 'Terms_Conditions/terms_conditions.html', context)

def comments(request):
    user_profile = Profile.objects.all()
    comments = Comments.objects.all()
    return render(request, 'Home/comments.html', { 'comments': comments, 'user_profile' : user_profile, })
