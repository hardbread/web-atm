from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    context = {'msg': 'Card is unavailable', 'back_to': 'index'}
    response = render_to_response('error.html', context,
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def card_blocked_error(request):
    context = {'msg': 'Sorry, your card was blocked', 'back_to': 'logout'}
    response = render_to_response('error.html', context,
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def amount_more_balance_error(request):
    context = {'msg': 'Withdrawal amount more than balance', 'back_to': 'get_cash'}
    response = render_to_response('error.html', context,
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response