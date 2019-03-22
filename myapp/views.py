from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
""" Executing custom SQL directly """
from django.db import connection, transaction
import datetime
from passlib.apps import custom_app_context as pwd_context


def index(request):
    """
    Index Page
    :param request:
    :return:
    """
    return render(request, 'index.html', {})


def get_register(request):
    """
    Get Login Page
    :param request:
    :return:
    """
    return render(request, 'get_register.html', {})


def post_register(request):
    """
    Post Login Page
    :param request:
    :return:
    """
    print('Registration Form Submitted')
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        """
        Encrypt the password
        """
        # encrypting a password...
        hashed_password = pwd_context.encrypt(password)
        password = hashed_password

        """ Executing custom SQL directly
        
        """
        cursor = connection.cursor()
        insert_stmt = (
            "INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) "
            "VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s)"
        )
        data = [password, True, username, first_name, last_name, email, False, True, datetime.datetime.today()]
        cursor.execute(insert_stmt, data)
        transaction.commit()
        print('You are registered successfully!!!')
        return render(request, 'get_login.html', {})


def get_login(request):
    """
    Get Login Page
    :param request:
    :return:
    """
    return render(request, 'get_login.html', {})


def post_login(request):
    """
    Post Login Page
    :param request:
    :return:
    """
    print('Login Form Submitted')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        """
        Converting password to django required hash 
        """
        # encrypting a password...
        # hash = pwd_context.encrypt('12345')
        # print(hash)

        # verifying a password...
        # password = pwd_context.verify(password, hash)

        # Data retrieval operation - no commit required
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM auth_user WHERE username=%s", [username])
        # cursor.commit()

        user = cursor.fetchone()

        """
                If we want to authenticate the user without any risk
                then use below method because SQL Injection is major
                Security issue
                """
        # user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            print('Logged in user')
            return render(request, 'dashboard.html', {'user': user})

    print('Error: Go to login again')
    return render(request, 'get_login.html', {})


def dashboard(request):
    """
    dashboard page for user
    :param request:
    :return:
    """
    return render(request, 'dashboard.html', {})


def get_logout(request):
    """
    Logout Method
    :param request:
    :return:
    """
    logout(request)
    return redirect('get_login')
