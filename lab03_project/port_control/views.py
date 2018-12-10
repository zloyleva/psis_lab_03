from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


# Create your views here.

@api_view(['GET'])
def set_pin(request, pk=None):
    if request.method == 'GET':
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        arr = [7,8,18,16,15,13,12,11]

        for i in arr:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, True)
            time.sleep(0.1)
        for i in arr:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
            time.sleep(0.1)
        return Response({"pin": pk})
