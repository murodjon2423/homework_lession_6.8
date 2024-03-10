from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexen(request):
    return HttpResponse("<table border='1'><tr><td>Weekday</td></tr><tr><td>Sunday</td></tr><tr><td>Monday</td></tr><tr><td>Tuesday</td></tr><tr><td>Wednesday</td></tr><tr><td>Thursday</td></tr><tr><td>Friday</td></tr><tr><td>Saturday</td></tr></table>")

def indexuz(request):
    return HttpResponse("<table border='1'><tr><td>Hafta kunlari</td></tr><tr><td>yakshanba</td></tr><tr><td>dushanba</td></tr><tr><td>seshanba</td></tr><tr><td>chorshanba</td></tr><tr><td>Payshanba</td></tr><tr><td>Juma</td></tr><tr><td>shanba</td></tr></table>")

def indexru(request):
    return HttpResponse("<table border='1'><tr><td>дни недели</td></tr><tr><td>Понедельник</td></tr><tr><td>Вторник</td></tr><tr><td>Среда</td></tr><tr><td>Четверг</td></tr><tr><td>Пятница</td></tr><tr><td>Суббота</td></tr><tr><td>Воскресенье</td></tr></table>")

def index(request):
    return HttpResponse("<table border='1'><tr><td>Weekday</td></tr><tr><td>Sunday</td></tr><tr><td>Monday</td></tr><tr><td>Tuesday</td></tr><tr><td>Wednesday</td></tr><tr><td>Thursday</td></tr><tr><td>Friday</td></tr><tr><td>Saturday</td></tr></table><br><table border='1'><tr><td>Hafta kunlari</td></tr><tr><td>yakshanba</td></tr><tr><td>dushanba</td></tr><tr><td>seshanba</td></tr><tr><td>chorshanba</td></tr><tr><td>Payshanba</td></tr><tr><td>Juma</td></tr><tr><td>shanba</td></tr></table><br><table border='1'><tr><td>дни недели</td></tr><tr><td>Понедельник</td></tr><tr><td>Вторник</td></tr><tr><td>Среда</td></tr><tr><td>Четверг</td></tr><tr><td>Пятница</td></tr><tr><td>Суббота</td></tr><tr><td>Воскресенье</td></tr></table>")


