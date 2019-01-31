from django.shortcuts import render
from rango.models import Page, Category
from django.http import HttpResponse
#from django.template import RequestContext

def index(request):

    #return HttpResponse('Rango says hello world! <br><a href="/rango/about/">About</a>')
    # Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"} #refers to the index html page
    #request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5] #first five most viewed records
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)



def about(request):

    context_dict = {
        'aboutmessage': "I am about message."
    }
    #return HttpResponse('Rango Says: Here is the about page.<br><a href="/rango/">Back to home page</a>')

    return render(request, 'rango/about.html', context=context_dict)




