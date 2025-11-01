#include <Arduino.h>
#include <WiFi.h>

const char* ssid = "Esp32";
const char* password ="12345678";
const unsigned int port = 8080;

WiFiServer server(port);
WiFiClient client;

int counter = 0;
void setup() {
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
 
  if (client) {
    client.println(counter);

    Serial.print("Sent: ");
    Serial.println(counter);
    
    counter++;
    delay(1000);
  }
 
 delay(10);
}

