## Contribuer au projet

Vous pouvez aider au projet et devenir facilement un contributeur. 
Vous pouvez tout d'abord rejoindre la communauté soit sur le salon discord "La Fonderie" dans le salon qui est dédié au système PF2, soit sur le discord "Pathfinder-fr" qui dispose également d'un salon consacré au chantier du wiki PF2 et de salons permettant de discuter du jeu en général et un consacré spécifiquement aux tables virtuelles.

Contribuer està la portée de chacun et nous avons constamment besoin de relecteurs et de traducteurs et même d'utilisateurs qui constatent des erreurs ou des problèmes d'affichage.  

Dans les données, vous trouverez notamment un dictionnaire. Il est devenu un peu lent à charger dans la mesure où il grossit au fur et à mesure mais il montre aussi tout ce qui est traduit et tout ce qui ne l'est pas en effectuant une comparaison entre les données anglaises et les données françaises.

Pour traduire quelque chose qui n'est pas encore traduit, il suffit de cliquer dessus. Gitlab dispose d'un éditeur intégré et il suffit donc de vous créer un compte sur Gitlab pour pouvoir contribuer.

En appuyant sur le lien sur le fichier, celui-ci s'ouvre et comprend plusieurs des champs suivants : 

* **Name:** C'est le nom en anglais du fichier et le nom affiché en anglais de la capacité, du don, du sort,... Vous n'y touchez pas.

* **Nom:** Ici vous devrez inscrire le nom que vous aurez traduit s'il ne l'est pas déjà ouvous n'y touchez pas s'il existe déjà en vf

* **PrereqEN:** Ce champ n'existe que pour les dons à ce jour et correspond aux prérequis quand ils existent. Vous n'y touchez pas

* **PrereqFR:** Ici vous devrez remplir en  indiquant les prérequis après les avoir traduits. S'il y en a plusieurs, vous devrez les séparer avec une barre verticale qui s'obtient en appuyant sur AltGr+6.

* **État:** L'état sert à générer les tableaux qui sont nécessaires pour mesurer la progression de la traduction et voir où les interventions sont nécessaires. L'indicateur _officielle_ montre en principe que tout va bien et que le fichier est à jour avec la traduction officielle. Elle peut avoir déjà été l'objet d'un erratum non encore pris en compte par l'éditeur de la version française. L'état _libre_ montre que tout va bien mais que le texte proposé est issu d'une traduction libre. Cela peut-être une traduction officielle qui a été modifiée car erronée ou trompeuse ou issue d'un errata ou une traduction qui est réalisée par un contributeur destinée à être remplacée un jour par le texte officiel diffusé par BBE si quelqu'un a l'énergie de la mettre à cet endroit.

