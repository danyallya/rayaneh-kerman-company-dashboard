# -*- coding:utf-8 -*-
__author__ = 'M.Y'
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render



class ExcelFileForm(forms.Form):
    excel_file = forms.FileField(label=u"فایل اکسل")


@login_required
def user_inputs(request):
    if request.user.is_superuser:
#         if request.POST:
#             form = ExcelFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 stds = get_rows_from_excel_file(form.cleaned_data.get('excel_file'))
#                 updated_users = 0
#                 new_users = 0
#                 for std in stds:
#                     try:
#                         u = User.objects.get(username=std.std_num)
#                         u.first_name = std.name
#                         u.last_name = std.lname
#                         u.username = std.std_num
#                         u.email = std.email
#                         u.save()
#                         updated_users += 1
#                     except User.DoesNotExist:
#                         u = User()
#                         u.first_name = std.name
#                         u.last_name = std.lname
#                         u.username = std.std_num
#                         u.email = std.email
#                         u.set_password(std.nat_code)
#                         u.save()
#                         new_users += 1
#                         if std.dorm:
#                             profile = Profile.objects.create(user=u, description=std.dorm)
#
#                 messages.success(request, u"تعداد %s کاربر بروزرسانی شدند و %s کاربر به سیستم اضافه شدند." % (
#                     updated_users, new_users))
#                 form = None
#         else:
#             form = ExcelFileForm()
#
#         context = locals()
#         context.update({'title': u"ورود کاربران از اکسل"})
        return render(request, 'admin/user_inputs.html', {})
    else:
        raise Http404


def get_rows_from_excel_file(f):
    import xlrd
    # import os
    #
    # module_dir = os.path.dirname(__file__)  # get current directory
    # file_path = os.path.join(module_dir, 'poshiban.xlsx')
    #
    # f = open(file_path, 'rb')

    stds = []
    wb = xlrd.open_workbook(file_contents=f.read())
    sh = wb.sheet_by_index(0)
    for rownum in range(sh.nrows):
        try:
            row = sh.row_values(rownum)
            stds.append(Student(row[0], row[1], int(row[2]), row[3], int(row[4]), row[5]))
        except Exception as e:
            pass

    return stds


class Student:
    def __init__(self, name, lname, std_num, dorm, nat_code, email):
        self.email = email
        self.nat_code = nat_code
        self.dorm = dorm
        self.std_num = std_num
        self.lname = lname
        self.name = name
