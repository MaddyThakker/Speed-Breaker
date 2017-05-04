 #include <SoftwareSerial.h>
 #include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);
//10->Rx
//9->Tx
int i=0;
int k=0;
SoftwareSerial mySerial(9,10);
char msg;
void setup()
{
  Serial.println("YO");
  lcd.begin(16, 2);
  lcd.print("ATTENTION");
  lcd.setCursor(0, 1);
  lcd.print("READ THE MESSAGE");
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  delay(100);
  mySerial.println("AT+CMGF=1\r");
  delay(100);
  mySerial.println("AT+CNMI=2,2,0,0,0"); // AT Command to receive a live SMS
  delay(100);
  lcd.clear();
}


void loop()
{
 if (mySerial.available()>0)
 {
  i++;
  msg=mySerial.read();
  Serial.print(i);
  Serial.println(msg);
  //Serial.println(msg);

//    if(msg=="1" || msg=="2" || msg=="3" || msg=="4" || msg=="5" || msg=="6" || msg=="7" || msg=="8" || msg=="9" || msg=="0"){
    if(i>51 && i<62){
    lcd.setCursor(k,0);
    lcd.print(msg);
  // Serial.println(msg);
   k++;}
  }
}
