import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "g3qvmi"
deviceType = "raspberrypi"
deviceId = "09876543"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True: 
        
        age=random.randint(18,78)
        #print(age)
        temp=random.randint(35,40)
        #print(temp)
        sys=random.randint(100,150)
        #print(sys)
        dia=random.randint(60,100)
        #print(dia)
        pul=random.randint(10,180)
        #print(pul)
        #Send age,temperature,systolic,diastolic,pulse to IBM Watson
        data = {'age':age,'temperature':temp,'systolic':sys,'diastolic':dia,'pulse':pul}
        #print (data)
        def myOnPublishCallback():
            print ("Published age= %s %%" %age,"temperature = %s %%" % temp,"systolic= %s %%"%sys,"diastolic=%s %%"%dia,"pulse=%s %%"%pul, "to IBM Watson")

        success = deviceCli.publishEvent("Health", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
