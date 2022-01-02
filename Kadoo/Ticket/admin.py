from django.contrib import admin
from django.forms.widgets import Textarea

from Ticket.models import ConversationModel, TicketModel, SupportTicketModel

class TicketAdminConfig(admin.ModelAdmin):
    model = TicketModel
    search_fields = ('author', 'Category', 'body', 'priority', 'created', 'modified')
    list_filter = ('author', 'Category', 'body', 'priority', 'created', 'modified')
    ordering = ('-created',)
    list_display = ('author', 'Category', 'body', 'priority', 'created', 'modified')
    fieldsets = (
        (None, {'fields': ('author', 'Category', 'priority')}),
        ('Personal', {'fields': ('body',)}),
    )
    formfield_overrides = {
         TicketModel.body: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('author', 'Category', 'body', 'priority', 'created', 'modified')}
         ),
    )


class SupportTicketAdminConfig(admin.ModelAdmin):
    model = SupportTicketModel
    search_fields = ('ticket_author', 'ticket_specialist', 'ticket_status', 'Category', 'body', 'created', 'modified')
    list_filter = ('ticket_author', 'ticket_specialist', 'ticket_status', 'Category', 'body', 'created', 'modified')
    ordering = ('-created',)
    list_display = ('ticket_author', 'ticket_specialist', 'ticket_status', 'Category', 'body', 'created', 'modified')
    fieldsets = (
        (None, {'fields': ('ticket_author', 'ticket_specialist', 'ticket_status', 'Category')}),
        ('Personal', {'fields': ('body',)}),
    )
    formfield_overrides = {
         TicketModel.body: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('ticket_author', 'ticket_specialist', 'ticket_status', 'Category', 'body', 'created', 'modified')}
         ),
    )

class ConversationAdminConfig(admin.ModelAdmin):
    model = ConversationModel
    search_fields = ('specialist', 'member', 'question_tickect', 'answer_tickect', 'rate', 'created', 'done')
    list_filter = ('specialist', 'member', 'question_tickect', 'answer_tickect', 'rate', 'created', 'done')
    ordering = ('-created',)
    list_display = ('specialist', 'member', 'rate', 'created', 'done')
    fieldsets = (
        (None, {'fields': ('specialist', 'member', 'question_tickect', 'answer_tickect', 'rate', 'done')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('specialist', 'member', 'question_tickect', 'answer_tickect', 'rate', 'created', 'done')}
         ),
    )

admin.site.register({TicketModel}, TicketAdminConfig)
admin.site.register({ConversationModel}, ConversationAdminConfig)
admin.site.register({SupportTicketModel}, SupportTicketAdminConfig)
