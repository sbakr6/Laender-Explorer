
import tkinter as tk  # Ich lade tkinter für mein Fenster
from gui import LaenderExplorer  # Ich hole meine grafische Oberfläche
from api import land_suchen  # Ich hole meine selbst programmierte Ländersuche

fenster = tk.Tk()  # Ich erstelle mein Fenster

app = LaenderExplorer(fenster, suche=land_suchen)  # Ich verbinde die GUI mit meiner API

fenster.mainloop()  # Ich lasse das Fenster geöffnet
