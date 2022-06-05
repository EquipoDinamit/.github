void setup()
{
 Serial.begin(9600);
}
 
void loop()
{
 int dato = analogRead(A0);
 
 if (dato > 100)
 {
 if (dato > 500 && dato < 520)
 Serial.println("1");
 else if (dato > 330 && dato < 350)
 Serial.println("2");
 else if (dato > 244 && dato < 264)
 Serial.println("3");
 else if (dato > 190 && dato < 210)
 Serial.println("4");
 else if (dato > 160 && dato < 180)
 Serial.println("13");  
 else if (dato > 140 && dato < 150)
 Serial.println("5");
 else if (dato > 110 && dato < 130)
 Serial.println("6");  

 delay(500);
 }
}
