---
name: skill-td
description: Crée en LaTeX une fiche de TD ou fiche d'exercices de mathématiques de lycée (seconde, première, terminale spécialité) au format du Lycée Français International Jean CHARCOT d'El Jadida (en-tête encadré, parties A, B, C…, exercices progressifs sans encadré, figures TikZ, tableaux de variations, Python), avec des énoncés vérifiés par le calcul et une mise en page contrôlée page par page. Utiliser dès qu'un professeur demande un TD, une fiche d'exercices, une série d'exercices, des exercices d'entraînement ou d'application sur un chapitre, même sans dire « skill ».
---

# Fiches de TD de mathématiques en LaTeX (LFI Jean CHARCOT)

Ce skill produit **uniquement des fiches d'exercices (TD)**, dans le style déjà
validé par le professeur (K. EL GHAZOULI).

- **Modèle à copier** : `templates/td_template.tex`.
- **Fiche complète de référence** : `exemples/TD_continuite_des_fonctions.tex`
  (15 exercices sur la continuité, Terminale spécialité). **La lire avant
  d'écrire** : elle fixe le niveau de détail, la progression, le ton et la mise
  en page attendus.

## Informations à obtenir

Le professeur indique en général le chapitre et le nombre d'exercices. S'il ne
dit pas le reste, utiliser ces valeurs par défaut sans poser de question :

| Information | Valeur par défaut |
|---|---|
| Niveau | Terminale spécialité mathématiques (en-tête droit : **TSpeMath**) |
| Nombre d'exercices | 15 |
| Année scolaire | année en cours (exemple : « 2026 - 2027 ») |
| Source | aucune : créer les exercices conformément au B.O. du niveau |

Abréviations du niveau pour l'en-tête droit : `2nde` (seconde), `1reSpeMath`
(première spécialité), `TSpeMath` (terminale spécialité), `TMathsComp` (maths
complémentaires), `TMathsExp` (maths expertes).

Si le professeur fournit un cours, un ancien TD ou des exercices (Word, PDF,
texte), s'en servir comme base. Pour un `.docx`, utiliser
`pandoc fichier.docx -t markdown`.

## Déroulement

1. **Copier le modèle** et remplacer tous les champs `«…»` : titre du chapitre
   (en-tête gauche et grand titre), nombre d'exercices, rappel du cours dans
   l'encadré orange, et niveau si ce n'est pas la terminale (lignes « Niveau : … »
   et en-tête droit).
2. **Concevoir la progression** avant de rédiger :
   - 3 à 5 parties (A, B, C, D…), qui vont des applications directes du cours
     aux exercices de synthèse ;
   - pour un TD de terminale, une dernière partie « Vers le bac » (problème
     avec fonction auxiliaire, exercice de réflexion, approfondissement) ;
   - des types d'exercices variés : lecture graphique, calcul, recherche de
     paramètre, vrai/faux justifié, tableau de variations, algorithme Python à
     compléter, problème en plusieurs parties.
3. **Rédiger les exercices** en suivant les règles ci-dessous.
4. **Vérifier chaque énoncé par le calcul** (avec un court script Python) :
   valeurs numériques, signes, limites, solutions, encadrements, nombre de
   solutions, étapes d'une dichotomie. Un exercice faux ou infaisable est
   inacceptable.
5. **Compiler et contrôler** : `python scripts/compiler.py fichier.tex`.
   Il faut zéro erreur et zéro alerte Overfull. Regarder la planche PNG
   produite (toutes les pages en miniature) et corriger la mise en page.
6. **Livrer** le `.tex` et le `.pdf`, avec un résumé en français : liste des
   exercices par partie, et proposition de rédiger le corrigé.

## Présentation (validée par le professeur, ne pas modifier sans demande)

- **En haut de la page 1** : un encadré avec, sur des lignes séparées :
  - « Lycée Français International Jean CHARCOT - EL JADIDA » ;
  - « Année scolaire AAAA - AAAA » ;
  - « Niveau : … » ;
  - un filet, puis le grand titre « TD -- Titre du chapitre » et
    « N exercices progressifs ».
- **Sous l'encadré du haut** : un encadré orange **« Rappel : »** qui contient
  seulement la définition ou le théorème central du chapitre.
