int leftLed = 11;
int midLed = 12;
int rightLed = 13;
String input = NULL;
void setup(){
  
  pinMode(leftLed,OUTPUT);
  pinMode(midLed,OUTPUT);
  pinMode(rightLed,OUTPUT); 
  Serial.begin(9600);
  Serial.println("Starting");
  
  while(true){
    String tempStr = Serial.readString();
    if(tempStr != NULL)
    {
       input = tempStr;
       Serial.println(input[0]);    
    }
    
    // Left Turn
    if(input[0] == 'L')
    {
        digitalWrite(leftLed,HIGH); 
    }
    else
    {
      digitalWrite(leftLed,LOW); 
    }
    
    //Go Straight
    if(input[0] == 'U')
    {
        digitalWrite(midLed,HIGH);  
    }
    else
    {
      digitalWrite(midLed,LOW);  
    }
    
    // Right Turn 
    if(input[0] == 'R')
    {
        digitalWrite(rightLed,HIGH);     
    }
    else
    {
      digitalWrite(rightLed,LOW);  
    }
  }
}

void loop(){
  
}


