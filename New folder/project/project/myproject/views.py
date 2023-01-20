from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from myproject import forms
from myproject.models import service
# Create your views here.


def index(request):

    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    if request.method == 'GET':
        hellow = request.GET.get('output')
    return render(request, 'about.html', {'khan': hellow})


def blog(request):
    serviceData=service.objects.all()
    data = {
        'title': 'This is Blog page',
        'body': 'This is the Blog body page text render from views',
        'course': ['java', 'pytthon', 'c++'],
        'student': [
            {'name': 'saeed ullah', 'phone': '03336713258'},
            {'name': 'khan', 'phone': '03469307889'}
        ],
        'number': [12, 32, 43, 45, 66, 77, 88],
        'formdata':serviceData
    }

    return render(request, 'blog.html', data)


def blogdetail(request, detail):
    return HttpResponse(detail)


def form(request):
    answer = 0
    data = {}
    try:
        if request.method == 'POST':
            # if request.method == 'GET':
            # n1 = int(request.GET['name'])
            # n2 = int(request.GET['phone'])
            # n1 = int(request.GET.get('name'))
            # n2 = int(request.GET.get('phone'))

            n1 = int(request.POST['name'])
            n2 = int(request.POST['phone'])
        answer = n1+n2
        data = {
            'n12': n1,
            'n22': n2,
            'output': answer
        }
        url = '/about?output={}'.format(answer)
        return HttpResponseRedirect(url)

    except:
        pass
    return render(request, 'form.html', data)
    # {'output': answer}


def saeed(request):
    c = ''

    if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num1'))
            opr = request.GET.get('opr')
            if opr == '*':
                c = n1 * n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '/':
                c = n1 / n2
            elif opr == '+':
                c = n1+n2
            else:
                c = n1 % n2

    return render(request, 'saeed.html',{'ans':c})


def sheet(request):
    if request.method == "POST":
        n1 = int(request.POST['maths'])
        n2 = int(request.POST['computer'])
        n3 = int(request.POST['physics'])
        n4 = int(request.POST['islamyat'])
        per = int(request.POST['per'])
        grade = int(request.POST['grade'])
        t = n1+n2+n3+n4 
        print(t)
        data={
            'total':'total',
            'per':'per',
            'grade':'grade'
        }

    return render(request,'sheet.html')
