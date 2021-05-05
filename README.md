# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).
Le module améliore le système pathfinder2 pour le français.

[![pipeline](https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/badges/master/pipeline.svg?style=flat-square&key_text=validité%20traduction&key_width=130)](https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/commits/master)

## Traducteurs

* Les fichiers à traduire ou à corriger se trouvent dans le répertoire [data](data/)

* Chaque fichier correspond à une entrée à traduire
  * Pour chaque fichier, vous disposez de plusieurs champs en anglais et en français.
  * Ne pas supprimer les textes d'origine qui doivent rester inchangés! (ils permettent la comparaison entre deux mises à jour pour prendre en compte les évolutions)
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les instructions de traduction et de modifications

* Pour voir l'état d'avancement des différentes traductions, consultez les fichiers en .md dans les data :
  * [capacités d'héritage](data/status-ancestryfeatures.md)
  * [Historiques](data/status-backgrounds.md)
  * [Classes](data/status-classes.md)
  * [capacités de classe](data/status-classfeatures.md)
  * [Équipement](data/status-equipment.md)
  * [Dons](data/status-feats.md)
  * [Sorts](data/status-spells.md)
  * [Actions](data/status-actions.md)

## Utilisation sous Foundry

Pour appliquer les traductions, il faut installer le module Babele et pointer vers le répertoire [babele](babele/). Instructions détaillées
* [Prérequis] Installer et activer le module [Babele](https://gitlab.com/riccisi/foundryvtt-babele)
* Ce module peut être trouvé en cherchant PF2 en français ou être installé manuellement avec le manifest `https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/raw/master/module.json`
* Il faut ensuite configurer Babele pour pointer les traductions vers le répertoire `modules/pf2-fr/babele`
* Plusieurs configurations alternatives sont possibles selon vos envies:
  * `modules/pf2-fr/babele-alt/vf-vo`: noms au format "nom fr (nom en)" et description fr
  * `modules/pf2-fr/babele-alt/vo-vf`: noms au format "nom en (nom fr)" et description fr
  * `modules/pf2-fr/babele-alt/vo`: noms conservés dans leur version originale (en) mais description en français
* Enjoy!

L'utilisation vo/vf et vf/vo peut amener un décalage dans l'affichage de la feuille de personnage qui n'empêche pas de jouer

## Ressources utiles
À partir des traductions, l'extraction complète au fil du temps et des releases un [Glossaire](data/dictionnaire.md) qui permet de disposer du nom en anglais, du nom en français et de l'ID (le nom du fichier qui permet d'en faire un lien réutilisable ailleurs)

## Bugs de la vo
Les erreurs dans les textes en vo peuvent être remontées sur le projet de Hooking en créant une "issue". Le mieux est de donner le numéro du fichier, suivie de sa traduction et indiquer en quoi il est incorrect

À jour au 6 avril 2021

