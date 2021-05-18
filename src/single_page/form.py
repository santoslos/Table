from django import forms
from single_page.models import Table


class TableForm(forms.Form):
    names_field = [f.name for f in Table._meta.get_fields() if f.name not in ['date', 'id']]

    verbose_name = [f.verbose_name for f in Table._meta.get_fields() if f.name not in ['date', 'id']]
    choices_fields = zip(names_field, verbose_name)
    order_field = forms.ChoiceField(label='Имя столбца для сортировки', choices=choices_fields,
                                    widget=forms.Select(
                                        attrs={'class': 'form-select'}
                                    ))

    names_field = [f.name for f in Table._meta.get_fields() if f.name not in ['date', 'id']]

    verbose_name = [f.verbose_name for f in Table._meta.get_fields() if f.name not in ['date', 'id']]
    choices_fields = zip(names_field, verbose_name)
    name_field = forms.ChoiceField(label='Имя столбца для фильтрации', choices=choices_fields,
                                   widget=forms.Select(
                                       attrs={'class': 'form-select'}
                                   ))
    choice_filter = (('1', 'Меньше'), ('2', 'Больше'), ('3', 'Равно'),)
    filter = forms.ChoiceField(label='Имя фильтра', choices=(choice_filter),
                               widget=forms.Select(
                                   attrs={'class': 'form-select'}
                               ))
