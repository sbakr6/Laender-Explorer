import requests  # Ich lade die Bibliothek requests

def land_suchen(land):  # Ich erstelle eine Funktion für die Ländersuche

        url = "https://countries.dev/name/" + land  # Ich erstelle die Adresse mit dem Ländernamen

        try:  # Ich versuche, die API aufzurufen
            antwort = requests.get(url, timeout=10)  # Ich frage die API und speichere die Antwort

            if antwort.status_code == 200:  # Ich prüfe, ob die Anfrage erfolgreich war
                daten = antwort.json()  # Ich wandle die Antwort in Python-Daten um

                if len(daten) > 0:  # Ich prüfe, ob Länder gefunden wurden
                    land_daten = daten[0]  # Ich nehme das erste gefundene Land

                    return {
                        "name": land_daten["name"],
                        "capital": land_daten["capital"],
                        "population": land_daten["population"]
                    }  # Ich gebe die Informationen an die GUI zurück

            return None  # Ich gebe nichts zurück, wenn kein Land gefunden wurde

        except requests.RequestException:  # Ich fange Fehler bei der Internetverbindung ab
            return None  # Ich gebe nichts zurück, wenn die Anfrage nicht funktioniert
