# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext

from blog.models import Post

def index(request):
	"""blog列表"""
	
	posts = get_list_or_404(Post)
	return render_to_response("blog/index.html",
				  {"posts": posts},
				  context_instance=RequestContext(request))

def post(request, pk):
	"""单篇文章"""
	
	post = get_object_or_404(Post, pk=pk)
	return render_to_response("blog/post.html",
				  {"post": post},
				  context_instance=RequestContext(request))
