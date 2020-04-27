-[_Parcours Openclassrooms_](https://openclassrooms.com/fr/projects/158/assignment)-

# [Projet 7][1]

## Créez GrandPy Bot, le papy-robot

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

### Cahier des charges

#### Fonctionnalités

*   Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
*   Vous utiliserez l'API de Google Maps et celle de Media Wiki.
*   Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
*   Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !

#### Parcours utilisateur

L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :

*   header : logo et phrase d'accroche
*   zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.
*   footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez

L'utilisateur tape dans le champ de formulaire :
> "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" 
Puis il appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît : 
> "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." 
En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message : 
> "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia][2]"

### Livrables

- Document texte expliquant la démarche choisie 
    * difficultés rencontrées / solutions trouvées
    * format pdf et ne pas excéder 2 pages A4
    * rédigé en anglais ou en français, au choix
    * Adresse du site déployé
- [Code source hébergé sur Github][3]
- [Tableau Trello ou Pivotal Tracker contenant vos user stories][4]

### Contraintes

*   Interface responsive
*   Test Driven Development
*   Code intégralement écrit en anglais : fonctions, variables, commentaires, ...
*   Utilisation d'AJAX pour l'envoi des questions et l'affichage des réponses (les questions et réponses sont en une seule langue au choix, anglais ou français)
*   Tests utilisant des mocks pour les API

[1]: https://openclassrooms.com/fr/projects/158/assignment
[2]: https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis
[3]: https://github.com/raoofrachidi/Projet-7
[4]: https://github.com/raoofrachidi/Projet-7/projects/1
