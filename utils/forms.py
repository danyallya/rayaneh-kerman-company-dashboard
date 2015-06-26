# -*- coding:utf-8 -*-
from django import forms

__author__ = 'M.Y'


# def initial_dec(function):
#     def new_init(self, *args, **kwargs):
#         res = function(self, *args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})
#         return res
#
#     return new_init


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.provide_fields()

    def provide_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})