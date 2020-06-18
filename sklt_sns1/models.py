from django.db import models
from django.conf import settings
from django.utils import timezone

from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from sns1.utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    id_num = models.FloatField()
    kurasu = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # slug = models.SlugField(max_length = 250, null = True, blank = True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    def __str__(self):
        return self.name

       
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(User, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    like = models.ManyToManyField(User, related_name='like')
    # slug = models.SlugField(max_length=500, unique=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    # def __str__(self):
    #     return self.text

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.created_date)
    #     return super(Post, self).save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.text)
    #     return super(Post, self).save(*args, **kwargs)

class Ine(models.Model):
    ip_address = models.CharField('IPアドレス', max_length=20)
    parent = models.ForeignKey(Post, on_delete=models.CASCADE) 

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comment')
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text





