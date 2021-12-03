from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse('''Hello world <a href="https://stackoverflow.com/questions/5768797/manage-py-runserver"> Stack Overflow </a>''')
def searchpunc(request):
    a=""
    if request.method == 'POST':
        a = request.POST.get('title')
        print(a)
        b = request.POST.get('ckbox')
        c = request.POST.get('ckbox1')
        d = request.POST.get('ckbox2')
        analyzed = ''
        punctuation = ''',":';!@#$%^&*()\}[{/]'''
        if b and not c and not d:
            for char in a:
                if char not in punctuation:
                    analyzed = analyzed + char

            params = {'punctuation': analyzed}        
    #    if b:
     #       return HttpResponse(a)
      #  else:
       #     return HttpResponse('You didn\'t check the box' )
            return render(request,'searchpunc.html',params)
        elif c and not b and not d:
            for char in a:
                analyzed = analyzed + char.upper()
                params = {'punctuation': analyzed}        
    #    if b:
     #       return HttpResponse(a)
      #  else:
       #     return HttpResponse('You didn\'t check the box' )
            return render(request,'searchpunc.html',params)
        elif d and not b and not c:
            print("d")
            for char in a:
                analyzed = len(a)
                params = {'punctuation': analyzed}        
    #    if b:
     #       return HttpResponse(a)
      #  else:
       #     return HttpResponse('You didn\'t check the box' )
            return render(request,'searchpunc.html',params)
        elif b and c and not d:
            #analyz = ""
            for char in a:
                if char not in punctuation:
                    analyzed = analyzed + char.upper()   
            #for char in analyzed:
            #    analyzed = analyzed + char.upper()
                params = {'punctuation': analyzed}
            return render(request,'searchpunc.html',params)
        elif b and d and not c:
            analyz = ""
            for char in a:
                if char not in punctuation:
                    analyz = analyz + char
                    s = len(a)
            analyzed = analyz + format(s)
            params = {'punctuation': analyzed}        
    #    if b:
     #       return HttpResponse(a)
      #  else:
       #     return HttpResponse('You didn\'t check the box' )
            return render(request,'searchpunc.html',params)
        elif c and d and not b:
            analyz = ""
            for char in a:
                analyz = analyz + char.upper()
                s = len(a)
            analyzed = analyz + format(s)
            params = {'punctuation': analyzed}        
    #    if b:
     #       return HttpResponse(a)
      #  else:
       #     return HttpResponse('You didn\'t check the box' )
            return render(request,'searchpunc.html',params)
        elif b and c and d:
            analyz = ""
            for char in a:
                if char not in punctuation:
                    analyz = analyz + char.upper()
                    s = len(a)   
            #for char in analyzed:
            #    analyzed = analyzed + char.upper()
            analyzed = analyz + format(s)
            params = {'punctuation': analyzed}
            return render(request,'searchpunc.html',params)
        else:
            return HttpResponse('<h1>error</h1>')    
