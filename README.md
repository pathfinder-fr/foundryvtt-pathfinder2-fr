# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).
Le module améliore le système pathfinder2 pour le français.

Expérimentations en cours pour:
* Actions

## Traducteurs

* Les fichiers à traduire se trouvent dans le répertoire [data](data/)
* Chaque fichier correspond à une entrée à traduire
  * Pour chaque fichier, il faut inscrire le nom et la description en se basant sur les textes d'origine (en anglais)
  * Ne pas supprimer les textes d'orgine!
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les fichiers de traduction
* Pour voir l'état d'avancement des traductions:
  * [Actions](data/status-actions.md)
  * [Classes](data/status-classes.md)
  * [Équipment](data/status-equipment.md)
  * [Dons](data/status-feats.md)
  * [Sorts](data/status-spells.md)

## Utilisation

Pour appliquer les traductions, il faut installer le module Babele et pointer vers le répertoire [babele](babele/). Instructions détaillées
* [Prérequis] Installer et activer le module [Babele](https://gitlab.com/riccisi/foundryvtt-babele)
* Installer ce module manuellement avec le manifest `https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/raw/master/module.json`
* Configurer Babele pour pointer les traductions vers le répertoire `modules/pf2-fr/babele`
* Enjoy!

## Ressources utiles
https://docs.google.com/spreadsheets/d/1MmY9rB7EU1yjpPmmoDdqgawiA46fetS_NBCC0Ay7zsw/edit#gid=508492121

## Bugs de la vo
Le don Golem Crafter Dedication est erroné -> il s'agit de Golem **G**rafter Dedication