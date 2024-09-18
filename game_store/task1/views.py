from django.shortcuts import render
from .models import Game

def games_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games.html', context)
def platform_view(request):
    return render(request, 'fourth_task/platform.html')

def cart_view(request):
    return render(request, 'fourth_task/cart.html')

from django.shortcuts import render
from .forms import UserRegister

def sign_up_by_django(request):
    users = ['Vasya', 'admin', 'user123']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    # Этот метод может использовать обычную HTML форму, если вы не хотите использовать Django формы

    users = ['Vasya', 'admin', 'user123']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)