S'il est inscrit **aucune**, c'est que le fichier n'a encore jamais été traduit jusqu'à présent (ou que le contributeur étourdi a oublié de modifier l'État).

** Si c'est vous qui faites la traduction, vous remplacez donc aucune par libre.
** si vous copiez/collez la traduction officielle qui est effectuée par BBE en français, vous remplacez alors par officielle. 

Si l'état indique **changé**, cela signifie que le fichier anglophone a connu des modifications depuis sa traduction. Cela peut être des changements de structure, de balises, l'insertion de formules de calculs, l'introdutcion d'effets codés dans le système de Foundry pour permettre l'automatisation. Dans ce cas, en dessous d'état, devrait figurer un autre champ intitulé **État d'origine:** Ce champ n'existe donc que si le fichier a déjà été traduit auparavant. Il indique si la traduction précédent provient d'une traduction libre ou d'une traduction officielle. Dans le cas où vous éditez ce fichier, il faut donc supprimer la ligne état changé et remettre devant l'État, soit libre, soit officielle selon ce qui était indiqué sous État d'origine en supprimant la ligne État d'origine. Pour intervenir sur un fichier changé, il vous faut donc vous assurer de bien repérer les éventuelles modifications entre la vo et la vf et tout contrôler, y compris les liens. Il vaut mieux être certain de toutes les repérer avant de modifier l'état pour le remettre à son état antérieur.

* ------ **Description (en)** ------
suivie d'un texte en anglais, comprenant une mise en forme avec des balises de code.

* ------ **Description (en)** ------
S'il n'existe aucune traduction, ce champ est vide et vous devrez le remplir complètement en remettant les balises présentes en anglais.

** soit vous disposez de la traduction officielle. Alors vous la copier et replacez les balises existantes en anglais en respectant leur structure.

** Soit vous ne disposez pas de la traduction officielle. Alors vous traduisez le texte en vous aidant du Dictionnaire qui comprend tous les mots qui font l'objet d'une balise dans la traduction anglaise.

Vous pouvez facilement éditer un fichier qui est déjà traduit pour voir comment c'est fait.

Au besoin, vous pouvez vous faire aider par différents membres de la communauté francophone sur le discord La Fonderie, dans le salon PF2 ou sur le discord Pathfinder-fr dans le salon chantier du wiki.

* **Quelques conventions et observations** :

** Une majuscule est utilisée uniquement sur le premier mot du nom de la capacité que vous traduisez et sur les noms propres. Ainsi : _Blocage au bouclier_

** La première lettre des mots qui correspondent à un terme technique du jeu sont fréquemment en majuscule. Ainsi : _vous faites une **F**rappe à une créature **O**bservée._ Cela permet au lecteur de savoir que vous visez un terme technique du jeu.

** on supprime en général les balises <span></span> lorsqu'elles ne sont pas suivies d'autres instructions de codage et encadrent simplement du texte.

** On supprime absolument toutes les références aux pages des livres puisque nous naviguons sur internet.

** Quand il est indiqué des sorts "dans ce livre", on remplace par des sorts "du livre de base". Il n'y a pas de "sorts ordinaires", mais des "sorts courants"  (pb de glossaire des traducteurs de chez BBE). 

** En vf, dans une description, on remet les listes créées dans l'ordre alphabétique ou par niveau si c'est classé par niveau lorsque c'est possible. En cas de doute, ne pas hésiter à demander un avis.

** Dans les textes descriptifs : 1/jour devient une fois par jour. 1 min. devient 1 minute. On a de la place, ce qui n'est pas le cas des traducteurs officiels des bouquins qui ont besoin de réduire pour respecter la pagination.

** Il existe des balises pour créer des liens que vous repérerez facilement car elles prennent la forme  suivante @Compendium[pf2e.feats-srd.muMOxZyduEFv8UT6]{Nom en français}. Quand vous les croisez, vous remplacez ce qui est entre les {nom affiché}. Vous pouvez alors sans souci mettre au féminin, au pluriel ou conjuguer. Les liens entre les fichiers se font par renvoi à l'ID du compendium qui est indiqué entre les [crochets] qui ne doit par contre jamais être modifié.

** il existe des balises qui permettent, sous Foundry, de lancer les dés à partir du fichier. Elles ont une structure très particulière `[[/r 1d4 #perforants]]{1d4 perforants}` et désormais `[[/r 1d4[piercing]]]{1d4 perforants}` que vous ne touchez pas sauf si vous êtes capable de coder. De même, il existe des balises vers des effets qui ont un intérêt pour ceux qui utilisent Foundry. On traduit le nom de l'effet quand on en trouve un entre `{texte à traduire}`. Ce qui est entre les `{` est à traduire `}` et sera affiché par le système. On ne traduit pas ce qui est entre les crochets. D'autres structures appelées inline rolls sont plus complexes à modifier. Demandez conseil sur le discord.

Pour obtenir de l'aide un petit MP, ou un tag à rectulo dans l'un ou l'autre des discord et vous devriez avoir rapidement une réponse en journée (à l'heure française) et plusieurs contributeurs peuvent aussi vous répondre.

Fait le 26 octobre 2021
