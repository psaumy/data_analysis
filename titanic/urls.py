from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from titanic.views import home, ticket_class_view, ticket_class_view_2, embarked_view, adr_view, readTable, bargraph

urlpatterns = [
    path('', view=home, name='chart'),
    path('ticket-class', view=ticket_class_view, name='ticket_class_view'),
    path('ticket-class-2', view=ticket_class_view_2, name='ticket_class_view_2'),
    path('embarked', view=embarked_view, name='embarked_view'),
    path('adr', view=adr_view, name='adr_view'),
    path('readTable', view=readTable, name='readTable'),
    path('bargraph', view=bargraph, name='bargraph'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)