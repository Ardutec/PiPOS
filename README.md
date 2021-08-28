# PiPOS
It is Raspberry pi based POS system which reads AWS SQS que and print on thermal printer
We need to configure the thermal printer to work with python code running on Raspberry Pi with Linux-based OS Rasbian buster installed. These are the quick instructions to set up a USB thermal printer.

## Setup for Thermal Printer SpeedX 200 Plus ###

Install Library: Install library in use with this command

```pip3 install python-escpos```

Connect the thermal printer with Raspberry pi and Run this command. 

```lsusb```

Note down vendor id, product id, and bus number from response

Create a file named "99-escpos.rules" at "/et/udev/rules.d" overall directory would be like this: /et/udev/rules.d/99-escpos.rules

Put this line in above file make sure vendor ID and product ID is updated that you have already noted down.
>SUBSYSTEM=="usb", ATTRS{idVendor}=="0456", ATTRS{idProduct}=="0808", MODE="0664", GROUP="dialout"

Run these commands to restart and reload the service. 

```
sudo service udev restart
sudo udevadm control --reload
```

Take a USB drive and save credentials.json file in that.
  Update the credentials as per your AWS account. 
  Copy the credentials.json file address.


Now open the python code file and update crFile address with the address you just copied. 
  Update the Que name in the Python file
  Update the vendor Id, product Id, and endpoint you have received from "lsusb" command. 


### Run the code, if everything goes well it will start working.
