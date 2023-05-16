from django.shortcuts import render

# Create your views here.
def index(request):
    mylist="mylist"
    return render(request,'baseapp/index.html')
# import webbrowser
# import pyautogui
# import time

# webbrowser.open('https://web.whatsapp.com/')

# time.sleep(10)

# person_name=input("Enter the person name whom you want to send a message")
# # print(pyautogui.position())
# pyautogui.click(184,189)
# pyautogui.typewrite(person_name)