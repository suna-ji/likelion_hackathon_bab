from django.shortcuts import render, redirect, get_object_or_404
import pdb
from .models import *
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect




def browserecipes(request):
    return render(request, 'bab_app/browse-recipes.html')


def contact(request):
    return render(request, 'bab_app/contact.html')

def productpage(request):
    return render(request, 'bab_app/product-page.html')

def postcreate(request):
    if request.method == "POST":
        user = request.user
        if user.is_anonymous:
            return redirect('account_login')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        cooking_time = request.POST.get('cooking_time')
        cooking_level = request.POST.get('cooking_level')
        post = Post.objects.create(user = user, title = title, content = content, image = image, category = category, amount = amount, cooking_time = cooking_time, cooking_level = cooking_level)
        # 포스트완성
        ingredientname_list = request.POST.getlist('ingredientname')
        ingredientnote_list = request.POST.getlist('ingredientnote')
        for ingre in ingredientname_list:
            if not Ingredient.objects.filter(ingre_name=ingre):
                Ingredient.objects.create(ingre_name = ingre)
        for ingre, quantity in zip(ingredientname_list, ingredientnote_list):
            ingredient = get_object_or_404(Ingredient ,ingre_name = ingre)
            Postingre.objects.create(post = post, ingredient = ingredient, quantity = quantity)     
        # 포스트-재료완성                 
    return redirect('home')
    
    # 포스트-재료 만들기n
def recipepage(request,id):
    therecipe = get_object_or_404(Post, pk = id)
    postingres = Postingre.objects.filter(pk = id)
    print(postingres)
    return render(request, 'bab_app/recipe-page-1.html', {'therecipe' : therecipe, 'postingres':postingres})
    

def shop(request):
    return render(request, 'bab_app/shop.html')


def shortcodes(request):
    return render(request, 'bab_app/shortcodes.html')   


def submitrecipe(request):
    return render(request, 'bab_app/submit-recipe.html')


def typography(request):
    return render(request, 'bab_app/typography.html')



def sendemail(request):
    username = request.POST.get('userName')
    subject = "밥줘 사용자 "+username+"님이 보내신 문의 메일입니다."
    message = request.POST.get('userComment')
    useremail = request.POST.get('userEmail')
    if subject and message and useremail:
        try:
            send_mail(subject, message, useremail, ['givemebab123@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')    
