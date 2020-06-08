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
  * [Backgrounds](data/status-backgrounds.md)
  * [Classes](data/status-classes.md)
  * [ancestry features](data/status-ancestryfeatures.md)
  * [Équipment](data/status-equipment.md)
  * [Dons](data/status-feats.md)
  * [Sorts](data/status-spells.md)

## Utilisation

Pour appliquer les traductions, il faut installer le module Babele et pointer vers le répertoire [babele](babele/). Instructions détaillées
* [Prérequis] Installer et activer le module [Babele](https://gitlab.com/riccisi/foundryvtt-babele)
* Installer ce module manuellement avec le manifest `https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/raw/master/module.json`
* Configurer Babele pour pointer les traductions vers le répertoire `modules/pf2-fr/babele`
* Configuration alternatives possibles:
  * `modules/pf2-fr/babele-alt/vf-vo`: noms au format "nom fr (nom en)" et description fr
  * `modules/pf2-fr/babele-alt/vo-vf`: noms au format "nom en (nom fr)" et description fr
  * `modules/pf2-fr/babele-alt/vo`: noms conservés dans leur version originale (en) mais description en français
* Enjoy!

## Ressources utiles
[Glossaire](https://docs.google.com/spreadsheets/d/1MmY9rB7EU1yjpPmmoDdqgawiA46fetS_NBCC0Ay7zsw/edit#gid=508492121)

## Bugs de la vo
* Golem Crafter Dedication is a wrong name -> The good one is Golem **G**rafter Dedication
* Dedication feats frome the base classes of the core are in class feats -> archetype feats
* Bard dedication : the special part is missing
* Druid dedication : the special part is missing
* Magaambyan Attendant Dedication -> archetype feat
* Primal Hierophant -> class feature of level 19, not 03
