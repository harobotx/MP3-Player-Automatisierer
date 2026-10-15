from pathlib import Path
import zipfile
from mutagen.easyid3 import EasyID3
import re

def gültiger_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', '-', name)
    return name

def ja_nein(frage):
    # Enter oder "y"/"j" bedeutet Ja, alles andere Nein
    antwort = input(f"{frage} (Y/n)   ").strip().lower()
    return antwort in ("", "y", "j")

def Song_umbenenner(target):
    ordner = Path(target)
    songs = list(ordner.glob("*.mp3"))


    for song in songs:
        try:
            audio = EasyID3(song)

            track = str(audio.get("tracknumber", ["0"])[0].split("/")[0]).zfill(2)
            title = gültiger_filename(audio.get("title", [song.stem])[0])

            new_name = f"{track} - {title}.mp3"
            print(new_name)
            song.rename(song.with_name(new_name))

        except Exception as Fehler:
            print(f"Fehler bei {song.name}: {Fehler}")
    print("Alle Songs erfolgreich umbenannt")
    return


ZipOrdner = Path(r"C:\Users\localUser\Documents\Zip Mp3")
SD_KARTE = Path(r"D:\music")

if not SD_KARTE.exists():
    print(f"SD-Karte nicht gefunden ({SD_KARTE}). Ist sie eingesteckt?")
else:
    try:
        for zip_file in ZipOrdner.glob("*.zip"):

            print(f"Zip Datei erkannt: {zip_file.name}")
            name = zip_file.stem[22:]

            target = SD_KARTE / name
            target.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(zip_file, "r") as zip_ref:
                zip_ref.extractall(target)
            print("Daten wurden extrahiert und in den Ordner übertragen")

            if ja_nein(f"Soll die Zip Datei {zip_file.name} gelöscht werden?"):
                zip_file.unlink()

            if ja_nein("Soll das Album nummeriert werden?"):
                Song_umbenenner(target)

    except Exception as fehler:
        print(f"Fehler: {fehler}")
