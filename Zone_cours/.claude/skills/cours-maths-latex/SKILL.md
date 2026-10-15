---
name: cours-maths-latex
description: Rédige en LaTeX un cours ou une fiche de TD de mathématiques de lycée (seconde, première, terminale spécialité) au format du Lycée Français International Jean CHARCOT d'El Jadida (page de garde, en-têtes, encadrés colorés, figures TikZ, exemples d'application conformes au B.O.), puis compile et vérifie la mise en page page par page. Utiliser dès qu'un professeur demande de convertir un cours Word/PDF en LaTeX, de restructurer ou mettre en page un chapitre, d'ajouter des exemples d'application, ou de créer une fiche d'exercices/TD progressive sur un chapitre, même sans dire « skill ».
---

# Cours et TD de mathématiques en LaTeX (LFI Jean CHARCOT)

Ce skill produit deux types de documents, dans le style déjà validé par le
professeur (K. EL GHAZOULI) :

- un **cours** : page de garde, sommaire, extrait du B.O., parties numérotées en
  chiffres romains, encadrés Définition / Théorème / Exemple / Remarque / Méthode /
  Démonstration, et une synthèse « L'essentiel du chapitre » ;
- une **fiche de TD** : en-tête encadré, rappel, parties A, B, C… et exercices
  progressifs numérotés.

Les modèles sont dans `templates/`, et deux documents complets servent de
référence dans `exemples/` (chapitre « Continuité des fonctions »). **Lire
l'exemple correspondant avant d'écrire** : il montre le niveau de détail, le ton
et la mise en page attendus.

## Déroulement

1. **Lire la source** (Word, PDF ou texte). Pour un `.docx`, la convertir avec
   `pandoc fichier.docx -t markdown` et extraire les images (`unzip`, dossier
   `word/media`) pour les regarder.
2. **Copier le modèle** (`templates/cours_template.tex` ou
   `templates/td_template.tex`) et remplacer tous les champs `«…»`.
3. **Rédiger le contenu** en suivant les règles ci-dessous.
4. **Vérifier les calculs** : chaque valeur numérique, encadrement, limite ou
   solution annoncée doit être contrôlée (par exemple avec un court script Python).
5. **Compiler et contrôler** :
   `python scripts/compiler.py fichier.tex`. Il faut zéro erreur et zéro alerte
   Overfull. Regarder ensuite la planche PNG produite (toutes les pages en
   miniature).
6. **Corriger la mise en page** jusqu'à ce que les règles de la section
   « Mise en page » soient toutes respectées, puis livrer le `.tex` et le `.pdf`.

## Identité visuelle (ne pas modifier sans demande)

- **Page de garde du cours**, en haut, sur trois lignes séparées :
  « Lycée Français International Jean CHARCOT - EL JADIDA »,
  « Année scolaire AAAA - AAAA », « Niveau : Terminale Spécialité Mathématiques »
  (adapter le niveau). En dessous, le titre principal en majuscules dans un
  encadré, une petite illustration TikZ et « Enseignant : K. EL GHAZOULI ».
- **En-tête** : à gauche « Cours -- Titre » ou « TD -- Titre », à droite
  l'abréviation du niveau (**TSpeMath** pour la Terminale spécialité).
- **Pied de page** : « LFI Jean CHARCOT -- EL JADIDA » | « page/total » |
  « K. EL GHAZOULI ».
- **Couleurs et encadrés** : ceux des modèles. Bleu pour les définitions, rouge
  pour les théorèmes et corollaires, vert (barre latérale) pour les exemples,
  gris pour les remarques, orange pour les méthodes.
