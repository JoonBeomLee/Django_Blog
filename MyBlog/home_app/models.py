from django.db import models

# Create your models here.
class homeInfo(models.Model):
    # web site title (사이트 상단에 노출될 이름)
    siteTitle = models.CharField(max_length=255)
    # page title (페이지 상단에 노출될 이름)
    pageTitle = models.CharField(max_length=255)
    
class intro(models.Model):
    title = models.TextField()
    content = models.TextField()