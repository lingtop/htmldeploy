#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

// K3 Connecter
// Pin Digit 4 bit
#define P1 12
#define P142 14
#define P140 27
#define P138 26
// Pin Ten 4 bit
#define P134 4
#define P132 16
#define P127 17
#define P124 5


//float to int
int celsius = 0;



DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  Serial.println("DHTxx test!");
  pinMode(P1, OUTPUT);
  pinMode(P142, OUTPUT);
  pinMode(P140, OUTPUT);
  pinMode(P138, OUTPUT);
  pinMode(P134, OUTPUT);
  pinMode(P132, OUTPUT);
  pinMode(P127, OUTPUT);
  pinMode(P124, OUTPUT);
  dht.begin();

}


int celsius_digit(int d, int c, int b, int a) {
  //digit 0000 0
  digitalWrite(P1, a);   //bit1
  digitalWrite(P142, b); //bit2
  digitalWrite(P140, c); //bit3
  digitalWrite(P138, d); //bit4
}

int celsius_ten(int d, int c, int b, int a) {
  //ten  0010 2
  digitalWrite(P134, a); //bit5
  digitalWrite(P132, b); //bit6
  digitalWrite(P127, c); //bit7
  digitalWrite(P124, d); //bit8
}

void loop() {
  delay(2000);
  float t = dht.readTemperature();
  Serial.println(t);
  Serial.println("-");
  Serial.println(celsius);
  Serial.println(F("°C "));
  celsius = t;

  if (celsius == 20) {
    //digit 0000 0
    celsius_digit(0, 0, 0, 0);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }

  else  if (celsius == 21) {
    //digit 0001 1
    celsius_digit(0, 0, 0, 1);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }

  else  if (celsius == 22) {
    //digit 0010 2
    celsius_digit(0, 0, 1, 0);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 23) {
    //digit 0011 3
    celsius_digit(0, 0, 1, 1);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 24) {
    //digit 0100 4
    celsius_digit(0, 1, 0, 0);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 25) {
    //digit 0101 5
    celsius_digit(0, 1, 0, 1);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 26) {
    //digit 0110 6
    celsius_digit(0, 1, 1, 0);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 27) {
    //digit 0111 7
    celsius_digit(0, 1, 1, 1);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 28) {
    //digit 1000 8
    celsius_digit(1, 0, 0, 0);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 29) {
    //digit 1001 9
    celsius_digit(1, 0, 0, 1);
    //ten  0010 2
    celsius_ten(0, 0, 1, 0);
  }
  else  if (celsius == 30) {
    //digit 0000 0
    celsius_digit(0, 0, 0, 0);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }
  else  if (celsius == 31) {
    //digit 0001 1
    celsius_digit(0, 0, 0, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }
  
  else  if (celsius == 32) {
    //digit 0010 2
    celsius_digit(0, 0, 0, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 33) {
    //digit 0011 3
    celsius_digit(0, 0, 1, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 34) {
    //digit 0100 4
    celsius_digit(0, 1, 0, 0);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 35) {
    //digit 0101 5
    celsius_digit(0, 1, 0, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 36) {
    //digit 0110 6
    celsius_digit(0, 1, 1, 0);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 37) {
    //digit 0111 7
    celsius_digit(0, 1, 1, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 38) {
    //digit 1000 8
    celsius_digit(1, 0, 0, 0);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 39) {
    //digit 1001 9
    celsius_digit(1, 0, 0, 1);
    //ten  0011 3
    celsius_ten(0, 0, 1, 1);
  }

  else  if (celsius == 40) {
    //digit 0000 0
    celsius_digit(0, 0, 0, 0);
    //ten  0100 4
    celsius_ten(0, 1, 0, 0);
  }
  else{
    //digit 0001 1
    celsius_digit(0, 0, 0, 1);
    //ten  0001 1
    celsius_ten(0, 0, 0, 1); 
  }
}
