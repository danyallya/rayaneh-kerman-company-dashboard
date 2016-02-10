# -*- coding:utf-8 -*-
import threading
from urllib import request

from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives

# from account.models import Profile
from django.template.defaultfilters import linebreaksbr

__author__ = 'M.Y'


class MessageServices(threading.Thread):
    from_email = u'prkgroup.ir@gmail.com'
    admin_email = u'prkgroup.ir@gmail.com'

    @staticmethod
    def send_forget_password(email):
        try:
            user = Profile.objects.get(email=email)
            user.create_code()

            url = settings.SITE_URL + "/change_pass/?c=" + request.quote(user.code)
            message = u"""
                <div style="direction:rtl;font-family:tahoma;font-size:17px;">
                باسلام
                <br/>
شما درخواست فراموشی گذرواژه را ارسال کرده اید.
    <br/>
    با استفاده از لینک زیر می توانید گذرواژه جدید خود را دریافت نمایید.
                    <br/><br/>
                    <br/>
                    <a href="%s">%s</a>

                    <br/>
                    <br/>
                    <br/>
                    موفق باشید
                </div>
                """ % (url, url)
            msg = EmailMultiAlternatives(subject=u"تغییر گذرواژه در منظوم", body='',
                                         from_email=MessageServices.from_email,
                                         to=[user.email])
            msg.attach_alternative(message, "text/html")
            msg.send()
        except Exception as s:
            print(s)


messa = """
<div id="yui_3_16_0_1_1431180077709_2045">
    <div style="width:100%;min-height:100%;margin:0;padding:0;background-color:#e1e1e1;font-family:'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:300;"
         id="yui_3_16_0_1_1431180077709_2062">
        <table bgcolor="" cellpadding="0" cellspacing="0"
               style="border-top:5px solid #464646;background:#fff;max-width:600px;margin:0 auto;" width="100%"
               id="yui_3_16_0_1_1431180077709_2218">
            <tbody id="yui_3_16_0_1_1431180077709_2221">
            <tr id="yui_3_16_0_1_1431180077709_2220">
                <td style="display:block;max-width:600px;margin:0 auto;clear:both;padding:0 0 10px;text-align:center;font-family:tahoma;font-size:12px;margin-top:10px;"
                    id="yui_3_16_0_1_1431180077709_2219">
                    <a rel="nofollow" target="_blank">
                        نرم افزار اندروید ححاج احمد امینی
                    </a></td>
            </tr>
            </tbody>
        </table>



        <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tbody>
            <tr>
                <td bgcolor="#ffffff"
                    style="background:#ffffff;color:#ffffff;display:block;line-height:20px;font-weight:300;max-width:600px;margin:0 auto;clear:both;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0"
                           style="font-family:Arial, serif;font-size:12px;font-weight:300;border-bottom-width:1px;text-align:center;"
                           width="100%">
                        <tbody>
                        <tr>
                            <td width="100%">
                                <a rel="nofollow"> </a>

                                <img src="http://parkgroup.ir/amini/images/avatar.png">


                                <a rel="nofollow">

                            </a></td>
                        </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
            </tbody>
        </table>
        <table cellpadding="0" cellspacing="0" style="border-top:5px solid #EF3F3E;max-width:600px;margin:0 auto;"
               width="100%" id="yui_3_16_0_1_1431180077709_2061">
            <tbody id="yui_3_16_0_1_1431180077709_2060">
            <tr id="yui_3_16_0_1_1431180077709_2059">
                <td bgcolor="orange" style="display:block;max-width:100%;margin:0 auto;clear:both;"
                    id="yui_3_16_0_1_1431180077709_2058">
                    <div style="padding:10px;max-width:600px;margin:0 auto;display:block;text-align:center;"
                         id="yui_3_16_0_1_1431180077709_2057">


                        <font color="black" face="tahoma" size="-1">ایمیل:</font><br>
                        <font color="black">prkgroup.ir@gmial.com</font><br>
                        <a rel="nofollow" target="_blank"
                           href="http://click.icptrack.com/icp/relay.php?r=1955680&amp;msgid=65830&amp;act=Z3I7&amp;c=1525176&amp;destination=http%3A%2F%2Fwww.facebook.com%2FDigikalaPortal"
                           style="text-decoration:none;display:inline-block;"><br>
                            <img alt="" class="yiv1985941497CToWUd"
                                 style="border:none;color:#818181;font-size:9px;display:block;width:35px;"> </a> <a
                            rel="nofollow" target="_blank"
                            href="http://click.icptrack.com/icp/relay.php?r=1955680&amp;msgid=65830&amp;act=Z3I7&amp;c=1525176&amp;destination=http%3A%2F%2Fwww.twitter.com%2FDigikalacom"
                            style="text-decoration:none;display:inline-block;" id="yui_3_16_0_1_1431180077709_2063"><br>
                        <img alt="" class="yiv1985941497CToWUd"
                             style="border:none;color:#818181;font-size:9px;display:block;width:35px;"> </a> <a
                            rel="nofollow" target="_blank"
                            href="http://click.icptrack.com/icp/relay.php?r=1955680&amp;ms
parkgroup.ir/amini/images/avatar.png

9:46:35 AM
gid=65830&amp;act=Z3I7&amp;c=1525176&amp;destination=https%3A%2F%2Fplus.google.com%2F107060095312678131486%2Fposts"
                            style="text-decoration:none;display:inline-block;"><br>
                        <img alt="" class="yiv1985941497CToWUd"
                             style="border:none;color:#818181;font-size:9px;display:block;width:35px;"> </a> <a
                            rel="nofollow" target="_blank"
                            href="http://click.icptrack.com/icp/relay.php?r=1955680&amp;msgid=65830&amp;act=Z3I7&amp;c=1525176&amp;destination=http%3A%2F%2Fwww.instagram.com%2Fdigikalacom"
                            style="text-decoration:none;display:inline-block;"><br>
                        <img alt="" class="yiv1985941497CToWUd"
                             style="border:none;color:#818181;font-size:9px;display:block;width:35px;"> </a></div>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
    <p id="yui_3_16_0_1_1431180077709_2056">
        &nbsp;</p>
</div>"""


class ContactEmail(threading.Thread):
    def __init__(self, name, email, title, text):
        threading.Thread.__init__(self)
        self.text = text
        self.title = title
        self.email = email
        self.name = name

    def run(self):
        try:
            message = u"""
                    <div style="direction:rtl;font-family:tahoma;font-size:17px;">
                    نام : %s
                    <br/>

                    ایمیل: %s

                    <br/>

                    عنوان : %s

                    <br/>

                    متن:
                    <br/>
                    %s


                    </div>
                    """ % (self.name, self.email, self.title, linebreaksbr(self.text))
            msg = EmailMultiAlternatives(subject=u"ارتباط با ما PRK", body='',
                                         from_email=MessageServices.from_email,
                                         to=['mymy47@gmail.com'])
            msg.attach_alternative(message, "text/html")
            msg.send()

        except Exception as e:
            print(e)
            pass
