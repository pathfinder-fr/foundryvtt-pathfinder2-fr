# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).  
Le module permet d'utiliser pathfinder2 en français en disposant des données des compendiums traduits. Les traductions sont officielles lorsque cela a été possible et libre lorsque les traducteurs n'ont pas disposé des textes traduits en français.  
Ce module est complémentaire de la version française du système pf2 qui est nécessaire pour disposer de l'interface en français.  

## Traducteurs

* Les fichiers à traduire ou à corriger se trouvent dans le répertoire [data](data/)

* Chaque fichier correspond à une entrée traduite ou à traduire
  * Pour chaque fichier, vous disposez de plusieurs champs en anglais et en français.
  * Ne pas supprimer les textes d'origine en anglais qui doivent rester inchangés! (ils permettent au système d'effectuer automatiquement une comparaison entre deux mises à jour anglophones pour prendre en compte les évolutions et les erratas)
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les instructions de traduction et de modifications

* Pour voir l'état d'avancement des différentes traductions, vous pouvez consulter les fichiers qui se terminent par **.md** dans le répertoire data dont les principaux sont :
  * [capacités d'ascendance](data/status-ancestryfeatures.md)
  * [Historiques](data/status-backgrounds.md)
  * [Classes](data/status-classes.md)
  * [capacités de classe](data/status-classfeatures.md)
  * [Équipement](data/status-equipment.md)
  * [Dons](data/status-feats.md)
  * [Sorts](data/status-spells.md)
  * [Actions](data/status-actions.md)

## Utilisation sous Foundry

Pour appliquer les traductions dans votre système, il existe un prérequis.
Il faut installer le module intitulé **Babele**, puis définir le répertoire vers lequel il ira chercher vos données en français pour les substituer aux données en anglais [babele](babele/). Instructions détaillées
* [Prérequis] **Installer** et **activer** le module [Babele](https://gitlab.com/riccisi/foundryvtt-babele)
* Il faut ensuite télécharger ce module qui peut être facilement trouvé en cherchant PF2 en français ou être installé manuellement en rentrant l'adresse du manifest `https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/raw/master/module.json`
* Il vous faut ensuite configurer Babele pour pointer les traductions vers le répertoire `modules/pf2-fr/babele`
* Plusieurs configurations alternatives sont possibles selon vos envies:
  * `modules/pf2-fr/babele-alt/vf-vo`: noms au format "nom fr (nom en)" et description fr
  * `modules/pf2-fr/babele-alt/vo-vf`: noms au format "nom en (nom fr)" et description fr
  * `modules/pf2-fr/babele-alt/vo`: noms conservés dans leur version originale (en) mais description en français
* Enjoy!

L'utilisation vo/vf et vf/vo peut amener un décalage dans l'affichage de la feuille de personnage qui n'empêche pas de jouer.

Vous pouvez remonter les erreurs de traduction, les typos, les erratas sur le discord du projet

## Ressources utiles
À partir des traductions, l'extraction complète au fil du temps et des releases permet de disposer d'un [Glossaire](data/dictionnaire.md) qui donne le nom en anglais, le nom en français de chaque donnée avec l'ID (le nom du fichier qui permet d'en faire un lien réutilisable ailleurs pour faciliter la navigation)

## Bugs de la vo
Les erreurs dans les textes en vo peuvent également être remontées sur le projet de Hooking en créant une "issue". Le mieux est de donner le numéro du fichier, suivie de sa traduction et indiquer en quoi il est incorrect, le tout dans la langue anglaise.

À jour au 7 juillet 2021

