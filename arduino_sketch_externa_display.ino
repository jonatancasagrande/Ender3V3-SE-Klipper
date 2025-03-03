#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define LCD_ADDR 0x27  // Dirección I2C de la pantalla (puede ser 0x3F en algunos modelos)
#define LCD_COLS 16
#define LCD_ROWS 2

LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLS, LCD_ROWS);

void setup() {
    Serial.begin(9600); // Inicializa el puerto serie
    lcd.init();         // Inicializa el LCD
    lcd.backlight();    // Enciende la luz de fondo del LCD
    lcd.clear();
}

void loop() {
    static String mensaje = "";
    
    if (Serial.available()) {
        char c = Serial.read(); // Lee un carácter del puerto serie
        
        if (c == '\n') { // Si es un salto de línea, limpia y muestra el mensaje
            lcd.clear();
            lcd.setCursor(0, 0);
            
            if (mensaje.length() <= LCD_COLS) {
                lcd.print(mensaje); // Muestra el mensaje si cabe en una línea
            } else {
                lcd.print(mensaje.substring(0, LCD_COLS)); // Muestra la primera línea
                lcd.setCursor(0, 1);
                lcd.print(mensaje.substring(LCD_COLS, LCD_COLS * 2)); // Segunda línea
            }
            
            mensaje = ""; // Reinicia el mensaje para la siguiente entrada
        } else {
            mensaje += c; // Agrega el carácter al mensaje
        }
    }
}
