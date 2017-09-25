from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Article

class IndexView(generic.ListView):
    template_name = 'blog/base_index.html'
    context_object_name = 'articles'
    paginate_by = 4
    def get_queryset(self):
        return Article.objects.all().order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/base_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(DetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
        # 视图必须返回一个 HttpResponse 对象
        return response


def aboutme(request):
    return render(request, 'blog/base_aboutme.html')




