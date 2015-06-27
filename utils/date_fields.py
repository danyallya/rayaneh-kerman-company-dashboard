# -*- coding:utf-8 -*-
from django.utils.safestring import mark_safe

from utils.calendar import jalali_to_gregorian, gregorian_to_jalali


__author__ = 'M.Y'
from django import forms


class ShamsiWidget(forms.DateInput):
    def render(self, name, value, attrs=None):
        value = gregorian_to_jalali(value)
        html = super(ShamsiWidget, self).render(name, value, attrs)
        js = """
        <script type='text/javascript'>
            $('#id_%s').addClass('datepicker');
            $('#id_%s').datepicker({
                changeMonth: true,
                changeYear: true,
                yearRange:'-50:+50',
                dateFormat: 'yy/mm/dd'
            });
        </script>
        """ % (name, name)
        return mark_safe(u"%s %s" % (html, js))

    def value_from_datadict(self, data, files, name):
        shamsi_val = data.get(name, '')
        miladi_val = jalali_to_gregorian(shamsi_val)
        if miladi_val:
            return miladi_val.isoformat()
        else:
            return miladi_val


class ShamsiDateField(forms.DateField):
    widget = ShamsiWidget

    def to_python(self, value):
        return super(ShamsiDateField, self).to_python(value)
