String data = "000000100SZ";

void setup() {
  Serial.begin(9600);
  while (!Serial)
        delay(10);
}

void loop() {
  if (Serial.available() > 0) {
        String str = Serial.readStringUntil('\n');
        if (str.length() == 11) {
            data = str;
        }
    }

    switch(data.charAt(10)) {
      case 'T':
        Serial.println("21.1");
        data.setCharAt(10, 'Z');
        break;
        
      case 'H':
        Serial.println("55");
        data.setCharAt(10, 'Z');
        break; 
        
      case 'E':
        Serial.println("21.1");
        data.setCharAt(10, 'Z');
        break; 
        
      case 'I':
        Serial.println("55");
        data.setCharAt(10, 'Z');
        break; 
        
      case 'A':
        Serial.println(random(1, 200));
        data.setCharAt(10, 'Z');
        break;
    }
}
