## Takie tam luźne pomysłów z rozmowy z Łukaszem ....

##### _(Zapisane by nie zgubić)_

1. Nie zapisujemy treści postów innych osób do bazy, ani do plików.
2. W aplikacji działa w tle skrypt oparty o np cron, który dba o odnawianie/przedłużanie tokenu FB.

   Dane tokena przechowywane poza strukturą serwera WWW.
   Osobne środowisko do odnawiania tokena, nie polączone razem z glowna aplikacja (jako opcja).

3. Wymianę informacji postach znajomych opieramy o komunikację REST API. ->

   a. Osoba powierająca informacje musi uzyskać zezwolenie na pobranie danych.

   b. Autoryzacja -> klucze prywatne/publiczne lub wymiana własnych identyfikatorów np typu GUID

   c. Identyfikacja i Uwierzytelnianie -> TODO !!! ???? -> Wysyłanie zaproszeń

   Tylko SSL.

4. Powiadomienia w formie codziennego email z informacjami, kto jaki post umieścił.

5. Automatyzacja operacji rejestracji i pozyskiwania tokenów
