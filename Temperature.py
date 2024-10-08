# 온도값을 바탕으로 선풍기를 ON/OFF 하는 Temperature.py
import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import busio


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 점등을 위한 전역 변수 선언 및 초기화
led1 = 6 # 선풍기가 작동중임을 의미
led2 = 23 # 선풍기 ON 상태
GPIO.setup(led1, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
GPIO.setup(led2, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.


def controlLED(led, onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
        GPIO.output(led, onOff)

sda = 2 # GPIO 핀 번호, sda라고 이름이 보이는 핀
scl = 3 # GPIO 핀 번호, scl이라고 이름이 보이는 핀
i2c = busio.I2C(scl, sda)
tp = 13
GPIO.setup(tp,GPIO.OUT)
sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴
tpOnoff = 0
count=0

def getTemperature() :
        return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기


def tempOnoff(tp, tpOnoff):
        GPIO.output(tp,tpOnoff)
tempOnoff(tp,tpOnoff)
def controlTemp(temp, high, low): # 온도를 바탕으로 ON/OFF를 조절하는 함수
        global tpOnoff
        print("현재 온도는 %.2f도 입니다" % temp)
        print("%d" % tpOnoff)
        if (temp >= high  and tpOnoff == 0): # 온도가 28도 이상이고 선풍기가 OFF일때
                tpOnoff = 1
                tempOnoff(tp, tpOnoff) # 선풍기 on
                controlLED(led2,tpOnoff)
                print("현재 온오프는 %d " % tpOnoff)
        elif (temp < low and tpOnoff == 1): # 온도가 24도 아래이고 선풍기가 ON일때
                tpOnoff = 0
                tempOnoff(tp, tpOnoff) # 선풍기 off
                controlLED(led2,tpOnoff)
                print("현재 온오프는 %d" % tpOnoff)
        else:
                tempOnoff(tp,tpOnoff)

