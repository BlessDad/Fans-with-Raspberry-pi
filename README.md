# 1. 시스템 구조

<img width="618" alt="image" src="https://github.com/user-attachments/assets/26a42774-2ad4-4ece-8425-717396d5b414">


일반 선풍기와 라즈베리 파이가 연결되어 있습니다. 

선풍기는 사용자가 설정한 온도에따라 제어되고, 사용자는 웹 페이지를 통해 간편하게 온도를 조절할 수 있습니다. 

제어를하는 과정에서 MQTT의 토픽 기능을 활용하였습니다.

LED를 활용하여 선풍기가 전원 여부를 추가로 확인할 수 있고,

아직 꺼질 온도가 아니어도 사용자가 임의로 끄고 싶을 시 간편하게 끌 수 있게 

초음파 센서를 활용하여 손을 라즈베리 파이에 가까이 뻗을 시 선풍기의 전원이 꺼지도록 했습니다. 

마지막으로 차트 기능을 넣어 실시간으로 온도를 확인할 수 있게 했습니다.

# 2. 하드웨어

<img width="576" alt="image" src="https://github.com/user-attachments/assets/e3772f3e-cd03-40d8-9d63-5b079eaf0b1e">




# 3. 소프트웨어

(1) FanApp.py

Flask를 활용하여 웹을 구축해주는 앱입니다.

(2) Temperature.py

온도를 바탕으로 하여 선풍기를 ON/OFF 하는 앱입니다.

(3) SmartFanMQTT.py

GPIO, Temperature.py, MQTT 등을 직접적으로 이용하여 실질적으로 선풍기를 제어하는
앱입니다.

(4) SmartFan.html

실질적으로 사용자가 직접 제어할 수 있는 웹페이지 html 입니다.
Mqtt publish와 subscribe를 적절하게 활용했습니다.

(5) mqttio3.js

웹 페이지 상에서 실제 기능이 동작하는 함수를 담은 스크립트 파일입니다.

# 4. 시연

(1) 웹 페이지:

<img width="577" alt="image" src="https://github.com/user-attachments/assets/60915413-febc-41b5-89d0-618099ae77d3">
<img width="608" alt="image" src="https://github.com/user-attachments/assets/940809bf-fbca-49f0-a5da-36fbca35b93a">

처음으로는 라즈베리파이 IP를 통해 접속할 수 있는 창이 있고, 아래로는 특정 온도 이상에서 켜지도록 만드는 상한온도와


특정 온도 아래에서 꺼지도록 만드는 하한온도 설정 칸이 있습니다.

그 밑으로는 LED 사용 유무를 설정하는 칸이 있고, 자동 꺼짐 거리에 대한 안내가 있습니다.

마지막으로는 온도 변화를 그래프로 표시해주는 차트가 있습니다.

(2) 하드웨어: 

<img width="449" alt="image" src="https://github.com/user-attachments/assets/86edb833-405a-4849-8e35-0203eae98b78">


라즈베리파이와 연결된 선풍기가 웹페이지 상의 온도 설정에 따라 ON/OFF가 이루어집니다.
릴레이 스위치 덕분에 5V DC 로 220V AC를 컨트롤할 수 있습니다.

(3) 시연 영상:

https://youtu.be/zC_Wbp0-T7k
