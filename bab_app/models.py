from django.db.models import *
from users.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    view_count = IntegerField(default=0)
    image = ImageField(upload_to="img/")
    likes = ManyToManyField(User, related_name="liked_users")
    category = CharField(max_length = 50, default = "밥")

    def __str__(self):
       return self.title

    def comments(self):
        return Comment.objects.filter(post=self)
    # 이 포스트에 달린 모든 댓글을 가져오기 위한 함수

class Comment(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message


class Ingredient(TimeStampedModel):
    ingre_name = CharField(max_length=100)

    def __str__(self):
       return self.ingre_name

class Postingre(TimeStampedModel):
    post = ForeignKey(Post, on_delete = CASCADE)
    ingredient = ForeignKey(Ingredient, on_delete = CASCADE)
    quantity = CharField(max_length=100) 

    def __str__(self):
       return self.quantity



class Contact(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message