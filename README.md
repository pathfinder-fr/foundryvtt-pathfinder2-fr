# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).  
Le module permet de disposer des compendiums du système de jeu Pathfinder2 développé par Paizo en français en disposant des données des compendiums anglophones traduits soit en version française intégrale, soit en vo-vf ou en vf-vo pour améliorer la recherche et favoriser les tables qui utilisent plusieurs langues.  
Le module rend nécessaire l'utilisation du module Babele

Ce module est complémentaire du module qui vous permet de disposer de la version française du système pf2. Le module du système est nécessaire pour disposer de l'interface en français. Il fait l'objet d'un module distinct pour permettre aux francophones de jouer en vo en disposant de l'interface en français tout en disposant du contenu en anglais.

- La traduction du Livre de base est pour l'essentiel la reprise de la traduction officielle réalisée par Black Book Edition.
- La description des monstres du Bestiaire 1 est la traduction officielle.
- La traduction du compendium du Guide du Maître

Les traductions officielles ont cependant été l'objet d'un travail complémentaire des contributeurs du système pour supprimer les références des pages, insérer les liens nécessaires pour naviguer sous Foundry, réaliser les automatisations permises par le système. 

Les fichiers font l'objet de l'insertion progressive des erratas publiés par Paizo. 

Certains textes ont aussi été légèrement repris par souci de cohérence dans l'utilisation de certains mots ou lorsque la traduction n'a pas parue la mieux adaptée ou erronée.

Le reste de la traduction qui est proposée est pour le reste le fruit du travail des fans qui ont assuré la traduction des livres ultérieurs. L'objectif est de rester à jour de la traduction anglophone pour pouvoir continuer à jouer au rythme de la parution des aventures publiées par Paizo.

En aucun cas, le fuit de ce site n'est un site officiel de Paizo ou de Black Book Editions. 


La gamme Pathfinder est une création de Paizo Publishing. Elle fait l'objet d'une publication en français par Black Book Editions.

La traduction est réalisée en application des licences Open Game License (ogl) et Pathfinder Community Use Policy (PCUP).


## Traducteurs

* Les fichiers à traduire ou à corriger se trouvent dans le répertoire [data](data/)

* Chaque fichier correspond à une entrée traduite ou à traduire
  * Pour chaque fichier, vous disposez de plusieurs champs en anglais et en français.
  * Les textes d'origine qui se trouvent en anglais doivent rester inchangés! (ils permettent à un script d'effectuer automatiquement une comparaison entre le contenu de l'extraction et d'une éventuelle mise à jour anglophone. Cela permet de prendre en compte les évolutions dans l'automatisation, les oublis et les éventuels erratas)
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les instructions de traduction et de modifications pour ceux qui veulent pouvoir contribuer

* Pour voir l'état d'avancement des différentes traductions, vous pouvez consulter les fichiers qui se terminent par **.md** dans le répertoire data classés par thèmes.

## Utilisation sous Foundry