- **En-tête** : à gauche « TD -- Titre du chapitre », à droite l'abréviation
  du niveau.
- **Pied de page** : « LFI Jean CHARCOT -- EL JADIDA » | « page/total » |
  « K. EL GHAZOULI ».
- **Parties** : bandeaux bleus « Partie A -- … », « Partie B -- … »…
- **Exercices** :
  - environnement `exercice` : titre bleu en gras « Exercice n -- Titre »,
    souligné d'un filet ;
  - **aucun encadré** autour des exercices ;
  - **aucun niveau de difficulté**, ni étoiles, ni légende des niveaux.
- **Questions** : numérotées `1.`, `2.`… puis `a)`, `b)` (`enumerate`
  imbriqués, déjà réglés dans le modèle).
- **Indications** : encadré gris `indication`, facultatif, court.

## Règles mathématiques et de rédaction

- **Programme** : rester strictement dans le programme officiel (B.O.) du
  niveau, sans notion hors programme.
- **Énoncés** : clairs, complets, autonomes. Chaque question est réalisable
  avec ce qui précède.
- **Limites à gauche et à droite** : toujours les noter $x\to a^-$ et
  $x\to a^+$ (macros `\limg{a}{f(x)}` et `\limd{a}{f(x)}`), jamais avec deux
  lignes sous le « lim ».
- **Plusieurs intervalles disjoints** : les écrire comme une **réunion**,
  avec `\intoo{-\infty}{2}\;\cup\;\intoo{2}{+\infty}`, et non avec « et ».
  Le professeur dit parfois « intersection » pour parler de cette écriture :
  utiliser la réunion ∪ et le lui préciser.
- **Intervalles** : macros `\intff`, `\intoo`, `\intfo`, `\intof` (notation
  française avec point-virgule).
- **Fonctions par morceaux** : écrire « Sur chacun des intervalles …, $f$ est
  une fonction polynôme », jamais « coïncide avec ».
- **Ne pas donner la réponse dans l'énoncé** : par exemple, pas de
  « (ici x = −∛3) » après une question d'existence.
- **Figures** : graphiques en TikZ, avec des coordonnées calculées exactement ;
  points pleins et points creux pour les discontinuités.
- **Tableaux de variations** : utiliser `tkz-tab`.
- **Tableaux à compléter** (dichotomie, valeurs…) : colonnes assez larges
  pour écrire, en-têtes en gras, sans couleur de fond.
- **Python** : `listings`, avec des pointillés `............` pour les parties
  à compléter.
- **Listes de cas courts** (par exemple 4 fonctions par morceaux) : les mettre
  sur deux colonnes avec `multicols`.

## Mise en page (exigences du professeur)

- **Espacement aéré** : `\setstretch{1.25}`, déjà réglé dans le modèle.
- **Titres jamais isolés** : un titre de partie ou d'exercice ne doit jamais
  se retrouver seul en bas de page. Le modèle le gère avec `\needspace`.
- **Aucune page à moitié vide**, sauf la dernière. Le modèle redéfinit
  `\needspace` et met à zéro `\@secpenalty`, `\@beginparpenalty`,
  `\@endparpenalty` et `\@itempenalty`. Sinon, les pénalités négatives de
  LaTeX attirent les sauts de page trop tôt. **Ne pas retirer ce réglage.**
- **Si une page reste trop vide**, ajuster localement :
  - réduire un peu une figure ou un tableau ;
  - passer une liste en deux colonnes ;
  - garder un énoncé avec son tableau dans une `minipage` ;
  - fusionner deux questions courtes.

  Ne jamais ajouter de `\newpage` arbitraire.
- **Viser des pages pleines** : 1 page pour environ 2 exercices (la fiche de
  référence fait 7 pages pour 15 exercices).

## Compilation

- **Prérequis** : une distribution LaTeX avec `pdflatex` (MiKTeX ou TeX
  Live). Paquets utilisés : `tcolorbox`, `tikz`, `tkz-tab`, `titlesec`,
  `needspace`, `setspace`, `fancyhdr`, `lastpage`, `listings`, `multicol`,
  `babel` (français).
- **Script** : `scripts/compiler.py` compile deux fois (pour « page/total »),
  liste les alertes et crée la planche de contrôle (`pdftoppm` et Pillow sont
  nécessaires pour la planche).
