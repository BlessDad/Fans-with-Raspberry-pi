# publisher

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import Temperature

# 초음파 센서를 대한 전역 변수 선언 및 초기화
trig = 20
echo = 16
tp = 13
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
ghigh = 26
glow = 20
led1 = 6 # 스마트 선풍기 시스템 작동유무 체크
led2 = 23 # 선풍기가 돌아가는지 유무

def on_connect(client, userdata, flag, rc):
    # 연결된 순간에, 토픽들을 subscribe 해준다.
        client.subscribe("high", qos = 0) # 상한온도 high 토픽
        client.subscribe("low", qos = 0) # 하한온도 low 토픽
        client.subscribe("clock", qos = 0)  # 알람시간 clock 토픽
        client.subscribe("led", qos = 0)  # led onoff 토픽
        
def measureDistance():
        global trig, echo
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은시간후 0으로 떨어뜨려 falling edge를 만들기 위함
        GPIO.output(trig, False) # 신호 0 발생(falling 에지)

        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time() # 신호 1. 초음파 발생이 시작되었음을 알림
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() # 신호 0. 초음파 수신 완료를 알림

        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration      

def on_message(client, userdata, msg) : 
        global ghigh
        global glow
        if (msg.topic == "led"): # 만약 topic이 led 인경우
            msg = int(msg.payload)
            Temperature.controlLED(led1,msg)
            print(msg)
        elif (msg.topic == "high"):
            ghigh = int(msg.payload)
            print('상한온도 %d' % ghigh)
        elif (msg.topic == "low"):
            glow = int(msg.payload)
            print('하한온도 %d' % glow)

        else:
            return

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()

while(True):
        temp = Temperature.getTemperature()
        temp = round(temp,2)
        distance = measureDistance()
        client.publish("current", temp, qos=0)
        print('거리는' + str(distance))
        Temperature.controlTemp(temp, ghigh, glow)
        time.sleep(3)
        if (distance < 20.):
            print(str(distance))
            GPIO.output(tp,0)
            break
        
        

client.loop_stop()
client.disconnect()

