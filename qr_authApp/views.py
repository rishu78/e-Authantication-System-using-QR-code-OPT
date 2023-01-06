from django.shortcuts import render
import random
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

otp = 0


def openLoginPage(request):
    return render(request, "login.html")


def validateuser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "rishabh782818@gmail.com" and password == "Rishabh@54321":
        rno = random.randint(100000, 999999)
        global otp
        otp = rno
        im = qrcode.make("OTP : "+str(rno))
        im.save(r"qr_authApp/static/qrimages/rishabh.jpg")
        return render(request, "qrcode_page.html")

    else:
        return render(request, "login.html", {"message": "Invalid user"})


def validateOTP(request):
    user_otp = request.POST.get("otp")
    if user_otp == str(otp):
        return render(request, "welcome.html")
    else:
        return render(request, "login.html", {"message": "Invalid OTP"})

    return None

