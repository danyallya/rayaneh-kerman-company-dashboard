# -*- coding:utf-8 -*-
from django import forms

from utils.calendar import gregorian_to_jalali
from utils.date_fields import ShamsiDateField


__author__ = 'M.Y'


# def initial_dec(function):
#     def new_init(self, *args, **kwargs):
#         res = function(self, *args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})
#         return res
#
#     return new_init


def handel_date_fields(form):
    for field in form.fields:
        if isinstance(form.fields[field], (forms.DateField, forms.DateTimeField)):
            old_field = form.fields[field]
            new_field = ShamsiDateField(label=old_field.label, required=old_field.required,
                                        initial=gregorian_to_jalali(old_field.initial))
            form.fields[field] = new_field


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        # self.provide_fields()
        handel_date_fields(self)

    def provide_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})