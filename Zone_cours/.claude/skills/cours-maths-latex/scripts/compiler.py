"""Compile un document LaTeX et produit une planche de contrôle de la mise en page.

Usage :
    python compiler.py chemin/vers/fichier.tex [dossier_sortie]

- Lance pdflatex deux fois (sommaire, numéros de page « n/total »).
- Affiche les erreurs, les boîtes trop larges (Overfull) et les alertes tcolorbox.
- Si pdftoppm et Pillow sont disponibles, crée <nom>_planche.png : toutes les pages
  en miniature, pour repérer les titres isolés et les pages à moitié vides.
"""
import glob
import os
import re
import shutil
import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    tex = os.path.abspath(sys.argv[1])
    sortie = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(tex), "build")
    os.makedirs(sortie, exist_ok=True)
    nom = os.path.splitext(os.path.basename(tex))[0]
    log = os.path.join(sortie, nom + ".log")

    for _ in range(2):
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             "-output-directory", sortie, tex],
            cwd=os.path.dirname(tex), capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        if r.returncode != 0:
            texte = open(log, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"^!.*(?:\n.*){0,5}", texte, re.M):
                print(m.group(0))
            sys.exit("Échec de la compilation.")

    texte = open(log, encoding="utf-8", errors="replace").read()
    alertes = re.findall(r"^(Overfull.*|Package tcolorbox Warning.*)$", texte, re.M)
    print(f"Compilation réussie : {os.path.join(sortie, nom + '.pdf')}")
    print(f"{len(alertes)} alerte(s) de mise en page")
    for a in alertes[:20]:
        print("  ", a)

    if shutil.which("pdftoppm"):
        try:
            from PIL import Image
        except ImportError:
            print("Pillow absent : pas de planche de contrôle (pip install pillow).")
            return
        prefixe = os.path.join(sortie, nom + "_pg")
        for f in glob.glob(prefixe + "-*.png"):
            os.remove(f)
        subprocess.run(["pdftoppm", "-r", "60", "-png",
                        os.path.join(sortie, nom + ".pdf"), prefixe], check=True)
        pages = sorted(glob.glob(prefixe + "-*.png"))
        ims = [Image.open(p) for p in pages]
        w, h = ims[0].size
        cols = 4
        rows = (len(ims) + cols - 1) // cols
        planche = Image.new("RGB", (w * cols, h * rows), "white")
        for k, im in enumerate(ims):
            planche.paste(im, ((k % cols) * w, (k // cols) * h))
        chemin = os.path.join(sortie, nom + "_planche.png")
        planche.save(chemin)
        print(f"{len(ims)} pages — planche de contrôle : {chemin}")


if __name__ == "__main__":
    main()
