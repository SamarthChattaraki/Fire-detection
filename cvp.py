import cv2
from playsound  import playsound
 
fire_cascade = cv2.CascadeClassifier("fire_detection.xml")
cap =cv2.VideoCapture(0)
count = 0

while True:
    ret,frames =cap.read()
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frames,1.03,6)

    
    for x,y,w,h in fire:
        cv2.rectangle(frames,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),2)


        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frames[x:x+w,y:y+h]
        print("fire detected")
        
        count = count+1
        playsound("audio.mp3")
    if count >0:
        print("sent sms to your mobile apllication")
        from twilio.rest import Client

        account_sid = 'AC1351f5d31a87f241dfe739a0a4d4c343'
        auth_token = 'a284dde85f87780df20e41a1f50dcfcd'

        twilio_number = '+19289637445'
        my_phone_number = '+917259323346'

        client = Client(account_sid, auth_token)
        msg = "status: HII CLASS"
        message = client.messages.create(
        body=msg,
        from_=twilio_number,
        to=my_phone_number
	    )
        print(message.body)




    


    
    cv2.imshow("fire detected",frames)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()




