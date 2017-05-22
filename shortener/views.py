#-*- coding:utf8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.
def kirr_redirect_view(request,shortcode=None, *args, **kwargs): #function based view FBV
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return HttpResponseRedirect(obj.url)

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})



class KirrCBView(View): #class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
		
	def post(self,request,*args, **kwargs):
		return HttpResponse()






'''
def kirr_redirect_view(request,shortcode=None, *args, **kwargs): #function based view FBV
	#obj = KirrURL.objects.get(shortcode=shortcode)
	print(request.method	)
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	#obj_url = obj.url
	#try:
	#	obj = KirrURL.objects.get(shortcode=shortcode)
	#except:
	#	obj = KirrURL.objects.all().first()

	
	#Person.objects.filter(name__iexact="abc")
	#名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件 
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url

	return HttpResponse("Hello {sc}".format(sc=obj.url))
'''