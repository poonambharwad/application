from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello from poonam</h1>')

def contactus(request):
    return HttpResponse('<h1> This is contactus Page</h1>')

def address(request):
    return HttpResponse('<h1> This is address Page</h1>')

def desktop(request):
    return HttpResponse('<h1> This is desktop Page</h1>')

def technology(request):
    return HttpResponse('<h1> This is technology Page</h1>')

def web(request):
    return HttpResponse('<h1> This is web Page</h1>')

def mobile(request):
    return HttpResponse('<h1> This is mobile Page</h1>')

# def index(request):
#     return HttpResponse('<h1><a href="https://www.google.com"> target="_blank">open google</a></h1>')
#                        < h1 > <a href="http://www.facebook.com" >open facebook</a></h1>
#
#                        ('<h1 ><a  href="http://www.gmail.com" > open gmail </a></h1>')
#
#                        ('<h1> <a href="https://www.yahoo.com">open yahoo</a></h1>')

def page1(request):
    return HttpResponse("page 1 <a href='/'>Back</h1>")
def page2(request):
    return HttpResponse("page 2 <a href='/'>Back</h1>")
def page3(request):
    return HttpResponse("page 3 <a href='/'>Back</h1>")

    