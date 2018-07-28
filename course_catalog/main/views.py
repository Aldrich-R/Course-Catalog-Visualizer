from django.http import HttpResponse
from django.template import loader

from .models import Course

def main(request):
	template = loader.get_template('main/main.html')
	context = {}
	return HttpResponse(template.render(context, request))