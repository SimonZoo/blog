from django.contrib import admin
from .models import Article, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	fieldsets = [
		('Tags', {'fields':['name']})
	]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Content',          {'fields':['content']}),
        ('Tags',             {'fields':['tags']}),
        ('Date information', {'fields': ['pub_date']}),

    ]
    filter_horizontal = ('tags',)


