int leftLed = 11;
int midLed = 12;
int rightLed = 13;
char input = ' ';
void setup(){
  
  pinMode(leftLed,OUTPUT);
  pinMode(midLed,OUTPUT);
  pinMode(rightLed,OUTPUT); 
  Serial.begin(115200);
  Serial.println("Starting");
  
  
  
  while(true){  
    char temp = Serial.read();
    if(temp != -1)
    {
       input = temp;
       Serial.println(input);    
    }
    
    // Left Turn
    if(input == 'L')
    {
        //Simulate
        digitalWrite(leftLed,HIGH); 
        delay(300);
        digitalWrite(leftLed,LOW);
        //Code here
        input = ' ';   
    }
     // Right Turn 
    if(input == 'R')
    {
      //Simulate
        digitalWrite(rightLed,HIGH);
        delay(300); 
        digitalWrite(rightLed,LOW);
        //Code here
        input = ' ';     
    }
    
    //Go Straight
    if(input == 'S')
    {
      //Simulate
       digitalWrite(midLed,HIGH); 
       delay(300); 
       digitalWrite(midLed,LOW);
      //Code here 
       input = ' ';
    }
    //Go Backwards
    if(input == 'B')
    {
       //Code here 
       input = ' ';
    }
    //Calibrate
    if(input == 'C')
    {
        Calibrate();
    }
   
    delay(300);
  }
}

void loop(){
  
}
void Calibrate(){
  digitalWrite(leftLed,HIGH); 
  delay(100);  
  digitalWrite(midLed,HIGH);  
  delay(100);
  digitalWrite(rightLed,HIGH);
  delay(100);
  digitalWrite(leftLed,LOW);
  digitalWrite(midLed,LOW);
  digitalWrite(rightLed,LOW);
}


