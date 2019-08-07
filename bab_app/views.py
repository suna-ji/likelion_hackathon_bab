from django.shortcuts import render, redirect, get_object_or_404
import pdb
from .models import *
from django.db.models import Count, Q
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
import json



def browserecipes(request):
    user = request.user
    posts = Post.objects.all().order_by('-created_at').annotate(likes_count=Count('likes'))
    ingredient = Ingredient.objects.all()
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        posts = posts.filter(
            Q(title__icontains=q)|
            Q(content__icontains=q)
            ).distinct() # 제목에 q가 포함되어 있는 레코드만 필터링 

    context = {
        'user':user,
        'posts':posts,
        'ingredient':ingredient,
        'q':q,
    }
    return render(request, 'bab_app/browse-recipes.html', context)
  



def contact(request):
    return render(request, 'bab_app/contact.html')

def productpage(request):
    return render(request, 'bab_app/product-page.html')

def postcreate(request):
    if request.method == "POST":
        user = request.user
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


def comment_create(request, id):
    if request.method == "POST":
        user = request.user
        if user.is_anonymous:
            return redirect('account_login')
        post = get_object_or_404(Post, id = id)
        message = request.POST.get('message')
        Comment.objects.create(user = user, post = post, message = message, star = star)
        return redirect('home')

    # 포스트-재료 만들기n
def recipepage(request,id):
    therecipe = get_object_or_404(Post, pk = id)
    postingres = Postingre.objects.filter(pk = id)
    best_posts = Post.objects.order_by('view_count')[:3]
    return render(request, 'bab_app/recipe-page-1.html', {'therecipe' : therecipe, 'postingres':postingres, 'best_posts':best_posts })



def shop(request):
    return render(request, 'bab_app/shop.html')


def shortcodes(request):
    return render(request, 'bab_app/shortcodes.html')   


def submitrecipe(request):
    user = request.user
    if user.is_anonymous:
            return redirect('account_login')
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



def like_toggle(request, post_id):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    post = get_object_or_404(Post, pk=post_id)
    is_like = user in post.likes.all()
    if is_like:
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('home')


def post_like(request):
   user = request.user
   if user.is_anonymous:
       return redirect('account_login')
   pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
   post = get_object_or_404(Post, pk=pk)
   is_like = user in post.likes.all()
   if is_like:
       post.likes.remove(user)
       message = "좋아요 취소"
   else:
       post.likes.add(user)
       message = "좋아요"
   context = {'like_count': post.likes_count,
              'message': message,
              }
   return HttpResponse(json.dumps(context), content_type="application/json")


def favorite_toggle(request, post_id):
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
    post = get_object_or_404(Post,pk=post_id)
    is_favorite = user in post.favorite.all()
    if is_favorite:
        post.favorite.remove(user)
    else:
        post.favorite.add(user)
    return redirect('home')

def favorite(request, user_id):
    user = request.user
    favorite_user = get_object_or_404(User, pk = user_id)
    posts = Post.objects.all()
    posts.favorite
    for post in posts:
        if post.favorite.add(user):
            favorite = post.favorite
    default_view_count = posts.view_count
    posts.view_count = default_view_count + 1
    posts.save()
    context = {
        'user':user,
        'posts':posts,
        }
    return render(request, 'bab_app/index-2.html', context)



