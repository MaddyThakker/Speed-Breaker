import os
import time

os.system("octave number_plate_det.m")

#os.system("number_plate_det")
#os.system("cd /home/pi/Downloads/asd/Vehicle number plate recognition/")
os.system("tesseract output11.jpg /home/pi/Downloads/asd/Vehicle/input11")
os.system("tesseract output21.jpg /home/pi/Downloads/asd/Vehicle/input21")
os.system("tesseract output12.jpg /home/pi/Downloads/asd/Vehicle/input12")
os.system("tesseract output22.jpg /home/pi/Downloads/asd/Vehicle/input22")
os.system("tesseract output11b.jpg /home/pi/Downloads/asd/Vehicle/input11b")
os.system("tesseract output21b.jpg /home/pi/Downloads/asd/Vehicle/input21b")
os.system("tesseract output12b.jpg /home/pi/Downloads/asd/Vehicle/input12b")
os.system("tesseract output22b.jpg /home/pi/Downloads/asd/Vehicle/input22b")


a=[]
f1=open("/home/pi/Downloads/asd/Vehicle/input11.txt",'r')
f2=open("/home/pi/Downloads/asd/Vehicle/input21.txt",'r')
f3=open("/home/pi/Downloads/asd/Vehicle/input12.txt",'r')
f4=open("/home/pi/Downloads/asd/Vehicle/input22.txt",'r')
f5=open("/home/pi/Downloads/asd/Vehicle/input11b.txt",'r')
f6=open("/home/pi/Downloads/asd/Vehicle/input21b.txt",'r')
f7=open("/home/pi/Downloads/asd/Vehicle/input12b.txt",'r')
f8=open("/home/pi/Downloads/asd/Vehicle/input22b.txt",'r')

for i in f1:
    s=i.strip("\n")
    a.append(s)
    
for i in f2:
    s=i.strip("\n")
    a.append(s)
    
for i in f3:
    s=i.strip("\n")
    a.append(s)
    
for i in f4:
    s=i.strip("\n")
    a.append(s)

for i in f5:
    s=i.strip("\n")
    a.append(s)
    
for i in f6:
    s=i.strip("\n")
    a.append(s)
    
for i in f7:
    s=i.strip("\n")
    a.append(s)
    
for i in f8:
    s=i.strip("\n")
    a.append(s)

max=0
for i in range(1,len(a)):
    temp=len(a[i])
    if(temp>len(a[max]) and len(a[i])<=11):
        max=i

f9=open("/home/pi/Downloads/asd/Vehicle/output.txt",'w')
f9.write(a[max])

f10=open("/var/www/html/output.txt",'w')
f10.write(a[max])

os.system("cp image1.jpg /var/www/html/")
os.system("cp image2.jpg /var/www/html/")
os.system("cp output11.jpg /var/www/html/")
os.system("cp output21.jpg /var/www/html/")
os.system("cp output12.jpg /var/www/html/")
os.system("cp output22.jpg /var/www/html/")
os.system("cp output11b.jpg /var/www/html/")
os.system("cp output21b.jpg /var/www/html/")
os.system("cp output12b.jpg /var/www/html/")
os.system("cp output22b.jpg /var/www/html/")
