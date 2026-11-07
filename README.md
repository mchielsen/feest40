# Fotoapp 40 jaar Tijn & Martijn

Gasten scannen de QR-code, vullen hun naam in en maken of kiezen foto's. Alles komt in één map in Google Drive en verschijnt op de live fotomuur.

- App: https://mchielsen.github.io/feest40/
- Tv-scherm in het café (diavoorstelling met QR-code): https://mchielsen.github.io/feest40/?scherm

## Installatie (eenmalig)

1. Ga naar script.google.com, maak een nieuw project en plak de inhoud van `Code.gs` erin.
2. Kies bovenin de functie `setup` en klik op **Uitvoeren**. Geef toestemming (bij "Google heeft deze app niet geverifieerd": Geavanceerd → Ga naar project).
3. **Implementeren → Nieuwe implementatie → Web-app**. Uitvoeren als: *Ik*. Wie heeft toegang: *Iedereen*. Kopieer de URL (eindigt op `/exec`).
4. Plak die URL in `index.html` bij `API_URL`.
5. Zet `index.html` en `qr.png` in de repo `feest40` en zet GitHub Pages aan (Settings → Pages → branch `main`, map `/root`).

## Na afloop

Open in Google Drive de map **Feest 40 Tijn & Martijn - foto's** → rechtermuisklik → **Downloaden** (Drive maakt er een zip van).

## Foto van de muur halen

Verwijder de regel in de Sheet **Feest 40 Tijn & Martijn - fotologboek** (en eventueel het bestand in de map).
