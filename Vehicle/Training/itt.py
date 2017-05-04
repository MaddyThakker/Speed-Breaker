import os
import time

os.system("octave number_plate_det.m")

#os.system("number_plate_det")
#os.system("cd /home/pi/Downloads/asd/Vehicle number plate recognition/")
os.system("tesseract output11.jpg input11")
os.system("tesseract output21.jpg input21")
os.system("tesseract output12.jpg input12")
os.system("tesseract output22.jpg input22")

#os.system(
a=[]
f1=open("input11.txt",'r')
f2=open("input21.txt",'r')
f3=open("input12.txt",'r')
f4=open("input22.txt",'r')

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

max=0
for i in range(1,len(a)):
    temp=len(a[i])
    if(temp>len(a[max])):
        max=i

f5=open("output.txt",'w')
f5.write(a[max])

f6=open("/var/www/html/output.txt",'w')
f6.write(a[max])

os.system("cp image1.jpg /var/www/html/")
os.system("cp image2.jpg /var/www/html/")
os.system("cp output11.jpg /var/www/html/")
os.system("cp output21.jpg /var/www/html/")
os.system("cp output12.jpg /var/www/html/")
os.system("cp output22.jpg /var/www/html/")
