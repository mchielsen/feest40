"""Bouwt de losse Fotomuur-app (repo mchielsen/fotomuur) uit index.html van feest40.

Gebruik: python3 tools/maak-fotomuur.py /pad/naar/fotomuur-repo
De Fotomuur draait op een eigen adres (mchielsen.github.io/fotomuur/), zodat hij op een
telefoon als aparte app naast de Fotoapp geïnstalleerd kan worden.
"""
import json, shutil, sys
from pathlib import Path

src = Path(__file__).resolve().parent.parent
dst = Path(sys.argv[1]).resolve()

html = (src / 'index.html').read_text(encoding='utf-8')
html = html.replace('<head>\n', '<head>\n<script>window.FORCE_SCREEN = true;</script>\n', 1)
html = html.replace('<!-- Let op: de Fotomuur (repo fotomuur) wordt uit dit bestand gemaakt met tools/maak-fotomuur.py -->\n',
                    '<!-- Gegenereerd uit mchielsen/feest40 met tools/maak-fotomuur.py: niet hier aanpassen -->\n', 1)
html = html.replace('<title>Tijn &amp; Martijn 40 · Fotoapp</title>', '<title>Fotomuur · Tijn &amp; Martijn 40</title>', 1)
html = html.replace('<meta name="apple-mobile-web-app-title" content="Feest 40">', '<meta name="apple-mobile-web-app-title" content="Fotomuur">', 1)
html = html.replace('<link rel="icon" type="image/png" href="icon-192.png">', '<link rel="icon" type="image/png" href="icon-tv-192.png">', 1)
html = html.replace('<link rel="apple-touch-icon" href="apple-touch-icon.png">', '<link rel="apple-touch-icon" href="icon-tv-192.png">', 1)
(dst / 'index.html').write_text(html, encoding='utf-8')

for f in ['qr.png', 'tijn-martijn.jpg', 'icon-192.png', 'icon-tv-192.png', 'icon-tv-512.png', 'icon-tv-maskable-512.png']:
    shutil.copy2(src / f, dst / f)

m = json.loads((src / 'manifest-tv.webmanifest').read_text(encoding='utf-8'))
m.update({'id': './', 'start_url': './', 'scope': './'})
(dst / 'manifest-tv.webmanifest').write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding='utf-8')

sw = (src / 'sw.js').read_text(encoding='utf-8')
import re
ver = re.search(r"feest40-v(\d+)", sw).group(1)
sw = re.sub(r"const CACHE = '[^']*';", f"const CACHE = 'fotomuur-v{ver}';", sw)
sw = re.sub(r"const SHELL = \[[^\]]*\];", "const SHELL = ['./', './index.html', './qr.png', './tijn-martijn.jpg', './icon-tv-192.png', './icon-tv-512.png', './manifest-tv.webmanifest'];", sw)
(dst / 'sw.js').write_text(sw, encoding='utf-8')

(dst / 'README.md').write_text(
    '# Fotomuur · Tijn & Martijn 40\n\nTv-weergave van de fotoapp (https://mchielsen.github.io/feest40/).\n\n'
    'Niet hier aanpassen: deze bestanden worden gemaakt uit de repo `feest40` met `tools/maak-fotomuur.py`.\n',
    encoding='utf-8')
print('Fotomuur gebouwd in', dst)
