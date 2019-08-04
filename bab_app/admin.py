from django.contrib import admin
from .models import Post,Comment, Ingredient, Postingre, Contact 
from users.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Postingre)
admin.site.register(User)
admin.site.register(Contact)