from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    card = Card.objects.all()
    return render(request, 'site/home.html', {'card': card})

def index(request):
    user = request.user    
    card = Card.objects.all()
    top_cards = Card.most_liked()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            'top_cards': top_cards,
            }
        )
    return render(request, 'site/index.html', {'cards': data_card})

@login_required
def like_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    like, created = Like.objects.get_or_create(user=request.user, card=card)
    if not created:
        like.delete()
    return redirect('index')

@login_required
def create(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card cadastrado com sucesso!')
            return redirect('home')
    else:
        form = CardForm()
    return render(request, 'site/create.html', {'form': form})

@login_required
def edit(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card editado com sucesso!')
            return redirect('index')
    else:
        form = CardForm(instance=card)
    return render(request, "site/update.html",{"form":form, "card":card})

@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        card.delete()
        messages.success(request, 'Card deletado com sucesso!')
        return redirect('home')
    return render(request, 'site/delete.html', {'card': card})

def empreendedorismo(request):
    user = request.user    
    card = Card.objects.all()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/sections/empreendedorismo.html', {'cards': data_card})

def startUp(request):
    user = request.user    
    card = Card.objects.all()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/sections/startUp.html', {'cards': data_card})

def prototipo(request):
    user = request.user    
    card = Card.objects.all()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/sections/prototipo.html', {'cards': data_card})

def pitch(request):
    user = request.user    
    card = Card.objects.all()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/sections/pitch.html', {'cards': data_card})

def mentoria(request):
    user = request.user    
    card = Card.objects.all()
    data_card = []
    for cards in card:
        data_card.append(    
            {
            'cards': cards,
            'liked': cards.user_liked(user) if user.is_authenticated else False,
            }
        )
    return render(request, 'site/sections/mentoria.html', {'cards': data_card})

def resultados(request):
    return render(request, 'site/noticias.html')