Pour appliquer les traductions dans votre système, il existe un prérequis logiciel. Il vous faut installer le module intitulé [Babele](https://gitlab.com/riccisi/foundryvtt-babele) qui a été créé par Simone Riccisi. Ce logiciel réalise une cartogaphie des fichiers, repère les parties anglaises qu'il faut substituer avec les traductions proposées.

Une fois ces deux modules installés et activés, il vous faut remplir le chemin du répertoire dans lequel Babele poura aller chercher vos données en français [babele](babele/). 

Instructions détaillées 
* Dans Foundry, dans l'onglet Modules, cliquer sur Installer un module
* Chercher Babele, **Installer**
* Revenir dans l'onglet Module
* Chercher le module PF2 en français ou entrer manuellement l'adresse du manifeste du module : `https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/raw/master/module.json`
* Il vous faut ensuite configurer Babele pour pointer les traductions vers le répertoire `modules/pf2-fr/babele`
* Plusieurs configurations alternatives sont possibles selon vos envies:
  * `modules/pf2-fr/babele-alt/vf-vo`: noms au format "nom fr (nom en)" avec le contenu traduit en français
  * `modules/pf2-fr/babele-alt/vo-vf`: noms au format "nom en (nom fr)" avec le contenu traduit en français
  * `modules/pf2-fr/babele-alt/vo`: noms conservés dans leur version originale (en) mais avec le contenu en français
* Il ne vous reste qu'à en profiter !

L'utilisation vo/vf et vf/vo peut parfoir amener des décalages inesthétiques dans l'affichage du système qui n'empêchent pas de jouer mais que vous pouvez remonter aux contributeurs du système pour qu'ils tentent de remédier. Vous pouvez également remonter les erreurs de traduction, les typos, les erratas sur le discord du projet

## Ressources utiles

À partir des traductions, l'extraction complète au fil du temps et des publications a permis de disposer d'un [Glossaire](data/dictionnaire.md) qui vous donne le nom utilisé en anglais, le nom utilisé en français avec l'ID (l'identifiant du fichier qui permet d'insérer ailleurs un lien réutilisable pour faciliter la navigation)

## Bugs de la vo
Les erreurs que vous trouvez dans les textes en vo peuvent également être remontées sur le projet anglophone en créant une "issue". Le mieux est de donner le numéro du fichier, suivie de sa traduction et indiquer en quoi il est incorrect, le tout dans la langue anglaise. Au pire, remontez l'information sur le discord du projet où un contributeur du système pourra vous relayer.

## Génération des données standard - projet pf2-data-fr

Le script `update-pf2datafr.py` est responsable de la génération des fichiers pour le projet [pf2-data-fr](https://gitlab.com/pathfinder-fr/pf2-data-fr).

Si vous souhaitez que le projet [pf2-jekyll](https://gitlab.com/pathfinder-fr/pf2-jekyll/) puisse utiliser des données du module, ce sont ces instructions qu'il faut suivre.

Avant de modifier le script, il faut déterminer si la donnée est réellement manquante.
Allez sur le projet pf2-data-fr, ouvrez le fichier json qui correspond au type de données extraites et vérifiez que la valeur est bien présente.

Si la valeur est déjà présente, alors c'est le projet pf2-jekyll qu'il faut modifier pour charger cette donnée.
Si la valeur n'est pas présente, c'est ce script qu'il faut changer.

Si la valeur est une valeur "technique", il n'est pas nécessaire de partir du fichier de traduction : il suffit de charger la donnée depuis le JSON anglais.
Il faut aller modifier la partie "Récupération données fichier json anglais" du script de génération, et ajouter la propriété dans la variable dataJson à partir du fichier anglais.
Si la donnée n'est pas présente dans le JSON anglais, cela veut dire qu'elle n'existe pas.

Si la valeur est une donnée traduite (ex: traduction d'une phrase de portée de sort, traduction d'un avantage de don), alors il faut recopier la donnée depuis la traduction FR.
Il faut vérifier si la donnée traduite existe depuis les fichiers du dossier "data", et ensuite modifier la partie "Récupération données fichier .htm français" pour charger cette donnée.
Si la donnée n'est pas présente dans le fichier .htm du dossier data, c'est que la donnée n'est pas gérée en traduction.

## Ajout de données à extraire pour traduction

S'il est décidé qu'un autre champ du JSON anglais du fichier d'origine doit faire l'objet d'une traduction, c'est le fichier libdata.py qui doit être modifié, et en particulier les packs (variable SUPPORTED)

- si le champ JSON correspond à une liste, il faut ajouter le chemin de l'élément JSON tableau dans ̀`lists` (cf. prérequis des dons).
- si le champ JSON correspond à une valeur unique, il faut ajouter le chemin de l'élément JSON dans `extract` (cf. sorts).

## État

À jour au 20 février 2022
