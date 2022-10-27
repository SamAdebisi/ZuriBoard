from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {
        'insert_content': "HELLO I'M FROM MUSICAPP!"
    }
    return render(request, 'musicapp/index.html', context=my_dict)

