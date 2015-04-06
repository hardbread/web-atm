from django.shortcuts import render, get_object_or_404, redirect
from card.forms import CardInputForm, CardPinInputForm, GetCashInputForm
from card.models import Card, CardOperation
from error_handlers import card_blocked_error, amount_more_balance_error
from decimal import Decimal
from helpers import is_auth, auth_required
import settings


@is_auth
def index(request):
    if request.method == 'POST':
        form = CardInputForm(request.POST)
        if get_object_or_404(Card, card_id=request.POST['card_id'], is_active=True):
            request.session['card_id'] = request.POST['card_id']
            return redirect('pin_code')
    else:
        form = CardInputForm()
    return render(request, 'index.html', {'form': form})


@is_auth
def pin_code(request):
    if not request.session.get('card_id', False):
        return redirect('index')
    if request.method == 'POST':
        card_id = request.session['card_id']
        if Card.objects.filter(card_id=card_id, pin=request.POST['pin'], is_active=True).count():
            request.session.pop('attempts', None)
            request.session['is_authorized'] = True
            return redirect('operations')
        if request.session.get('attempts', 1) >= settings.PIN_ATTEMPTS:
            card = Card.objects.get(card_id=card_id)
            card.is_active = False
            card.save()
            return card_blocked_error(request)
        request.session['attempts'] = request.session.get('attempts', 1) + 1
        form = CardPinInputForm()
    else:
        form = CardPinInputForm()
    return render(request, 'pin_code.html', {'form': form})


@auth_required
def operations(request):
    return render(request, 'operations.html')


@auth_required
def get_cash(request):
    if request.method == 'POST':
        card_id = request.session['card_id']
        card = Card.objects.get(card_id=card_id, is_active=True)
        amount = Decimal(request.POST['amount'])
        if amount > card.balance:
            return amount_more_balance_error(request)
        residue = card.balance - amount
        card.balance = residue
        card.save()
        operation = CardOperation(card=card, amount=amount)
        operation.operation = 'withdrawal'
        operation.save()
        return render(request, 'report.html', {'operation': operation,
                                               'card': card,
                                               'back_to': 'operations'})
    else:
        form = GetCashInputForm()
    return render(request, 'get_cash.html', {'form': form})


@auth_required
def get_balance(request):
    card_id = request.session['card_id']
    card = Card.objects.get(card_id=card_id, is_active=True)
    operation = CardOperation(card=card)
    operation.operation = 'balance'
    operation.save()
    return render(request, 'report.html', {'operation': operation,
                                           'card': card,
                                           'back_to': 'operations'})