- **TD** : exercices **sans encadré** (titre bleu en gras souligné d'un filet),
  **sans niveau de difficulté** ni étoiles. Les encadrés gris « Indication »
  sont autorisés.

## Règles de rédaction mathématique

- **Programme officiel** : respecter le B.O. du niveau (contenus, capacités
  attendues, démonstrations, algorithmes), et recopier l'extrait du B.O. dans
  l'encadré `programme` du cours.
- **Contenu de la source** : tout le conserver (texte et figures), corriger les
  erreurs mathématiques (et les signaler au professeur dans la réponse), puis
  restructurer avec rigueur et logique.
- **Exemples d'application** : en ajouter après chaque notion, dans une
  sous-partie « Exemples d'application ».
- **Une étape par ligne** : dans les exemples, utiliser l'environnement `etapes`
  (« Étape 1. », « Étape 2. »…) et finir par `\textbf{Conclusion :}`. Dans les
  démonstrations, une idée par paragraphe.
- **Limites à gauche et à droite** : toujours les noter $x\to a^-$ et $x\to a^+$
  (macros `\limg{a}{f(x)}` et `\limd{a}{f(x)}`), jamais avec deux lignes sous
  le « lim » (« x→a / x<a »).
- **Continuité en un point** : la définir par
  $\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=f(a)$, avec la méthode en trois points
  (image, limite à gauche, limite à droite).
- **Plusieurs intervalles disjoints** : les écrire comme une **réunion**,
  $\left]-\infty;2\right[\;\cup\;\left]2;+\infty\right[$ (avec `\;\cup\;`), et
  non avec « et ». Le professeur dit parfois « intersection » pour parler de
  cette écriture : c'est bien la réunion ∪ qu'il faut utiliser, et le lui
  préciser.
- **Fonctions par morceaux** : écrire « Sur chacun des intervalles … , $f$ est
  une fonction polynôme ; donc $f$ est continue sur … ∪ … ». Ne pas écrire
  « coïncide avec ».
- **Fin de démonstration** : pas de symbole ■ ni de « CQFD » graphique.
- **Intervalles** : les écrire avec les macros `\intff`, `\intoo`, `\intfo` et
  `\intof` (notation française avec point-virgule).
- **Figures** : toujours les redessiner en TikZ/pgfplots plutôt que d'insérer
  des images. Calculer les coordonnées exactes des points annotés.
- **Ne pas ajouter** de précisions que le professeur a fait retirer (exemple :
  « (ici x = −∛3) » après une existence par le TVI).

## Mise en page (exigences du professeur)

- **Espacement aéré** : `\setstretch{1.25}` et des espaces entre paragraphes,
  déjà réglés dans les modèles.
- **Titres jamais isolés** : un titre de partie, de sous-partie ou d'exercice ne
  doit jamais se retrouver en bas de page sans son texte. Les modèles le gèrent
  par `\needspace`, et un titre de partie reste solidaire de sa première
  sous-partie.
- **Aucune page à moitié vide**, sauf la dernière. Les modèles redéfinissent
  `\needspace` et mettent à zéro `\@secpenalty`, `\@beginparpenalty`,
  `\@endparpenalty` et `\@itempenalty`. Les pénalités négatives
  qu'utiliseraient sinon LaTeX et `needspace` attirent les sauts de page trop
  tôt et créent des pages à moitié vides. **Ne pas retirer ce réglage.**
- **Si une page reste trop vide**, ajuster localement :
  - réduire légèrement une figure ou un tableau ;
  - mettre une liste de cas sur deux colonnes (`multicols`) ;
  - garder un énoncé avec son tableau (`minipage`) ;
  - fusionner deux questions courtes.
  Ne jamais insérer de `\newpage` arbitraire.
- **Pas d'encadré cassable dans une `minipage`** : passer l'option
  `unbreakable` (par exemple `\begin{exemple}[unbreakable]{}{}`).
- **Tableau de variations** : utiliser `tkz-tab`.
- **Algorithmes** : écrire en Python avec `listings` (programme et éventuel
  tableau pas à pas).

## Compilation

- Il faut une distribution LaTeX avec `pdflatex` (MiKTeX ou TeX Live) et les
  paquets `tcolorbox`, `pgfplots`, `tkz-tab`, `titlesec`, `tocloft`,
  `needspace`, `setspace`, `fancyhdr`, `lastpage`, `listings` et `babel`
  (français).
- Toujours compiler **deux fois** : `scripts/compiler.py` s'en charge.
- Livrer le `.tex` **et** le `.pdf`. Dans la réponse au professeur, résumer en
  français ce qui a été fait, les corrections mathématiques apportées et les
  éventuels choix à valider.
