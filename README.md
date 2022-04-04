# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).  

Le module permet d'utiliser les données des objets permettant de jouer sous Foundry à Pathfinder2, le jeu de rôles développé par Paizo. Il vous permet de disposer de la description des objets figurant dans les compendiums anglophones traduits en français. Il vous permet alternativement de pouvoir disposer d'un affichage du nom de chaque objet en vo-vf ou en vf-vo avec la description en vf pour faciliter la recherche et permettre de favoriser les tables qui utilisent le français et l'anglais.  

Le module rend indispensable d'utiliser les modules  
1. Babele, ce module est nécessaire assure la prise en charge de la traduction
2. PF2e system, ce module est nécessaire pour charger les compendium de données du système de jeu qui sont traduites
3. PF2e animal compendia, ce module est nécessaire pour charger les compendium de données propres aux différents compagnons (créature de l'inventeur, compagnon animal du druide ou du rodeur et eidolon du conjurateur) 

Le module ne prend en charge que la traduction des compendium des données. Il est complémentaire de celui qui permet de disposer de la version française de l'interface utilisateur du système pf2 et notamment de la feuille de personnage en français et des cartes affichées en français. L'interace utilisateur fait l'objet d'un module distinct.

Cette dualité permet aux francophones de jouer avec les données en vo tout en disposant de l'interface de jeu en français ou vice versa.

**En aucun cas, Paizo ou Black Book Editions ne reconnaîssent, ne sont à l'origine ou ne sont les mécènes de ce projet.**

La gamme Pathfinder est une création de **Paizo Publishing**. Elle fait l'objet d'une publication officielle en français par **Black Book Editions**.

La traduction est réalisée en application des licences Open Game License (ogl) et Pathfinder Community Use Policy (PCUP). Elle est destinée à l'utilisation du système Pathfinder 2e avec le logiciel Foundry VTT.

Si vous entendez utiliser les traductions réalisées à d'autres fins, vous devez respecter les licences ogl et PCUP et demander l'autorisation des traducteurs. 

Vous ne pouvez notamment pas utiliser ces traductions à des fins commerciales.

- La traduction du Livre de base est, pour l'essentiel, la reprise de la traduction officielle qui a été réalisée en français par Black Book Edition.
- La description des monstres du Bestiaire 1 est également issue de la traduction officielle.
- La traduction des objets du Guide du Maître est également issue de la traduction officielle.

Les traductions officielles qui ont été utilisées ont été l'objet d'un travail complémentaire des contributeurs du système pour supprimer les références des pages, y insérer les liens nécessaires pour naviguer dans lee logiciel Foundry entre les objets, réaliser les automatisations permises par le système. Les fichiers ont fait l'objet de l'insertion progressive des erratas publiés par Paizo. 

Certains textes ont aussi été légèrement repris par souci de cohérence dans l'utilisation de certains mots ou lorsque la traduction n'a pas parue la mieux adaptée ou lorsqu'elle est erronée, notamment pour appliquer les erratas.

Le reste de la traduction des fichiers anglophones qui vous est proposée dans ce module est le fruit du travail passionné de membres de la communauté qui ont pour objectif d'assurer la traduction des ouvrages Paizo au rythme de leur parution.

## Note aux traducteurs 

* Les fichiers à traduire ou à corriger se trouvent dans le répertoire [data](data/).

* Chaque fichier correspond à une entrée traduite ou à traduire
  * Pour chaque fichier, vous disposez de plusieurs champs en anglais et en français,
  * Les textes d'origine en anglais doivent rester inchangés ! (ils permettent à un script d'effectuer automatiquement une comparaison entre le contenu de l'extraction et une éventuelle mise à jour anglophone. Cela permet de prendre en compte les évolutions dans l'automatisation, les oublis et les éventuels erratas),
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les instructions de traduction et de modifications pour ceux qui veulent pouvoir y contribuer.

* Pour voir l'état d'avancement des différentes traductions, vous pouvez consulter les fichiers qui se terminent par **.md** dans le répertoire data classés par thèmes.

## Utilisation sous Foundry

Pour appliquer les traductions dans votre système, il existe un prérequis logiciel. Il vous faut installer le module intitulé [Babele](https://gitlab.com/riccisi/foundryvtt-babele) qui a été créé par Simone Riccisi. Ce module réalise une cartogaphie des fichiers, repère les parties anglaises qu'il faut substituer avec les traductions proposées en français.

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

À partir des traductions, l'extraction complète au fil du temps et des publications a permis de disposer d'un [Glossaire](data/dictionnaire.md) qui vous donne le nom utilisé en anglais, le nom utilisé en français avec l'ID (l'identifiant du fichier qui permet d'insérer ailleurs un lien réutilisable pour faciliter la navigation). Ce dictionnaire est aussi disponible en partant du français pour disposer de la traduction en anglais.

## Bugs de la vo
Les erreurs que vous trouvez dans les textes en vo peuvent être remontées sur le projet anglophone en créant une "issue" sur le système en décrivant la phrase erronée et la phrase que vous proposez. Le mieux est de donner le numéro du fichier, suivie de sa traduction et indiquer en quoi il est incorrect, le tout dans la langue anglaise. Au pire, remontez l'information sur le discord du projet où un contributeur du système pourra vous relayer.

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

À jour au 04 avril 2022
