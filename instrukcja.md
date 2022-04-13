1. Wejdź na stronę: https://developers.facebook.com/ -> "LogIn" (prawy górny róg)
2. Jeśli nie masz konta to je załóż.
3. Klikamy w menu -> "My Apps" (prawy górny róg)
4. Klikamy w przycisk "Create App"
5. Wybieramy "Konsument" i klikamy w przycisk "Next"
6. Wypełniamy:
   "Display name" -> jak tam uważasz
   "App contack emaill" -> wpisujemy swój prawdziwy email do komunikacji z FB
   Business Accounts -> zostawiamy "No Busines ...."
   klikamy w przycisk "Create app"
7. Przechodzimy w nowej karcie na adres: https://developers.facebook.com/tools/explorer/
8. W prawej strony pole "Facebook App" ustawiamy na pozycją zgodną na nadaną wyżej nazwą.
9. Pole "User or Page" ustawiamy na "Get User Token" i w wyskakującym oknie potwierdzamy żądanie uprawnień.
10. W polu "Permision" dodajemy uprawnienia:
    user_likes
    user_link
    user_posts
    user_photos
    user_videos
    user_friends
    pages_show_list
    user_events
    user_managed_groups

11. Klimamy w przycisk "Generate Access Token" w oknie które wyskoczy potwierdzamy tożsamoś oraz ustalamy zakres uprawnień do własnych zasobów.
12. Kopiujemy wygenerowany token.
13. Klikamy w górnym menu "Tools" i wybieramy pozycje "Access token debugger"
14. Wklejamy w pole nasz token i klikamy "Debug"
15. Pokaże uprawnienia naszego tokenu. Token musi by typu "User", w polu "Expires" podano jego czas ważności. (zazwyczaj jest to mała wartoś)
16. Czas ważności możemy wydłuży, klikamy w przycisk "Extend Access Token" , wyświetlony nowy token zapisujemy.
17. Przechodzimy do adresu URL: https://developers.facebook.com/ -> "My App", wybieramy utworzoną aplikacje.
18. Klikamy w meny z lewej "Settings" a nastepnie "Basic"
19. Zapisujemy wartości w polach "App ID" oraz "App secret"
20. Tworzymy plik config.py o strukturze:
    class MY():
    app_id = "twoj App ID"
    app_secret = "twoj App secret"
    user_long_token = "twoj token"
21. Czynności do samodzielnego wykonania:

a) tam gdzie mamy ustawienia naszej App (Settings->Basic) należy uzupełni pola: App domains, Provacy Policy URL, User data delection, Category, App purpose, Terms od Service URL, Category

b) a nastepinie zweryfikowac aplikacja -> przycisk "Start Verification oraz przełaczyc "AppMode" na "Live".

Jak to zrobicie aplikacja bedzie w pełni działac i udostepni wiecej danych w zwracanych odpowiedziach.

22. Instalujemy srodowisko i moduły
    python3 -m env .env

23. Dla test_01 wymagane: pip install logging requests
24. Dla test_02 wymagane: pip install python-facebook-api
