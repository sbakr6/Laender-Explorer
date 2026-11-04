
import tkinter as tk


class LaenderExplorer:
    def __init__(self, fenster, suche=None):
        self.fenster = fenster
        self.suche = suche

        self.fenster.title("Länder Explorer")
        self.fenster.geometry("850x600")
        self.fenster.minsize(650, 520)
        self.fenster.configure(bg="#0B1120")

        # Farben für meine Oberfläche
        self.hintergrund = "#0B1120"
        self.karte = "#172033"
        self.blau = "#3B82F6"
        self.weiss = "#F8FAFC"
        self.grau = "#94A3B8"

        # Überschrift
        tk.Label(
            fenster,
            text="LÄNDER EXPLORER",
            font=("Segoe UI", 28, "bold"),
            fg=self.weiss,
            bg=self.hintergrund
        ).pack(pady=(45, 5))

        tk.Label(
            fenster,
            text="Entdecke Länder aus der ganzen Welt",
            font=("Segoe UI", 12),
            fg=self.grau,
            bg=self.hintergrund
        ).pack(pady=(0, 35))

        # Suchbereich
        suchbereich = tk.Frame(fenster, bg=self.hintergrund)
        suchbereich.pack(fill="x", padx=65)

        self.eingabe = tk.Entry(
            suchbereich,
            font=("Segoe UI", 14),
            bg=self.karte,
            fg=self.weiss,
            insertbackground=self.weiss,
            relief="flat",
            bd=0
        )
        self.eingabe.pack(side="left", fill="x", expand=True, ipady=14, ipadx=15)

        tk.Button(
            suchbereich,
            text="Suchen",
            font=("Segoe UI", 12, "bold"),
            bg=self.blau,
            fg="white",
            activebackground="#2563EB",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12,
            command=self.land_suchen
        ).pack(side="left", padx=(12, 0))

        self.fenster.bind("<Return>", lambda event: self.land_suchen())

        # Bereich für Länderinformationen
        self.infobereich = tk.Frame(
            fenster,
            bg=self.karte,
            padx=35,
            pady=30
        )
        self.infobereich.pack(fill="both", expand=True, padx=65, pady=30)

        tk.Label(
            self.infobereich,
            text="LÄNDERINFORMATIONEN",
            font=("Segoe UI", 11, "bold"),
            fg=self.blau,
            bg=self.karte
        ).pack(anchor="w", pady=(0, 25))

        self.name = self.info_zeile("Land")
        self.hauptstadt = self.info_zeile("Hauptstadt")
        self.einwohner = self.info_zeile("Einwohner")

        # Meldungen unten
        self.status = tk.Label(
            fenster,
            text="Gib oben einen Ländernamen ein.",
            font=("Segoe UI", 10),
            fg=self.grau,
            bg=self.hintergrund
        )
        self.status.pack(pady=(0, 25))

        self.eingabe.focus_set()

    def info_zeile(self, titel):
        bereich = tk.Frame(self.infobereich, bg=self.karte)
        bereich.pack(fill="x", pady=12)

        tk.Label(
            bereich,
            text=titel,
            font=("Segoe UI", 12),
            fg=self.grau,
            bg=self.karte,
            width=15,
            anchor="w"
        ).pack(side="left")

        wert = tk.Label(
            bereich,
            text="—",
            font=("Segoe UI", 15, "bold"),
            fg=self.weiss,
            bg=self.karte,
            anchor="w",
            wraplength=400,
            justify="left"
        )
        wert.pack(side="left", fill="x", expand=True)

        return wert

    def daten_anzeigen(self, daten):
        self.name.config(text=str(daten["name"]))
        self.hauptstadt.config(text=str(daten["capital"]))
        self.einwohner.config(text=str(daten["population"]))
        self.status.config(text="Land erfolgreich gefunden!", fg="#4ADE80")

    def land_suchen(self):
        land = self.eingabe.get().strip()

        if land == "":
            self.status.config(
                text="Bitte gib einen Ländernamen ein.",
                fg="#F87171"
            )
            return

        if self.suche is None:
            self.status.config(
                text="Die GUI ist fertig. Die API wird als Nächstes verbunden.",
                fg=self.grau
            )
            return

        try:
            daten = self.suche(land)

            if daten is None:
                self.status.config(
                    text="Dieses Land wurde nicht gefunden.",
                    fg="#F87171"
                )
                return

            self.daten_anzeigen(daten)

        except Exception:
            self.status.config(
                text="Bei der Suche ist ein Fehler aufgetreten.",
                fg="#F87171"
            )


# Ich starte meine grafische Oberfläche
if __name__ == "__main__":
    fenster = tk.Tk()
    app = LaenderExplorer(fenster)
    fenster.mainloop()
