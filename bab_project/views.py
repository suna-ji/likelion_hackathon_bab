from django.shortcuts import render
import pdb

def home(request):
    return render(request, 'bab_app/index.html')


def browserecipes(request):
    return render(request, 'bab_app/browse-recipes.html')


def contact(request):
    return render(request, 'bab_app/contact.html')


def productpage(request):
    return render(request, 'bab_app/product-page.html')


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


