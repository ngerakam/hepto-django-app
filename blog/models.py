from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    title = models.CharField(max_length=255)
    tagged_article = models.ForeignKey(
        'Article', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=255)
    featured_article = models.ForeignKey(
        'Article', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Article(models.Model):
    class Meta:
        ordering = ['-date_written']

    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField()
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.PROTECT)
    author = models.ForeignKey(
        Author, blank=True, null=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=1500, blank=True, null=True)
    date_written = models.DateTimeField(auto_now_add=True, null=True)
    picture = models.ImageField(default="mess.png", null=True, blank=True)
    tag = models.ForeignKey(
        Tag, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    # # def get_absolute_url(self):
    # #     return reverse("article_detail", kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
