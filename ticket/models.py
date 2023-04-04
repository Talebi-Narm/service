from django.db import models

from common.models import BaseModel


class SpecialistTicket(BaseModel):
    category_quantifiers = (
        ('Pre-Sale Question', 'Pre-Sale Question'),
        ('Order Question', 'Order Question'),
        ('Return', 'Return'),
        ('Shipping', 'Shipping'),
        ('Product Availability', 'Product Availability'),
        ('Plant caring', 'Plant caring'),
        ('General', 'General'),
    )

    customer = models.ForeignKey('user.User', null=True, blank=True, on_delete=models.CASCADE)
    Category = models.CharField(max_length=50, choices=category_quantifiers, default='General', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    priority = models.IntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)


class SupportTicket(BaseModel):
    category_quantifiers = (
        ('Pre-Sale Question', 'Pre-Sale Question'),
        ('Order Question', 'Order Question'),
        ('Return', 'Return'),
        ('Shipping', 'Shipping'),
        ('Product Availability', 'Product Availability'),
        ('Plant caring', 'Plant caring'),
        ('General', 'General'),
    )

    status_quantifiers = (
        ('Sent', 'Sent'),
        ('In progress', 'In progress'),
        ('Accepted', 'Accepted'),
        ('Done', 'Done'),
    )

    ticket_author = models.ForeignKey('user.User', related_name="ticket_author", null=True, blank=True,
                                      on_delete=models.CASCADE)
    # ticket_specialist = models.ForeignKey('Specialist.Specialist', null = True, related_name="ticket_specialist", blank = True, on_delete = models.CASCADE)
    Category = models.CharField(max_length=50, choices=category_quantifiers, default='General', null=True, blank=True)
    ticket_status = models.CharField(max_length=50, choices=status_quantifiers, default='Sent', null=True, blank=True)
    rate = models.IntegerField(blank=True, default=0)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)

# class Conversation(BaseModel):
#     # specialist = models.ForeignKey('Specialist.Specialist', related_name="specialist", on_delete=models.CASCADE)
#     member = models.ForeignKey('user.User', related_name="member", on_delete=models.CASCADE)
#     question_tickect = models.ManyToManyField("TicketModel", related_name="question_tickect", blank=True)
#     answer_tickect = models.ManyToManyField("TicketModel", related_name="answer_tickect", blank=True)
#     rate = models.IntegerField(blank=True, default=0)
#     created = models.DateTimeField(auto_now_add=True)
#     done = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.id)