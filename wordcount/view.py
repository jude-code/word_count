from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['hi'] = 'hi World!'
    context['a'] = 'http://www.baidu.com'
    return render(request, 'hello.html', context)



def home(request):
    return render(request, 'home.html')