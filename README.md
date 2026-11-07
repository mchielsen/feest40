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

## Fotomuur op de tv (tablet + Chromecast)

1. Open op de Android-tablet in Chrome: https://mchielsen.github.io/feest40/tv
2. Tik op **App installeren** (rechtsboven). De app "Fotomuur" opent voortaan direct de tv-weergave.
3. Tik op het **cast-icoon** en kies de Chromecast.

Standaard stuurt de tablet de foto's één voor één naar de Chromecast (de tablet moet dan blijven aanstaan).

### Eigen ontvanger (optioneel, beste resultaat)

Dan draait de complete fotomuur (met QR-code en zijbalk) zelfstandig op de Chromecast.

1. Registreer op https://cast.google.com/publish (eenmalig $5).
2. **Add new application → Custom Receiver**. Receiver URL: `https://mchielsen.github.io/feest40/ontvanger/`
3. Publiceer de app, of registreer het serienummer van de Chromecast (15 min wachten en Chromecast herstarten).
4. Zet de App-ID in `index.html` bij `CAST_APP_ID`.
