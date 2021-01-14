from django.db import models
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from tinymce import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="뉴스 카테고리를 입력하세요")

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    # content = models.TextField()
    createDate = models.DateTimeField(blank=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text="카테고리를 설정하세요")
    author = models.CharField(max_length=30, null=True,default='none')
    main3 = models.BooleanField(default=False)
    editorpick = models.BooleanField(default=False)
    content = HTMLField()
    textcontent = models.TextField(null=True,default='none')
    image = models.ImageField(upload_to= 'blogimg',blank=True) 
    image_thumbnail_1 = ProcessedImageField(upload_to='blogimg/thumbnail', processors=[ResizeToFill(500,300)], format='JPEG', blank=True)
    image_thumbnail_2 = ProcessedImageField(upload_to='blogimg/thumbnail', processors=[ResizeToFill(1900,1140)], format='JPEG', blank=True)
    image_thumbnail_3 = ProcessedImageField(upload_to='blogimg/thumbnail', processors=[ResizeToFill(300,400)], format='JPEG', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse("single", args=[str(self.id)])
        return reverse("post", args=[str(self.id)])
    
    def is_content_more125(self):
        return len(self.textcontent) > 125
    
    def get_content_under125(self):
        return self.textcontent[:125]

    def is_content_more320(self):
        return len(self.textcontent) > 320

    def get_content_under320(self):
        return self.textcontent[:300]