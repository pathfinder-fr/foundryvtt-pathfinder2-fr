## Contribuer au projet

Vous pouvez aider au projet et devenir facilement un de ses contributeurs.  

Vous pouvez également rejoindre la communauté à partir de l'application discord "La Fonderie" qui dispose d'un salon qui est dédié au système PF2.

Vous pouvez rejoindre la communauté Pathfinder 2 à partir de l'application discord "Pathfinder-fr" qui dispose également de salons consacrés au chantier du wiki PF2, de salons permettant de discuter du jeu en lui-même et un salon plus particulièrement consacré spécifiquement aux tables virtuelles.

Contribuer est à la portée de chacun. Nous avons constamment besoin de relecteurs et de traducteurs et même d'utilisateurs capables de signaler des erreurs ou des problèmes d'affichage.  

Dans les données présentes, vous disposez également d'un dictionnaire vo/VF et d'un dictionnaire vf/vo. Il est un peu lent à charger en raison de la taille de la bse de données qui a grossi au fur et à mesure de l'avancée du projet. Il montre tout ce qui est traduit et ce qui ne l'est pas encore. Il est généré automatiquement à chaque mise à jour.

Si vous constatez qu'un fichier dont vous avez besoin n'est pas encore traduit, il suffit de cliquer dessus pour l'éditer. Gitlab dispose d'un éditeur intégré et il suffit donc de vous créer un compte sur Gitlab pour pouvoir contribuer. Le fichier sera alors signalé à ceux qui contribuent au système qui pourront alors bénéficier de votre traduction.

Si vous éditez le fichier à partir de Gitlab, il s'ouvre et comprend les champs suivants : 

* **Name:** C'est le nom en anglais du fichier et le nom affiché en anglais de la capacité, du don, du sort,... Vous n'y touchez. Si vous constatez une typo, n'hésitez pas à la signaler sur le salon discord. Elle sera remontée aux anglophones.

* **Nom:** Ici vous devrez inscrire le nom que vous aurez traduit s'il ne l'est pas déjà ou vous n'y touchez pas s'il existe déjà en vf

* **État:** L'état sert à générer les tableaux qui sont nécessaires pour mesurer la progression de la traduction et voir où les interventions sont nécessaires. 
** L'indicateur _officielle_ montre que le fichier est à jour et correspond à la traduction officielle réaliséee par l'éditeur francophone (Black Book Editions). Cette donnée peut avoir déjà été l'objet d'un erratum qui n'a pas encore été pris en compte par l'éditeur de la version française. 
** L'état _libre_ montre que tout va bien mais que le texte proposé est issu d'une traduction libre. Cela peut-être une traduction officielle qui a été modifiée car erronée ou trompeuse ou issue d'un errata ou une traduction qui est réalisée par un contributeur destinée à être remplacée un jour par le texte officiel diffusé par BBE si quelqu'un a l'énergie de la mettre à cet endroit.
** L'état __aucune__ indique que le fichier n'a encore jamais été traduit jusqu'à présent (ou que le précédent contributeur étourdi a oublié de modifier l'état).

** Si c'est vous qui faites la traduction, vous remplacez donc aucune par **libre**.
** si vous placez la traduction officielle effectuée par BBE en français, vous remplacez alors l'état par **officielle**. 

Si l'état indique **changé**, cela signifie que le fichier anglophone a connu des modifications depuis sa dernière traduction.

Cela peut être des changements de structure, de balises, l'insertion de formules de calculs, l'introduction d'effets codés dans le système de Foundry pour faciliter le jeu. 

Dans ce cas, en dessous d'état, devrait figurer un autre champ intitulé **État d'origine:** Ce champ n'existe donc que si le fichier a déjà été traduit auparavant. Il indique si la traduction précédent provient d'une traduction libre ou d'une traduction officielle. Dans le cas où vous éditez ce fichier, il faut donc supprimer la ligne état changé et remettre devant l'État, soit libre, soit officielle selon ce qui était indiqué sous État d'origine en supprimant la ligne État d'origine. Pour intervenir sur un fichier changé, il vous faut donc vous assurer de bien repérer les éventuelles modifications entre la vo et la vf et tout contrôler, y compris les liens. Il vaut mieux être certain de toutes les repérer avant de modifier l'état pour le remettre à son état antérieur.

* **PrereqEN:** Ce champ n'existe que pour les dons à ce jour et correspond aux prérequis quand ils existent. Vous n'y touchez pas

