# Projet 03 : Aidez Mac Gyver à s'echapper

- [Projet 03 : Aidez Mac Gyver à s'echapper](#projet-03--aidez-mac-gyver-%C3%A0-sechapper)
    - [Introduction](#introduction)
    - [Environnement de développement](#environnement-de-d%C3%A9veloppement)
    - [Choix de programmation](#choix-de-programmation)
    - [Structure du code](#structure-du-code)
    - [Difficultés rencontrées](#difficult%C3%A9s-rencontr%C3%A9es)
    - [Conclusion](#conclusion)

## Introduction

Le projet constiste à développer un jeu de labyrinthe en 2D avec les fonctionnalités suivantes :

- un seul niveau, mais dont la structure doit être dans un fichier facilement modifiable;
- le personnage doit être contrôlé par les touches directionnelles du clavier;
- les objets doivent réparti aléatoirement dans le labyrinthe à chaque démarrage du jeu;
- le labytinthe doit être un carré de 15x15 cases;
- les objets sont récupérés en passant dessus;
- le programme s'arrête quand on est face au gardien. Si on a tous les objets on gagne, sinon on perd.

**Attention :** Le programme doit être standalone et codé uniquement en anglais et dans le respect des bonnes pratiques de la [PEP8](https://www.python.org/dev/peps/pep-0008/).

Code source : <https://github.com/vincenthouillon/macgyver-maze-game">

## Environnement de développement

- Python 3.6.4
- pygame 1.9.4
- Visual Studio Code
- Windows 10 & Linux Mint 18.3

## Choix de programmation

Utilisation de randint(random) pour définir les positions aléatoires des objets et vérification que les cases ne soient pas des murs ou un gardien :

```python
loot = 0
while loot < len(OBJECTS):
    x_object = randrange(0, SPRITE_NUMBER)
    y_object = randrange(0, SPRITE_NUMBER)

    if maze_structure[y_object][x_object] == " ":
        maze_structure[y_object][x_object] = OBJECTS[loot]
        loot += 1
```

Méthode pour récupérer la case de départ de Mac Gyver dans le fichier texte 'labyrinth_scheme.txt', permet de configurer facilement la position de départ du labyrinthe :

```python
def __get_position_mac(self):
"""Private method for get the macgyver position."""
    line_number = 0
    for line in self.structure:
        case_number = 0
        for sprite in line:
            pos_x = case_number
            pos_y = line_number
            if sprite == "s":
                self.macgyver_pos = (pos_x, pos_y)
            case_number += 1
                line_number += 1
```

## Structure du code

Arborescence du dépôt git :

- **includes** _(dossier contenant les éléments nécessaires au jeu)_
  - **font** _(contient la police d'écriture et sa licence)_
    - IndieFlower.ttf _(police utilisée dans je jeu pour la liste des objets et les messages de fin du jeu)_
    - OFF.txt _(licence de police d'écriture)_
  - **img** _(dossier contenant les images utilisées dans le jeu (fournis avec le cahier des charges))_
    - aiguille.png
    - ether.png
    - floor-tiles-20x20.png
    - Gardien.png
    - MacGyver.png
    - tube_plastique.png
    - etc.
  - `classes.py` _(génération du labyrinthe à partir du fichier texte et mise en place alétoire des objets à collecter)_
  - `constants.py` _(contient les paramètres du jeu)_
  - `labyrinth_scheme.txt` _(fichier texte définissant la structure du labyrinthe)_
  - `macgyver.py` _(gestion des déplacements de Mac Gyver)_
- `macgyver_maze_game.py` _(programme principal)_
- `README.md` _(fiche de présentation du jeu notamment pour Github)_
- `requirements.txt` _(pour installer les packages externes nécessaires au jeu)_
- `setup.py` _(script pour la création d'un exécutable pour Windows, voir `README.md`)_

## Difficultés rencontrées

Les échanges de données entre les méthodes, attributs et propriétés des différentes classes du programme.

Bien assimiler le fonctionnement de pygame, savoir quand gerer les différents affichages, événements, etc dans le programme.

Ne voulant pas 'hardcoder' (coder en dur) la position de Mac Gyver, il a fallu trouver une méthode pour récupérer la position indiquée dans le fichier texte et qu'elle soit accessible par la classe "macgyver" qui gère les déplacements du personnage.

## Conclusion

Pour un débutant, c'est un exercice qui réclame que l'on ait une bonne vue d'ensemble de son projet. Qui demande de bien assimiler le fonctionnement de pygame, à savoir quand gerer les différents affichages, événements, etc. Et nous démontre la puissance et la complexité qu'est la Programmation Orientée Objets.
