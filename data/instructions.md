# Instructions pour l'édition des fichiers

* **Name**: le nom original en anglais. Ne pas modifier ce texte ni retirer la ligne!
* **Nom**: le nom en français
* **PrereqEN**: les prérequis en anglais. Ne pas modifier le texte ni retirer la ligne!
* **PrereqFR**: traduisez les prérequis anglais en séparant par une barre verticale (obtenue par AltGr+6) uniquement s'il y a des prérequis en anglais
* **État**: l'état de la traduction. Peut prendre l'une des valeurs suivantes:
  * *aucune*: traduction manquante / à faire
  * *libre*: traduction libre
  * *officielle*: traduction officielle
  * *doublon*: cette entrée sera simplement ignorée
* **Description (en)**: la description d'origine en anglais. Ne pas modifier le texte ou supprimer.
* **Description (fr)**: la description en français

Exemple de fichier traduit:
```yaml
Name: Cast a Spell
Nom: Jeter un sort
État: libre

------ Description (en) ------
<p><span id="ctl00_MainContent_DetailedOutput">You cast a spell you have prepared 
or in your repertoire. Casting a Spell is a special activity that takes a variable number 
of actions depending on the spell, ...</span></p>
------ Description (fr) ------
<p><span id="ctl00_MainContent_DetailedOutput">Vous lancez un sort que vous avez préparé 
ou dans votre répertoire. Lancer un sort est une activité spéciale qui prend un nombre variable 
d'actions en fonction du sort, ... <span></p>
```
