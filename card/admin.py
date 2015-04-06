from django.contrib import admin
from card.forms import CardAdminForm
from card.models import Card, CardOperation


class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'is_active', 'balance')
    search_fields = ['card_id', 'balance']

    form = CardAdminForm


class CardOperationAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        'get_card', 'operation',
        'amount', 'operation_time'
    )

    search_fields = ['=card_id__card_id', ]
    fieldsets = [
        (None, {'fields': ()}),
    ]

    @staticmethod
    def get_card(obj):
        return obj.card_id

    def __init__(self, *args, **kwargs):
        super(CardOperationAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

admin.site.register(Card, CardAdmin)
admin.site.register(CardOperation, CardOperationAdmin)