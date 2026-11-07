"""Maakt tv/index.html (de aparte, installeerbare Fotomuur-app) uit index.html."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
inject = '<base href="../">\n<script>window.FORCE_SCREEN = true;</script>\n'
html = html.replace('<head>\n', '<head>\n' + inject, 1)
html = html.replace('<title>Tijn &amp; Martijn 40 · Fotoapp</title>', '<title>Fotomuur · Tijn &amp; Martijn 40</title>', 1)
html = html.replace('<meta name="apple-mobile-web-app-title" content="Feest 40">', '<meta name="apple-mobile-web-app-title" content="Fotomuur">', 1)
(root / 'tv' / 'index.html').write_text(html, encoding='utf-8')
print('tv/index.html bijgewerkt')
