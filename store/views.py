from django.shortcuts import render


def index(request):
	
	context = {} #context fictionary to pass some data 
	return render(request, 'html/store.html', context) #return a html template , through context inside the remplate to see it there