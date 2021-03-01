# Proposition système d'export

Actuellement ce projet contient la traduction des données techniques du module Foundry VTT.
On parle de donnée technique pour désigner toutes les données qui sont rangées sous forme de listes par "type" : monstres, classes, archétypes, équipement, sorts, etc.

On souhaite générer un SRD Pathfinder 2 en utilisant les traductions techniques déjà faites pour Foundry.
Le SRD utilise un format markdown pour le contenu + entêtes YAML (front matter) pour des données normalisées techniques (ex: [action deviner les intentions](https://gitlab.com/pathfinder-fr/pf2-jekyll/-/blob/master/_actions/deviner-les-intentions.md))

Ce SRD aura besoin des informations textuelles, mais aussi des informations techniques de chaque élément.
Par exemple pour les sorts on voudra connaître les différentes composantes, écoles, etc.
Pour les actions on souhaitera connaître le type, le nombre d'actions, les prérequis, etc.

Pour l'instant, le SRD utilise [ses propres scripts](https://gitlab.com/pathfinder-fr/pf2-jekyll/-/tree/master/_scripts) qui récupèrent certaines informations du module anglais (données techniques) et les traduction depuis ce projet.

L'inconvénient de ce système est que ces scripts ne sont écrits qu'avec la vision du SRD.
Si un autre projet (par exemple une adaptation de [easytools](http://www.pf2.easytool.es/) en français) souhaite voir le jour, il sera obligé de créer ses propres scripts pour générer des données pour le site.

L'objectif ici est donc de centraliser ici la génération de fichiers techniques + traduction pour que les autres projets puissent directement utiliser les fichiers.


A partir des données de traduction et des données du module anglais Foundry, on souhaite générer des fichiers standardisés contenant les données techniques + descriptions + traduction fr du nom et description.

- Bonus : standardiser les descriptions pour masquer les particularités de foundry
- Bonus : ne pas nécessiter d'intervention manuelle pour les générer
- Bonus : fournir un fichier json de qualité, en retravaillant certaines données du json anglais
- Ces fichiers serviront pour générer les pages du SRD
- Ces fichiers pourront servir à tout projet souhaitant proposer un outil utilisant les traductions françaises : traduction de [easytools](http://www.pf2.easytool.es/) en français par exemple.

**Retour des traductions.** Autre considération à garder en tête : Le module Foundry pourrait souhaiter réintégrer le contenu du SRD dans le module FR. Cela permettrait de consulter les règles depuis Foundry VTT.
Cela signifie qu'il faut aussi envisager (plus tard) un rappatriement du contenu du SRD (automatisé ?) dans ce projet, avec toutes les problématiques que cela pose : transformation inverse du markdown en HTML foundry, transformation des liens, etc.

## Exemple Actions

* [Repository données anglaises](https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/actions.db)
* [Repository traductions](https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/tree/master/data/actions)

Ci dessous deux exemples qui montrent ce qu'il est possible de faire.

### Exemple 1 - Amélioration json anglais - effort minimum

Dans cette version, on recopie simplement le json anglais et on ajoute les données de traduction françaises

```json
// exemple basé sur balance
// https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/blob/master/packs/data/actions.db/balance.json
{
	// recopie des données anglaises
	"_id": "M76ycLAqHoAgbcej",
    "data": {
        "actionCategory": {
            "value": ""
        },
        "actionType": {
            "label": "Action Type",
            "type": "String",
            "value": "action"
        },
        "actions": {
            "label": "Number of Actions",
            "type": "String",
            "value": "1"
        },
        "description": {
            "chat": "",
            "label": "Description",
            "type": "String",
            "unidentified": "",
            "value": "<p><strong>Requirements</strong> You are in a square that contains a narrow surface, uneven ground, or another similar feature</p>\n<hr />\n<p>You move across a narrow surface or uneven ground, attempting an <pf2-action action='balance' glyph='A'>Acrobatics</pf2-action> check against its Balance DC. You are flat-footed while on a narrow surface or uneven ground.</p>\n<hr />\n<p><strong>Critical Success</strong> You move up to your Speed.</p>\n<p><strong>Success</strong> You move up to your Speed, treating it as difficult terrain (every 5 feet costs 10 feet of movement).</p>\n<p><strong>Failure</strong> You must remain stationary to keep your balance (wasting the action) or you fall. If you fall, your turn ends.</p>\n<p><strong>Critical Failure</strong> You fall and your turn ends.</p><h2 class=\"title\">Sample Balance Tasks</h2>\n<ul>\n<li><strong>Untrained</strong> tangled roots, uneven cobblestones</li>\n<li><strong>Trained</strong> wooden beam</li>\n<li><strong>Expert</strong> deep, loose gravel</li>\n<li><strong>Master</strong> tightrope, smooth sheet of ice</li>\n<li><strong>Legendary</strong> razor's edge, chunks of floor falling in midair </li>\n</ul>"
        },
        "rarity": {
            "value": "common"
        },
        "requirements": {
            "label": "Requirements",
            "type": "String",
            "value": ""
        },
        "rules": [],
        "skill_requirement": {
            "label": "Skill Req.",
            "skill": {
                "rank": "0",
                "skill": "acrobatics",
                "type": "Number"
            },
            "type": "String"
        },
        "skill_requirements": {
            "rank": "",
            "skill": ""
        },
        "source": {
            "label": "Source",
            "type": "String",
            "value": ""
        },
        "traits": {
            "custom": "",
            "label": "Traits",
            "type": "String",
            "value": [
                "move"
            ]
        },
        "trigger": {
            "label": "Trigger",
            "type": "String",
            "value": ""
        },
        "weapon": {
            "label": "Associated Weapon",
            "type": "String",
            "value": ""
        }
    },
    "effects": [],
    "flags": {},
    "img": "systems/pf2e/icons/actions/OneAction.png",
    "name": "Balance",
    "permission": {
        "default": 0
    },
    "type": "action",

	// ajout des données FR
	"traduction": {
		"fr": {
			"name": "Garder l'équilibre",
			"état": "changé",
			"état d'origine": "officielle",
			"description": "<p><strong>Conditions</strong> Vous êtes dans une case contenant une surface étroite, un sol inégal ou un autre élément similaire.</p>\n<hr>\n<p>Vous vous déplacez sur une surface étroite ou sur un sol inégal en effectuant un test d’Acrobaties contre son DD pour Garder l’équilibre. Vous êtes pris au dépourvu lorsque vous êtes sur une surface étroite ou un sol inégal.</p>\n<hr>\n<p><strong>Succès critique</strong> Vous vous déplacez d’une distance maximale égale à votre Vitesse.</p>\n<p><strong>Succès</strong> Vous vous déplacez d’une distance maximale égale à votre Vitesse, en considérant la surface traversée comme un terrain difficile (chaque déplacement de 1,50 m compte comme un déplacement de 3 m).</p>\n<p><strong>Échec</strong> Vous devez rester sur place pour garder l’équilibre (l’action est tout de même dépensée) ou vous chutez. Votre tour prend fin si vous chutez.</p>\n<p><strong>Échec critique</strong> Vous chutez et votre tour prend fin.</p>\n<p>&nbsp;</p>\n<h2 class=&quot;title&quot;>Garder l'équilibre : exemples de tâches</h2>\n<ul>\n<li><strong>Inexpérimenté</strong> enchevêtrement de racines, pavés déchaussés<br><strong>Qualifié</strong> poutre de bois</li>\n<li><strong>Expert</strong> épaisse couche de graviers</li>\n<li><strong>Maître</strong> corde tendue, surface lisse et verglacée</li>\n<li><strong>Légendaire</strong> lame de rasoir, des sections du sol qui s'effondrent brusquement</li>\n</ul>"
		}
	}

}
```

Avantages :

- Très simple à code et mettre en place
- Contient forcément toutes les données disponibles
- Aucune prise de décision sur les données ou le format : aucun risque de faire un mauvais choix

Inconvénients :

- Format du json technique anglais peu standardisé.
  Les nombres sont souvent stockés sous forme de chaînes.
  Répétition de certains valeurs inutiles (ex: "actionType" sur "balance.json" reprend les informations de libellé et de type).
- Informations souvent utiles uniquement pour FoundryVTT (ex: chemin image, permissions)
- Descriptions avec HTML spécifique Foundry
- Plus de travail pour celui qui souhaite se servir des fichiers.

### Exemple 2 - Nouveau fichier spécifique - effort maximum

Dans cette version le fichier json en sortie contient le maximum de données parfaitement normalisées.

On cherche à faire un fichier json le plus standard possible pour éviter tout retravail derrière.

On transforme même la description en Markdown standard pour effacer toute trace du code spécifique foundry.

```json
// exemple basé sur Prodiguer les premiers soins
// EN : https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/blob/master/packs/data/actions.db/administer-first-aid.json
// FR : https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/blob/master/data/actions/MHLuKy4nQO2Z4Am1.htm
{
	// id foundry
	"id": "MHLuKy4nQO2Z4Am1",
	
	// id texte, nom du fichier en anglais
	"id_name": "administer-first-aid",
	
	// nom anglais, basé sur data.name
	"name": "Administer First Aid",
	
	// json anglais : data.actionCategory.value
	"category": "",
	
	// json anglais : data.actionType.value
	"type": "action",
	
	// json anglais : data.actions.value
	// présent ici pour l'exemple : si vide ne pas écrire la propriété
	// passer la valeur en numérique ?
	"actions": 2,
	
	// json anglais : data.description.value
	// On peut transformer le HTML en markdown (optionel car sans doute pas utlisé pour un projet FR).
	// Pour les liens internes, on transforme la syntaxe foundry en lien markdown avec une adresse spéciale sous la forme @category.id-name, permettant d'effacer les spécificités foundry.
	// Cela demande une norme pour générer un id basé sur un nom (remplacement des espaces, caractères spéciaux) qui sera utilisée partout, et une norme pour nommer les catégories (conditionitems et equipement ici) avec une table de correspondance (ex: conditionitems => condition)
	"description": "**Requirements** You're wearing or holding [Healer's Tools](@equipment.healer-s-tools])
	
	----
	
	You perform first aid on an adjacent creature that is [Dying](@conditionitems.dying) or [Bleeding](@conditionitems.persistent-Damage). If a creature is both dying and bleeding, choose which ailment you're trying to treat before you roll. You can Administer First Aid again to attempt to remedy the other effect.
	
	- **Stabilize:** Attempt a Medicine check on a creature that has 0 Hit Points and the dying condition. The DC is equal to 5 + that creature's recovery roll DC (typically 15 + its dying value).
	- **Stop Bleeding**: Attempt a Medicine check on a creature that is taking persistent bleed damage, giving them a chance to make another flat check to remove the persistent damage. The DC is usually the DC of the effect that caused the bleed.
	
	----
	
	**Success** If you're trying to stabilize, the creature loses the dying condition (but remains [Unconscious](@condition.unconscious). If you're trying to stop bleeding, the creature attempts a flat check to end the bleeding.
	
	**Critical Failure** If you were trying to stabilize, the creature's dying value increases by 1. If you were trying to stop bleeding, it immediately takes an amount of damage equal to its persistent bleed damage.",

	// json anglais : data.rarity.value
	"rarity": "common",
	
	// json anglais: data.skill_requirement
	// parfois vide si pas de prérequis, dans ce cas ne pas mettre la balise ?
	"skill_requirement": {
		"skill": "medecine",
		"rank": 0, // passer la valeur en numérique
	},
	
	// json anglais: data.traits.value
	"traits": [
		"manipulate",
		"skill"
	],
	
	// json anglais: data.trigger.value
	// présent ici pour l'exemple : si vide ne pas écrire la propriété
	"trigger": "",
	
	// json anglais: data.weapon.value
	// présent ici pour l'exemple : si vide ne pas écrire la propriété
	"weapon": "",
	
	"lang": {
		"fr": {
			"name": "Prodiguer les premiers soins",

			// on génère un id nom français qui pourra être utilisé dans les liens (cf. description ci-dessous)
			"id_name": "prodiguer-les-premiers-soins",

			// on utilise des termes anglais pour l'état
			"state": "official",

			// on adapte le HTML en markdown et on transforme les liens
			// par rapport à la version d'origine qui utilise les ID, cela signifie qu'il faut une table de correspondance ID foundry <=> nom + algorithme déterministe pour transformer le nom en id nom.
			// autre choix possible : traduire aussi la catégorie : equipment => équipement
			"description": "**Conditions** Vous avez des [instruments de guérisseur](@equipment.outils-de-guérisseur]{instruments de guérisseur}

----

Vous prodiguez les premiers soins à une créature adjacente qui est mourante ou victime de saignements. Si une créature est mourante et victime de saignements, choisissez quelle affection vous voulez soigner avant de faire le test. Vous pouvez Prodiguer les premiers soins à nouveau pour tenter de soigner l’autre affliction.

- **Stabiliser** Faites un test de Médecine sur une créature dans l’état mourant à qui il reste 0 point de vie. Le DD est égal à 5 + le DD du test de récupération de cette créature (pour un total s’élevant le plus souvent à 15 + la valeur de son état mourant).
- **Stopper l'hémorragie** Faites un test de Médecine sur une créature qui subit des dégâts de saignement persistants, ce qui lui permet d’effectuer un autre test nu pour éliminer les dégâts persistants. Le DD est le plus souvent égal à celui de l’effet qui a provoqué le saignement.

----

**Succès** Si vous tentez de la stabiliser, la créature n’a plus l’état mourant (mais elle reste [inconsciente](@condition.inconscient]{inconsciente}). Si vous tentez de stopper l’hémorragie, la créature effectue un test nu pour mettre un terme au saignement.

**Échec critique** Si vous tentez de la stabiliser, la valeur de l’état mourant de la créature augmente de 1. Si vous tentez de stopper l’hémorragie, elle subit immédiatement un montant de dégâts égal à ses dégâts de saignements persistants."
		}
	}
  }
}
```

Avantages :

- Format très neutre, sans spécificités Foundry
- Travail de normalisation
- Très simple à réutiliser
- Peut être repris par d'autres projets de traduction pathfinder2
- Si on transforme la description fr en markdown, permet en cas de résultat bizarre de retravailler le HTML d'origine FR pour avoir qq chose de plus propre.

Inconvénients :

- Travail de normalisation très fort à effectuer
- Décisions à prendre
- Travail de fourmi sur le nettoyage du HTML foundry

Cette solution demande à la fois du travail de création et de suivi des scripts.

Mais une fois les scripts générés et les formats standards acceptés, il est plus facile de contribuer aux scripts pour uniquement gérer (par exemple) une nouvelle tournure de lien HTML, ou bien ajouter une propriété ou corriger une correspondance.

Il y aura donc un gros travail initial de normalisation avec des compétences techniques, mais une fois ce travail effectué, il sera plus simple de contribuer à l'amélioration des scripts.

En gros, si cette solution est choisie, il y aura un travail initial pour créer les premiers scripts et la tuyauterie pour que ce soit au maximum automatisé.

Les scripts devront être écrits pour qu'il soit le plus simple possible aux contributeurs de modifier et améliorer ces scripts:

- Documenter au maximum le code, surtout les parties dictionnaires et correspondances
- Coder pour permettre d'améliorer facilement les algo (par exemple les regexp de transformation de l'HTML en markdown)