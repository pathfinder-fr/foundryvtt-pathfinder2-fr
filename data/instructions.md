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
  * *changé* cette entrée indique que le fichier anglais d'origine dont l'extraction est reprise a évolué. Cela peut être une modification dans les liens ajoutés ou modifiés, dans le texte en vo qui a été erratisé, dans l'automatisation qui est ajoutée pour permettre de lancer les dés directement sous Foundry. Lorsque c'est le cas, cela nécessite une vérification et une reprise des modifications en français. Si on modifie le fichier pour reprendre les modifiations, il faut alors supprimer le champ ci-dessous et remplacer par l'ancienne valeur libre ou officielle trouvé dans l'État antérieur.
* **État antérieur**: ce champ n'existe que s'il y a au dessus un état _changé_. Ce champ peut prendre l'une des deux valeurs suivantes libre ou officielle. Cela signifie qu'avant le changement, le texte provenait d'une traduction libre ou d'une traduction officielle.
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
