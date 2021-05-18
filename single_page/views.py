from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Table
# Create your views here.
from django.views.generic import ListView
from django.contrib import messages
from single_page.form import TableForm


class TableListView(ListView):
    template_name = 'single_page/page.html'
    context_object_name = 'objects'
    paginate_by = 4

    def get_queryset(self):
        name_field = self.request.GET.get('name_field')
        filter = self.request.GET.get('filter')
        value = self.request.GET.get('value')
        order_field = self.request.GET.get('order_field')
        fields = {}
        if filter and value and name_field:
            if filter == '3' and name_field == 'title':
                fields = {"%s__startswith" % (name_field): value}
            elif filter == '3' and name_field != 'title':
                fields = {name_field: value}
            elif filter == '1' and name_field != 'title':
                fields = {"%s__lt" % (name_field): value}
            elif filter == '2' and name_field != 'title':
                fields = {"%s__gt" % (name_field): value}
            else:
                messages.error(self.request, 'Меньше или больше не принемимо к полю "Заголовок"')
            if order_field:
                queryset = Table.objects.filter(**fields)
                queryset = queryset.order_by(f'{order_field}')
            else:
                queryset = Table.objects.filter(**fields)


        else:
            if order_field:
                queryset = Table.objects.all().order_by(f'{order_field}')
            else:
                queryset = Table.objects.filter(**fields)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TableForm(self.request.GET)
        reg = str(self.request)
        get_param = reg.partition('?')
        context['path'] = get_param[2][:-2]
        return context
