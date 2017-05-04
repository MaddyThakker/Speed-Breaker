# Speed-Breaker
As soon as an approaching car over speeds, image of number-plate is captured and the 
  following process takes place :
  Image processing using MATLAB.
  Further it removes all the surrounding elements considering only populated letters.
  By using Tesseract Optical Character Recognition on this image we get the number of the car. 
    The original image with the speed is uploaded to a server hosted on the R-Pi. Now, this 
    number is sent through a GSM module connected to the R-Pi to some security guards 
    on duty so that they can catch the over-speeding car. Further, another GSM module
    connected to an arduino, placed at the main gate, sounds a buzzer when the number       
    of the car is displayed notifying the guards of the over speeding car so that
    they can catch it when it leaves the campus.
    
    So, after connecting all the hardware -  
    Run the file- madhavldr.py
    As anycar overspeeds it will take the picture of the car's number plate.
    It will then run the file, image.py which will take 2 pics and will give you 8 pictures of car's number plate. It will also select the most accurate picture.
    Then, we send the message through, gsmfinalfinal.py and the recieved message is displayed on the Arduino.
    
    Arduino on the other hand recieves a message and displays the text through sketch_may02a.ino
    
    
    Details regarding image to text conversion -
    As an image is captured, a threshold value is set according to RGB values of any image. Then, the values above the threshold are marked white and below them are marked black. 
    In the next step, the alphabets which are close enough to cause problem for teseract are dropped.
    
    Same process is repeated with the white and black colours replaced for better accuracy.
