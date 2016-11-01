from django.http import HttpResponse, Http404
import datetime, urllib, urllib.request
from bs4 import BeautifulSoup
from myfirstsite.forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
        now =datetime.datetime.now()
        html="It is now %s."% now
        return HttpResponse(html)

def facebook_scrap(request):
	thepage = urllib.request.urlopen("https://www.facebook.com/5uboston")
	soup = BeautifulSoup(thepage,"html.parser")

#	return HttpResponse(soup.title.text)
	i=1
	
	for wb in soup.findAll('div',{"class":"_5pbx userContent"}):
#		html=i,". ",wb,"\n"
		return HttpResponse(wb)
		
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValuesError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html="In %s hour(s), it will be %s."% (offset, dt)
	return HttpResponse(html)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
        initial={'subject':'I love your site!'})
    return render(request, 'contact_form.html', {'form':
form})
