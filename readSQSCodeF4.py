import boto3
from escpos.printer import Usb
import time
import json
crFile = "/media/pi/RAO/data/credentials.json" # Address of Json file in USB drive

########################################INITIALIZE CONNECTION TO AWS VIA BOTO3 'CLIENT'#############################################
with open(crFile, "r") as readFile:
    data =  json.load(readFile)
    readFile.close()
    access_key = data["data"]["access_key"]
    secret_key = data["data"]["secret_key"]
    region =data["data"]["region"]
    arn = data["data"]["arn"]
client = boto3.resource('sqs',aws_access_key_id=access_key,
    aws_secret_access_key=secret_key, region_name=region)

queName="PiQueue"
accthttp=arn
LastTime = time.time()
###INPUT THE IAM CREDENTIALS WITH PERMISSIONS TO THE AWS ACCOUNT AND RESOURCE YOU'RE TRYING TO ACCESS.

p = Usb(0x0456,0x0808,0, 0x82,0x03) ##### 0x0456, is vender ID, 0x0808 is product ID and 0x03 is the Device ID change as per yours

while True:
    timeNow = time.time()
    time.sleep(1)
    if (timeNow - LastTime) >= 3:
        LastTime =  time.time()
        print("Requesting Queue")
        url = accthttp+str(queName)
        receipt = client.Queue(url=url).receive_messages()

# print(receipt)
        for message in receipt:
            print(message.body)
            p.text(message.body)
#             p.barcode('1452349857687','EAN13',64,3,'','')
            p.cut()
#             print(message)
            message.delete(QueueUrl=url, ReceiptHandle=message.receipt_handle)
            print("this message has been deleted.")
