#include <Arduino.h>
#include <WiFi.h>

const char* ssid = "Esp32";
const char* password ="12345678";
const unsigned int port = 8080;

WiFiServer server(port);
WiFiClient client;

const unsigned int LED_BUILTIN = 2;
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid,password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("\nWiFi connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  
  server.begin();
  Serial.println("Server started");
}

void loop() {
  if (!client.connected()) {
    client = server.available();
    if (client) {
      Serial.println("Client connected");
    }
  }
 
  if (client && client.available()) {
    int data = client.readStringUntil('\n').toInt();
    Serial.print("Received: ");
    Serial.println(data);
 
    if (data == 1) {
      digitalWrite(LED_BUILTIN, HIGH);
    } 
    else {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
 
 delay(10);
}
