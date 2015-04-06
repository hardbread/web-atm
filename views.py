from django.shortcuts import redirect


def logout(request):
    request.session.pop('card_id', None)
    request.session.pop('attempts', None)
    request.session.pop('is_authorized', None)
    return redirect('index')