# Projet IA

## Description
Ce projet implémente un jeu de Hex avec différentes stratégies pour les joueurs, y compris humain, random et minimax. Le jeu peut être joué en mode tournoi où différentes stratégies s'affrontent.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Aichael29/projet-ia.git
   cd projet-ia
   ```

2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
Accédez au répertoire source :
```bash
cd projet-ia/source
```

Exécutez le jeu avec les paramètres souhaités :
```bash
python main.py --player [strategy1] --other [strategy2] --size [board_size] --games [num_games]
```

- `strategy1` et `strategy2` peuvent être "humain", "random" ou "minimax".
- `board_size` spécifie la taille du plateau de jeu (par défaut : 7).
- `num_games` spécifie le nombre de parties à jouer dans le tournoi (par défaut : 5).

Exemple :
```bash
python main.py --player human --other random --size 7 --games 5
```

## Résultats du Tournoi
Après avoir exécuté le tournoi, le programme affichera le score final et les taux de victoire pour chaque stratégie.

## Stratégies
### Humain
- Un joueur humain peut participer au jeu en fournissant une entrée pendant son tour.

### Aléatoire
- L'ordinateur effectue des mouvements aléatoires pendant le jeu.

### Minimax
- L'ordinateur utilise une implémentation basique de l'algorithme Minimax pour effectuer des mouvements stratégiques.

## Structure du Code
- `main.py` : Le script principal pour exécuter le jeu et les tournois.
- `classes/` : Répertoire contenant les principales classes du jeu.
  - `strategy.py` : Définit les stratégies des joueurs.
  - `tournament.py` : Implémente la logique du tournoi.
- `requirements.txt` : Liste des dépendances du projet.

## Développeurs
- aicha elfelchaoui & firas boustila
