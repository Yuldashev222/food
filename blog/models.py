from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='post')
    tags = models.ManyToManyField(Tag, related_name='post')
    date_cr = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug': self.cat.slug, 'post_slug': self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipe')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.name
