from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Category, Pricing, Features, About, SelfInformation, Contact, Customer, Gallery, Video, Blog, Member, Activity
import math
# Create your views here.

# HOMEPAGE VIEW


def index(request):
    categories = Category.get_all_categories()
    prices = Pricing.get_all_prices()
    features = Features.get_all_features()
    abouts = About.get_all_descriptions()
    galleries = Gallery.get_all_galleries()
    informations = SelfInformation.get_all_information()
    blogs = Blog.get_all_blogs()
    # videos = Video.get_all_videos()

    userSession = request.session.get('username')
    context = {
        'categories': categories,
        'prices': prices,
        'features': features,
        'abouts': abouts,
        'galleries': galleries,
        'informations': informations,
        'blogs': blogs,
        # 'videos': videos,
        'user': userSession
    }
    return render(request, 'index.html', context)

    # ABOUTPAGE VIEW


def about(request):
    abouts = About.get_all_descriptions()
    categories = Category.get_all_categories()
    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')

    context = {
        'categories': categories,
        'abouts': abouts,
        'informations': informations,
        'user': userSession
    }

    return render(request, 'about.html', context)

    # GALLERYPAGE VIEW


def gallery(request):
    galleries = Gallery.get_all_galleries()
    userSession = request.session.get('username')
    informations = SelfInformation.get_all_information()

    context = {
        'galleries': galleries,
        'informations': informations,
        'user': userSession
    }

    return render(request, 'gallery.html', context)

    # CONTACTPAGE VIEW


def contact(request):
    if request.method == 'POST':
        concern = request.POST['concern']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        instance = Contact(concern=concern, name=name, email=email,
                           subject=subject)
        instance.save()
        return redirect('contact')

    if request.method == 'GET':
        informations = SelfInformation.get_all_information()
        userSession = request.session.get('username')

        context = {
            'informations': informations,
            'user': userSession
        }
        return render(request, 'contact.html', context)

        # COURSEPAGE VIEW


def courses(request):
    categories = Category.get_all_categories()
    informations = SelfInformation.get_all_information()
    # videos = Video.get_all_videos()
    userSession = request.session.get('username')

    context = {
        'categories': categories,
        'informations': informations,
        # 'videos': videos,
        'user': userSession
    }
    return render(request, 'courses.html', context)


def coursedetails(request, slug):
    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')
    try:
        category = Category.objects.get(slug=slug)
    except:
        return False
    context = {
        'informations': informations,
        'category': category,
        'user': userSession
    }
    return render(request, 'course_details.html', context)

    # PRICINGPAGE VIEW


def pricing(request):
    prices = Pricing.get_all_prices()
    features = Features.get_all_features()
    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')

    context = {
        'prices': prices,
        'features': features,
        'informations': informations,
        'user': userSession
    }
    return render(request, 'pricing.html', context)


def joining(request):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('username')

        member = Member(customer=customer,
                        duration=duration,
                        price=price,
                        address=address,
                        phone=phone)
        member.save()

        return redirect('pricing')

    # SERVICES VIEW


def services(request):
    return render(request, 'services.html')


def schedule(request):
    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')
    context = {
        'informations': informations,
        'user': userSession
    }
    return render(request, 'schedule.html', context)

    # BLOGPAGE VIEW


def blogs(request):
    no_of_post = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    blogs = Blog.get_all_blogs()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_post: page*no_of_post]
    total_page = math.ceil(length/no_of_post)

    if page > 1:
        prev = page - 1
    else:
        prev = None

    if page < total_page:
        nxt = page + 1
    else:
        nxt = None

    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')
    context = {
        'blogs': blogs,
        'informations': informations,
        'user': userSession,
        'prev': prev,
        'nxt': nxt,
        'total_page': range(total_page)
    }
    return render(request, 'blog.html', context)


def blogdetails(request, slug):
    informations = SelfInformation.get_all_information()
    userSession = request.session.get('username')
    try:
        blog = Blog.objects.filter(slug=slug).first()
    except:
        return False
    context = {
        'informations': informations,
        'user': userSession,
        'blog': blog
    }
    return render(request, 'blog_details.html', context)

    # REGISTRATION VIEW


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        value = {
            'name': name,
            'email': email
        }

        instance = Customer(name=name, email=email,
                            password=password)

        error_msg = None

        if len(name) < 4:
            error_msg = 'User name must be of at least 4 characters!'
        elif len(password) < 6:
            error_msg = 'Password can not be less than 6 digits!'
        elif instance.isUserExists():
            error_msg = 'Username Already Exists! Try another!..'
        elif instance.isEmailExists():
            error_msg = 'Email Already Registered!..'

        if not error_msg:
            instance.password = make_password(instance.password)
            instance.save()
            customer = Customer.get_customer_by_username(name)
            request.session['customer_id'] = customer.id
            request.session['username'] = customer.name
            return redirect('index')
        else:
            context = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'registration.html', context)

            # LOGIN VIEW


def login(request):
    return_url = None
    if request.method == 'GET':
        return_url = request.GET.get('return_url')
        # print(request.GET.get('return_url'))
        return render(request, 'registration.html')

    if request.method == 'POST':
        userName = request.POST.get('username')
        userPass = request.POST.get('userpass')
        customer = Customer.get_customer_by_username(userName)
        err_msg = None
        if customer:
            flag = check_password(userPass, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['username'] = customer.name
                # print(return_url)
                if return_url:
                    # print(return_url)
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
                    return redirect('index')
            else:
                err_msg = 'Username or Password Invalid!!'
        else:
            err_msg = 'Username or Password Invalid!!'
        return render(request, 'registration.html', {'err': err_msg})

        # LOGOUT VIEW


def logout(request):
    request.session.clear()
    return redirect('index')


def profile(request, slug):
    customer = request.session.get('username')
    customers = Customer.get_customer_by_username(customer)
    informations = SelfInformation.get_all_information()
    memberships = Member.get_requests_by_customer(customer)
    context = {
        'customers': customers,
        'user': customer,
        'informations': informations,
        'memberships': memberships

    }
    return render(request, 'profile.html', context)


def activities(request, slug):
    if request.method == 'GET':
        customer = request.session.get('username')
        customers = Customer.get_customer_by_username(customer)
        categories = Category.get_all_categories()
        informations = SelfInformation.get_all_information()
        activities = Activity.get_activities_by_customer(customer)
        context = {
            'customers': customers,
            'user': customer,
            'informations': informations,
            'categories': categories,
            'activities': activities

        }
        return render(request, 'activities.html', context)
    if request.method == 'POST':
        title = request.POST.get('title')
        types = request.POST.get('type')
        duration = request.POST.get('duration')
        date = request.POST.get('date')
        customer = request.session.get('username')

        member = Activity(customer=customer,
                          title=title,
                          types=types,
                          duration=duration,
                          date=date)
        member.save()

        return redirect('activity', slug=customer)


""" def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('task') """
