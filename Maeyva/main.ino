#include <AccelStepper.h>
AccelStepper stepper1 = AccelStepper(1, 6, 10); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
// type de moteur (1) - pin nombre de pas - pin direction
AccelStepper stepper2 = AccelStepper(1, 5, 13);

float Tensionlue;
float volume_initial = 0;
float volume_injecte = 0;
int Laser = 3;
String ChaineSaisie;

void setup()
{

    Serial.begin(9600); // pour démarrer une mesure série
    pinMode(A0, INPUT); // on définit A0 comme entrée
    pinMode(Laser, OUTPUT);

    stepper1.setMaxSpeed(1500);
    stepper1.setAcceleration(1500); // pompe 2
    stepper2.setMaxSpeed(1500);
    stepper2.setAcceleration(1500); // pompe 1
}

void loop()
{
    if (Serial.available())
    {
        ChaineSaisie = Serial.readString();
    }

    if (ChaineSaisie == "go")
    {
        stepper1.move(-11300);
        stepper1.runToPosition(); // pour remplir la boucle de soude
        stepper2.move(-23000);
        stepper2.runToPosition(); // pour remplir le chien avec la solution d'aspirine sans soude
        delay(1000);

        digitalWrite(Laser, HIGH);
        Tensionlue = analogRead(A0) * 5.0 / 1023.; // formule pour calculer la tension lue
        delay(1000);
        Serial.print("T=");
        Serial.println(Tensionlue); // afficher la valeur de la tension lue
        volume_initial = 0;
        Serial.print("Vi =");
        Serial.println(volume_initial);
        delay(1000);              // délai d'affichage des messages
        digitalWrite(Laser, LOW); //éteindre le laser

        stepper2.move(25000);
        stepper2.runToPosition(); // pour faire circuler une fois la solution à doser dans le  chien
        ChaineSaisie = "stop";
    }

    if (ChaineSaisie == "3")
    {
        stepper1.move(-13100);
        stepper1.runToPosition(); // pour verser 3 mL de soude
        delay(1000);

        stepper2.move(-23000);
        stepper2.runToPosition(); // pour remplir le chien avec la solution d'aspirine sans soude
        delay(1000);

        digitalWrite(Laser, HIGH);
        Tensionlue = analogRead(A0) * 5.0 / 1023; // formule pour calculer la tension lue
        delay(1000);
        Serial.print("T=");
        Serial.println(Tensionlue); // afficher la valeur de la tension lue
        volume_injecte = volume_initial + 3;
        Serial.print("Vinj =");
        Serial.println(volume_injecte);
        delay(1000);              // délai d'affichage des messages
        digitalWrite(Laser, LOW); //éteindre le laser

        stepper2.move(25000);
        stepper2.runToPosition(); // pour faire circuler une fois la solution à doser dans le chien
        ChaineSaisie = "stop";
    }

    if (ChaineSaisie == "M")
    {
        stepper1.move(-899);
        stepper1.runToPosition(); // pour ajouter 0,2 mL de soude dans la solution à titrer
        delay(2000);              // temps pour homogénéiser la solution
        stepper2.move(-23000);
        stepper2.runToPosition(); // pour que la solution remplisse le chien
        delay(1000);              // temps de pause pour la mesure

        digitalWrite(Laser, HIGH);
        Tensionlue = analogRead(A0) * 5.0 / 1023; // formule pour calculer la tension lue
        delay(1000);
        Serial.print("T=");
        Serial.println(Tensionlue); // afficher la valeur de la tension lue
        volume_injecte = volume_injecte + 0.2;
        Serial.print("Vinj =");
        Serial.println(volume_injecte);
        delay(1000);              // délai d'affichage des messages
        digitalWrite(Laser, LOW); //éteindre le laser

        stepper2.move(25000);
        stepper2.runToPosition(); // pour que la solution retourne dans le bécher
        delay(2000);              // homogénéiser la solution

        if (volume_injecte > 5.8)
        {
            ChaineSaisie = "stop";
        }
    }
    if (ChaineSaisie == "R")
    {
        stepper1.move(13000);
        stepper1.runToPosition(); // pour vider la boucle de soude

        stepper2.move(-23000);
        stepper2.runToPosition(); // pour remplir le chien avec de l'eau
        delay(1000);
        stepper2.move(25000);
        stepper2.runToPosition(); // pour faire vider l'eau du chien
        ChaineSaisie = "stop";
    }
}