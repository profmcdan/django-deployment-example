from django.shortcuts import render
# from django.http import HttpResponse
from proTwo.models import User
from proTwo.forms import NewUserForm

# Create your views here.

def index(request):
    # return HttpResponse("Hi Project 2")
    my_data = {'edit_me': 'Its good to code from Django'}
    return render(request, 'proTwo/index.html', context=my_data)

def help(request):
    page_data = {'local_data': 'Help Page!'}
    return render(request, 'proTwo/help.html', context=page_data)

def user2(request):
    user_dict = {'user_records': User.objects.order_by('firstname')}
    return render(request, 'proTwo/users.html', context=user_dict)

def user(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True) # Save to DB
            return index(request) # Retun to tyhe index page

        else:
            print('An ERROR!')

    return render(request, 'proTwo/users.html', {'form': form})
