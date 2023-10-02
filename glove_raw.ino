int glove1;

unsigned long p_millis = 0;
unsigned long interval = 6600;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  //analogReference(EXTERNAL);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int glove1= analogRead(A0);
  int glove2= analogRead(A1);
  int glove3= analogRead(A2);
  int glove4= analogRead(A3);
  int glove5= analogRead(A5);

  
  //delay(64);

  
//  int valA= map(glove1,802,895,0,100);
//  int valB= map(glove2,595,802,0,100);
//  int valC= map(glove3,597,756,0,100);
//  int valD= map(glove4,800,869,0,100);
//  int valE= map(glove5,683,847,0,100);
//  Serial.print(0);
//  Serial.print(" ");
//  Serial.print(1024);
//  Serial.print(" ");
  
//  Serial.println((String) ""+ glove1+"");
  Serial.println((String) ""+ glove1+","+ glove2+","+ glove3+","+ glove4+","+ glove5+"");
//  Serial.println((String) ""+ glove1+","+ glove2+","+ glove3+","+ glove4+"");
  //Serial.println( (String) ""+ glove4+"" );
  delay(4);
  //unsigned long now_millis = millis();
  //if ((now_millis - p_millis < interval)){
  //  Serial.println( (String) ""+ glove1+"" );
  //}
}
