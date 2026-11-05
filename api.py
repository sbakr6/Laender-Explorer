import requests

def land_suchen(land):
    url = "https://countries.dev/name/" + land

    try:
        antwort = requests.get(url)

        if antwort.status_code == 200:
            daten = antwort.json()

            if len(daten) > 0:
                land_daten = daten[0]

                return {
                    "name": land_daten["name"],
                    "capital": land_daten["capital"],
                    "population": land_daten["population"],
                    "flag": land_daten["flags"]["png"]
                }

        return None

    except requests.RequestException:
        return None