* **PrereqFR:** Ici vous devrez remplir en  indiquant les prérequis après les avoir traduits. S'il y en a plusieurs, vous devrez les séparer avec une barre verticale qui s'obtient en appuyant sur AltGr+6.

* ------ **Description (en)** ------
suivie d'un texte en anglais, comprenant une mise en forme avec des balises de code qui sert de modèle mais qu'il ne faut pas modifier.

* ------ **Description (en)** ------
S'il n'existe aucune traduction, ce champ est vide et vous devrez le remplir complètement en remettant les balises présentes en anglais.

Il existe d'autres champs extraits fonctinnnant sur le même principe. L'anglais au dessus et le français en dessous.

Vous traduisez le texte en vous aidant si possible du Dictionnaire pour les mots clés et techniques. Il comprend tous les mots qui peuvent faire l'objet d'un lien et d'une référence issus de la traduction anglaise.

Vous pouvez facilement regarder un fichier qui est déjà traduit pour voir comment il est constitué.

Au besoin, vous pouvez vous faire aider par différents membres de la communauté francophone sur les salons discord La Fonderie ou Pathfinder-fr.

* **Quelques conventions et observations** :

** Une majuscule est utilisée uniquement sur le premier mot du nom de la capacité que vous traduisez et sur les noms propres. Ainsi : _Blocage au bouclier_

** La première lettre des mots qui correspondent à un terme technique du jeu sont fréquemment en majuscule. Ainsi : _vous faites une **F**rappe à une créature **O**bservée._ Cela permet au lecteur de savoir que vous visez un terme technique du jeu.

** on supprime en général les balises <span></span> lorsqu'elles ne sont pas suivies d'autres instructions de codage et qu'elles encadrent simplement du texte. Il ne devrait plus en rester après les changements opérés mais il arrive qu'il puisse y avoir desbalises orphelines.

** On supprime absolument toutes les références aux pages des livres puisque nous naviguons sur internet.

** Quand il est indiqué des sorts "dans ce livre", on remplace par des sorts "du livre de base". Il n'y a pas de "sorts ordinaires", mais des "sorts courants"  (c'est un problème de glossaire lié à la rareté qui n'existe qu'en français à la suite des choix de traduction. Les mots ordinaire, commun et courant ont été traduits pour traduire l'unique mot anglais common).

** En vf, dans une description, on remet autant que possible les listes créées dans l'ordre alphabétique après traduction, ou par niveau et par ordre alphabétique si c'est classé par niveau chaque fois que c'est possible. En cas de doute, ne pas hésiter à demander un avis avant de faire.

** Dans les textes descriptifs : 1/jour devient **une fois par jour**. 1 min. devient **1 minute**. On a de la place, ce qui n'est pas le cas dans les livres physiques. L'anglais prend moins de place et les traducteurs ont souvent besoin de réduire au maximum pour respecter la pagination.

** Il existe des balises pour créer des liens que vous repérerez facilement car elles prennent la forme  suivante `@Compendium[pf2e.feats-srd.muMOxZyduEFv8UT6]{Nom en français}`. Quand vous les croisez, vous ne remplacez que ce qui figure entre les accolades {nom affiché}. Vous pouvez alors sans souci mettre le contenu de l'accolade au féminin, au pluriel ou même conjuguer. Les liens entre les fichiers se font ainsi par renvoi à l'ID propre à chaque fichier dans les compendium. L'ID est indiqué entre les [crochets]. Cet ID ne doit par contre jamais être modifié.

** il existe des balises qui permettent, sous Foundry, de lancer les dés à partir du fichier. Elles ont une structure très particulière `[[/r 1d4[piercing]]]{1d4 perforants}` que vous ne touchez pas sauf si vous êtes capable de coder. De même, il existe des balises vers des effets qui ont un intérêt pour ceux qui utilisent Foundry. On traduit le nom de l'effet quand on en trouve un entre `{texte à traduire}`. Ce qui est entre les `{` est à traduire `}` et sera affiché par le système. On ne traduit pas ce qui est entre les crochets. 

** D'autres structures appelées inline rolls sont plus complexes à modifier pour effectuer des tests. Demandez conseil sur le discord avant de les toucher.

Pour obtenir de l'aide un petit MP, un tag à rectulo dans l'un ou l'autre des discord mentionnés et vous devriez avoir rapidement une réponse en journée (à l'heure française). Plusieurs autres contributeurs peuvent aussi vous répondre si c'est posté dans les salons discord.

Fait le 20 février 2022
