import datetime
from django.db import models
from django.utils import timezone


class Tag(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

    
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    pub_date = models.DateTimeField('date published') # auto_now_add=True
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1     #更新浏览的次数，还未保存到数据库
        self.save(update_fields = ['views'])    #用save方法保存到数据库, update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率。  

    def __str__(self):
        return self.title
    
    def intro(self):
        return self.content[:self.content.find('\n')]
