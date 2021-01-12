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
* **Description (fr)**: la description en français. Sauf si vous savez ce que vous faites et connaissez les balises, vous reprenez les balises anglaises Les balises sont les instructions données qui permettent la mise en page du texte.

Exemple de fichier à traduire:

```yaml
Name: Cast a Spell
Nom: 
État: aucune

------ Description (en) ------
<p><span id="ctl00_MainContent_DetailedOutput">You cast a spell you have prepared 
or in your repertoire. Casting a Spell is a special activity that takes a variable number 
of actions depending on the spell, ...</span></p>
------ Description (fr) ------

```
Dans ce cas, on reprend le texte officiel s'il existe ou on fait la traduction. 
Ici, Lancer un sort possède une traduction officielle publiée dans le livre de base édité par BBE. On reprend alors ce texte sans fantaisie et on indique officielle en face de l'état.

Cela donnera 
```yaml
Name: Cast a Spell
Nom: Lancer un sort
État: officielle

------ Description (en) ------
<p>You cast a spell you have prepared or in your repertoire. Casting a Spell is a special activity that takes a variable number of actions depending on the spell, as listed in each spell's stat block. As soon as the spellcasting actions are complete, the spell effect occurs.
<ul>
<li>Material (manipulate)</li>
<li>Somatic (manipulate)</li>
<li>Verbal (concentrate)</li>
<li>Focus (manipulate)</li>
</ul>
<p><strong>Disrupted and Lost Spells</strong> Some abilities and spells can disrupt a spell, causing it to have no effect and be lost. When you lose a spell, you've already expended the spell slot, spent the spell's costs and actions, and used the Cast a Spell activity. If a spell is disrupted during a <a class="entity-link" draggable="true" data-pack="pf2e.actionspf2e" data-id="3f5DMFu8fPiqHpRg"> Sustain a Spell</a> action, the spell immediately ends. The full rules for disrupting actions appear on page 462.</p>
------ Description (fr) ------
<p>Vous lancez un sort que vous avez préparé ou qui figure dans votre répertoire. Lancer un sort est une activité spéciale qui demande un nombre d’actions variable en fonction du sort. Ce nombre figure dans le bloc de statistiques de chaque sort. L’effet du sort se produit dès que les actions d’incantation sont accomplies. </p>
<ul>
<li>Matériel (manipulation)</li>
<li>Somatique (manipulation)</li>
<li>Verbal (concentration)</li>
<li>Focaliseur (manipulation)</li>
</ul>
<p><strong>Sorts interrompus et perdus</strong> Certains sorts et pouvoirs permettent d’interrompre un sort, qui est alors perdu et n’a aucun effet. Quand vous perdez un sort, vous avez déjà dépensé son emplacement de sort, son coût et ses actions et déjà utilisé l’activité Lancer un sort. Si un sort est interrompu lors de l’action <a class="entity-link" draggable="true" data-pack="pf2e.actionspf2e" data-id="3f5DMFu8fPiqHpRg">Maintenir un sort</a>, alors ce sort se termine de suite. Vous pouvez consulter les règles complètes concernant les actions d’interruption.</p>

```


Exemple de fichier traduit à partir de la source officielle qui a été changé. Ici par exemple, les anglophones ont créé un nouveau champ de prérequis.

```yaml
Name: Graceful Poise
Nom: Aisance gracieuse
PrereqEN: Double Slice
PrereqFR: 
État: changé
État d'origine: officielle

------ Description (en) ------
<p>With the right positioning, your off-hand weapon can strike like a scorpion's stinger. While you are in this stance, if you make your second Strike from Double Slice with an agile weapon, Double Slice counts as one attack when calculating your multiple attack penalty.</p>
------ Description (fr) ------
<p><strong>Prérequis</strong> Double taille</p>
<hr>
<p>En prenant la bonne position, votre main secondaire peut frapper comme le fait un scorpion avec son dard. Tant que vous gardez cette posture, si vous effectuez votre deuxième Frappe grâce à Double taille avec une arme agile, la Double taille compte comme une attaque dans le calcul de votre malus d’attaques multiples.</p>
```

Il faut indiquer le prérequis, indiquer officielle en face de l'État et supprimer la ligne État d'origine. Cela donnera
```yaml
Name: Graceful Poise
Nom: Aisance gracieuse
PrereqEN: Double Slice
PrereqFR: Double taille
État: officielle

------ Description (en) ------
<p>With the right positioning, your off-hand weapon can strike like a scorpion's stinger. While you are in this stance, if you make your second Strike from Double Slice with an agile weapon, Double Slice counts as one attack when calculating your multiple attack penalty.</p>
------ Description (fr) ------
<p>En prenant la bonne position, votre main secondaire peut frapper comme le fait un scorpion avec son dard. Tant que vous gardez cette posture, si vous effectuez votre deuxième Frappe grâce à Double taille avec une arme agile, la Double taille compte comme une attaque dans le calcul de votre malus d’attaques multiples.</p>
```
