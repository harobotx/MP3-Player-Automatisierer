# MP3-Player-Automatisierer

Ein Python-Script, das Musikalben aus ZIP-Dateien automatisch auf die SD-Karte meines MP3-Players kopiert und die Songs auf Wunsch einheitlich nummeriert.

## Was das Script macht

1. Sucht in einem Ordner nach heruntergeladenen Album-ZIP-Dateien.
2. Legt auf der SD-Karte einen Ordner mit dem Albumnamen an. Dafür wird ein festes Präfix am Anfang des ZIP-Namens abgeschnitten.
3. Entpackt das Album direkt in diesen Ordner.
4. Fragt, ob die ZIP-Datei danach gelöscht werden soll.
5. Fragt, ob die Songs umbenannt werden sollen. Dabei werden die ID3-Tags (Tracknummer und Titel) ausgelesen und die Dateien nach dem Schema `01 - Titel.mp3` benannt. Ungültige Zeichen im Dateinamen (`< > : " / \ | ? *`) werden durch `-` ersetzt.

## Voraussetzungen

- Python 3.x
- Die Bibliothek [mutagen](https://mutagen.readthedocs.io/) zum Auslesen der MP3-Tags

```
pip install -r requirements.txt
```

## Einrichtung

Die beiden Pfade stehen am Anfang des Hauptteils im Script und müssen an den eigenen Rechner angepasst werden:

```python
ZipOrdner = Path(r"C:\Users\localUser\Documents\Zip Mp3")   # Ordner mit den ZIP-Dateien
SD_KARTE = Path(r"D:\music")                                 # Laufwerk der SD-Karte
```

Außerdem schneidet das Script mit `zip_file.stem[22:]` die ersten 22 Zeichen vom ZIP-Namen ab, um den Albumnamen zu erhalten. Wenn deine ZIP-Dateien ein anderes Namensschema haben, muss diese Zahl angepasst werden.

## Benutzung

SD-Karte einstecken, ZIP-Dateien in den ZIP-Ordner legen und starten:

```
python mp3_player_automatisierer.py
```

Anschließend werden die Fragen im Terminal beantwortet: Enter oder `y` bedeutet Ja, jede andere Eingabe (z. B. `n`) bedeutet Nein.

## Beispiel

Vorher: `Song_Name_final.mp3` (Tag: Track 3, Titel "Mein Song")
Nachher: `03 - Mein Song.mp3`

## Mögliche Erweiterungen

- Pfade und Präfix-Länge über eine Konfigurationsdatei oder Kommandozeilenargumente einstellbar machen
- Unterstützung für weitere Formate (z. B. FLAC, M4A)

## Technik

- Python
- `pathlib`, `zipfile`, `re` (Standardbibliothek)
- `mutagen` (ID3-Tags)
