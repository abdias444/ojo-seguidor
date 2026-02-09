#include <Servo.h>

// Declaramos los servos
Servo servo;
Servo servo2;

// Variables
char dato;
int angulo = 145;
int angulo2 = 50;

void setup() {
    // Inicia la comunicación serial
    Serial.begin(9600);

    // Adjunta los servos a los pines correspondientes
    servo.attach(9);   // Servo en pin 9
    servo2.attach(10); // Servo en pin 10

    // Posición inicial de los servos
    servo.write(angulo);
    servo2.write(angulo2);
}

void loop() {
    if (Serial.available()) {
        dato = Serial.read();
        delay(10);

        switch (dato) {
            case 'd':   // Derecha
                angulo -= 1;
                servo.write(angulo);
                break;

            case 'i':   // Izquierda
                angulo += 1;
                servo.write(angulo);
                break;

            case 'u':   // Arriba
                angulo2 += 1;
                servo2.write(angulo2);
                break;

            case 'b':   // Abajo
                angulo2 -= 1;
                servo2.write(angulo2);
                break;

            case 'p':   // Parar
                servo.write(angulo);
                servo2.write(angulo2);
                break;
        }
    }
}