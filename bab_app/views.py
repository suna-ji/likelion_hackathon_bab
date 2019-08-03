from django.shortcuts import render, redirect, get_object_or_404
import pdb
from .models import *




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
        post = Post.objects.create(user = user, title = title, content = content, image = image, category = category)
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
def recipepage(request):
    return render(request, 'bab_app/recipe-page.html')
    

def shop(request):
    return render(request, 'bab_app/shop.html')


def shortcodes(request):
    return render(request, 'bab_app/shortcodes.html')   


def submitrecipe(request):
    return render(request, 'bab_app/submit-recipe.html')


def typography(request):
    return render(request, 'bab_app/typography.html')


