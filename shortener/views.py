#-*- coding:utf8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL


# Create your views here.
def kirr_redirect_view(request,shortcode=None, *args, **kwargs): #function based view FBV
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return HttpResponseRedirect(obj.url)

# def home_view_fbv(request,*args,**kwargs):
# 	 if request.method == "POST":
# 	 	print(request.POST)
# 	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm(request.GET)
		context = {
			"title":"Submit URL",
			"form":the_form,	
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title":"Submit URL",
			"form":form,	
		}
		template = "shortener/home.html"
		if form.is_valid():
			url = form.cleaned_data.get("post_url")
			if "http" not in url and "www" in url:
				new_url = 'http://' + url
			elif "http" not in url and "www" not in url:
				new_url = 'http://www.' + url 
			else:
				new_url = url
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context ={
				"object":obj,
				"created":created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request,template,context)


class URLRedirectView(View): #class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		# qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
		# if qs.count() != 1 and not qs.exists():
		# 	raise Http404
		# obj = qs.first()
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		print(ClickEvent.objects.create_event(obj))
		# qs = ClickEvent.objects.create_event(obj)
		return HttpResponseRedirect(obj.url)
		





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