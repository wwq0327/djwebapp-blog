# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.views.generic import ListView, DetailView

from blog.models import Post, Category

class PostList(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/index.html'

	def get_context_data(self, **kwargs):
		ctx = super(PostList, self).get_context_data(**kwargs)
		ctx['categories'] = Category.objects.all()
		return ctx

index = PostList.as_view()


class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'blog/post.html'

	def get_context_data(self, **kwargs):
		ctx = super(PostDetailView, self).get_context_data(**kwargs)
		ctx['categories'] = Category.objects.all()

		return ctx

post = PostDetailView.as_view()

def category(request, pk):
	"""相应分类下的文章检索"""

	try:
		cate = Category.objects.get(pk=pk)
	except Category.DoesNotExist:  ## 读取分类，如果不存在，则引发错误，并404
		raise Http404

	posts = cate.post_set.all() ## 获取分类下的所有文章
	return render_to_response('blog/index.html', ## 使用首页的文章列表模版，但加入了的一个`is_category`开关
		{"posts": posts,
		"is_category": True,
		"cate_name": cate.name,
		"categories": Category.objects.all()},
		context_instance=RequestContext(request))

