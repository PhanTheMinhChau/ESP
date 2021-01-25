#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <EEPROM.h>
ESP8266WebServer webServer(80);
//==========AP info=======================//
char* ssid_ap = "E-SMART HOME";
char* pass_ap = "12345678";
IPAddress ip_ap(192,168,1,1);
IPAddress gateway_ap(192,168,1,1);
IPAddress subnet_ap(255,255,255,0);
String statusD1="1",statusD2="1",statusD3="1",statusD4="1";
String ssid;
String pass;
