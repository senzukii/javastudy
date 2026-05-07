with open('C:/Users/layeu/Downloads/javastudy/qcm.html', 'r', encoding='utf-8') as f:
    content = f.read()

NEW_CREATION = """    {
      q: "Dans Factory Method, quel est le rôle de la méthode du Créateur abstrait qui appelle creerProduit() puis utilise le résultat ?",
      opts: [
        "Elle crée directement le produit sans déléguer aux sous-classes",
        "Elle orchestre l'utilisation du produit — appelle creerProduit() sans savoir quelle classe concrète est retournée (Template Method)",
        "Elle remplace le Directeur du pattern Builder",
        "Elle valide que le produit créé est conforme à l'interface"
      ],
      correct: 1,
      expl: "C'est le <strong>Template Method</strong> intégré au Factory Method : la classe abstraite Créateur définit une méthode concrète (ex: preparerCommande()) qui appelle creerProduit() en interne. Elle utilise le produit via son interface, sans jamais savoir si c'est une MargheritaCharleroi ou une MargheritaBruxelles."
    },
    {
      q: "Dans Abstract Factory, que faut-il faire pour ajouter une nouvelle famille (ex: ingrédients espagnols) ?",
      opts: [
        "Créer IngredientsEspagnols implements IngredientsFactory — sans modifier l'interface ni les familles existantes",
        "Modifier l'interface FabriqueAbstraite pour ajouter les méthodes espagnoles",
        "Modifier toutes les FabriquesConcretes existantes",
        "Ajouter des méthodes supplémentaires à l'interface Produit"
      ],
      correct: 0,
      expl: "Ajouter une famille = <strong>une nouvelle FabriqueConcrete</strong>. Aucun code existant n'est touché — c'est OCP respecté pour l'axe des familles. On n'ajoute que IngredientsEspagnols implements IngredientsFactory."
    },
    {
      q: "Quel pattern de création est le plus difficile à étendre quand on veut ajouter un nouveau TYPE de produit (pas une nouvelle famille) ?",
      opts: [
        "Simple Factory",
        "Abstract Factory — il faut modifier l'interface + toutes les FabriquesConcretes existantes",
        "Factory Method",
        "Builder"
      ],
      correct: 1,
      expl: "<strong>Abstract Factory</strong> souffre ici : ajouter creerDessert() à IngredientsFactory oblige à l'implémenter dans IngredientsItaliens ET IngredientsBelges ET IngredientsEspagnols... Facile d'ajouter des familles, difficile d'ajouter des types."
    },
    {
      q: "Dans Builder, qui appelle getResultat() pour obtenir l'objet final ?",
      opts: [
        "Le Directeur, en interne après avoir orchestré toutes les étapes",
        "L'interface Builder automatiquement",
        "Le Client — après que le Directeur a construit, le Client appelle getResultat() sur le BuilderConcret",
        "Le Produit lui-même lors de sa finalisation"
      ],
      correct: 2,
      expl: "C'est le <strong>Client</strong> : il passe le BuilderConcret au Directeur, le Directeur orchestre les étapes, puis le Client récupère le Produit fini via builderConcret.getResultat(). Le Directeur ne retourne rien."
    },
    {
      q: "Dans Factory Method, le Client instancie-t-il directement PizzeriaCharleroi ?",
      opts: [
        "Oui — c'est lui qui choisit le CréateurConcret. Mais il ne connaît pas MargheritaCharleroi (le Produit concret)",
        "Non — le Client ne connaît aucune classe concrète",
        "Non — c'est la classe abstraite Pizzeria qui instancie PizzeriaCharleroi",
        "Oui, et il instancie aussi directement MargheritaCharleroi"
      ],
      correct: 0,
      expl: "Le Client <strong>choisit le CréateurConcret</strong> (new PizzeriaCharleroi()) mais ne connaît jamais le ProduitConcret (MargheritaCharleroi). Le découplage est entre Client et Produit, pas entre Client et Créateur."
    },
    {
      q: "Dans Abstract Factory, IngredientsItaliens et IngredientsBelges implémentent quelle interface ?",
      opts: [
        "ProduitAbstrait",
        "L'interface FabriqueAbstraite (ex: IngredientsFactory)",
        "FeuilleConcrete du pattern Composite",
        "La classe abstraite Créateur du pattern Factory Method"
      ],
      correct: 1,
      expl: "IngredientsItaliens et IngredientsBelges sont les <strong>FabriquesConcretes</strong> : elles implémentent IngredientsFactory et fournissent une implémentation cohérente pour creerPate, creerSauce, creerFromage."
    },
    {
      q: "Dans Builder, si on veut créer deux burgers différents à la suite avec le même Directeur, que fait-on ?",
      opts: [
        "Créer deux Directeurs différents, un par type",
        "Le Directeur reconstruit automatiquement",
        "Appeler construire() deux fois avec des BuilderConcrets différents : construire(new BurgerPoulet()) puis construire(new BurgerBoeuf())",
        "Le Directeur garde en mémoire le dernier objet et le duplique"
      ],
      correct: 2,
      expl: "Le Directeur est <strong>réutilisable</strong> : construire(new BurgerPoulet()) → getResultat() → construire(new BurgerBoeuf()) → getResultat(). Même Directeur, BuilderConcrets différents, Produits différents."
    },
    {
      q: "Dans Factory Method, qu'arrive-t-il si on ajoute une nouvelle Pizzeria (PizzeriaLyon) ?",
      opts: [
        "On modifie la classe abstraite Pizzeria pour ajouter un cas",
        "On crée PizzeriaLyon extends Pizzeria et on implémente creerPizza() — aucun code existant n'est modifié",
        "On modifie toutes les PizzeriaConcretes existantes",
        "On ajoute un cas dans un switch central"
      ],
      correct: 1,
      expl: "<strong>OCP respecté</strong> : créer une nouvelle Pizzeria = écrire une nouvelle classe. Zéro modification de Pizzeria abstraite ou des autres Pizzerias. Le code existant et testé reste intact."
    },
    {
      q: "Dans Builder, le Produit final connaît-il le BuilderConcret qui l'a assemblé ?",
      opts: [
        "Oui — il stocke une référence au BuilderConcret",
        "Oui — via l'interface Builder",
        "Non — le Produit est juste un objet assemblé, il ne sait pas comment il a été créé",
        "Oui, pour permettre sa reconstruction"
      ],
      correct: 2,
      expl: "Le Produit (Burger) est <strong>indépendant de son processus de création</strong>. Un Burger contient des attributs (pain, viande, sauce) mais ne sait pas qu'il a été construit par BurgerPoulet via le Cuisinier."
    },
    {
      q: "Dans Factory Method, creerProduit() dans le Créateur abstrait est-elle toujours abstraite ?",
      opts: [
        "Oui — elle doit toujours être abstraite pour forcer les sous-classes à l'implémenter",
        "Non — elle peut avoir une implémentation par défaut que les sous-classes peuvent surcharger si elles veulent",
        "Non — elle est toujours concrète",
        "Oui, sinon ce n'est pas un Factory Method"
      ],
      correct: 1,
      expl: "Elle peut être <strong>abstraite OU avoir une implémentation par défaut</strong>. Si abstraite, toutes les sous-classes DOIVENT l'implémenter. Avec une implémentation par défaut, les sous-classes peuvent l'utiliser telle quelle ou la surcharger. Les deux variantes sont valides."
    },
    {
      q: "Dans Abstract Factory, si le Client change IngredientsItaliens pour IngredientsBelges, combien de lignes de code change-t-il ?",
      opts: [
        "Toutes les lignes qui créent des produits",
        "L'ensemble du code métier",
        "Seulement la ligne où la FabriqueConcrete est instanciée/injectée",
        "Les méthodes creerPate(), creerSauce(), creerFromage() partout"
      ],
      correct: 2,
      expl: "<strong>Une seule ligne</strong> : new IngredientsBelges() au lieu de new IngredientsItaliens(). Tout le reste du code appelle fab.creerPate() etc. via l'interface — il n'a aucune idée que la famille a changé."
    },
    {
      q: "Quel est le nom des 4 participants du pattern Builder ?",
      opts: [
        "Créateur, CréateurConcret, Produit, Client",
        "Fabrique, FabriqueConcrete, Produit, Client",
        "Builder, BuilderConcret, Directeur, Produit",
        "Strategy, Context, Produit, Directeur"
      ],
      correct: 2,
      expl: "Les 4 participants : <strong>Builder</strong> (interface définissant les étapes), <strong>BuilderConcret</strong> (implémentation concrète), <strong>Directeur</strong> (orchestre l'ordre), <strong>Produit</strong> (l'objet complexe résultant). Ex: BurgerBuilder, BurgerPoulet, Cuisinier, Burger."
    },
    {
      q: "Dans Simple Factory, créer une méthode statique creerPizza(String type) — quel inconvénient cela pose-t-il ?",
      opts: [
        "Les méthodes statiques sont interdites dans le Simple Factory",
        "Les méthodes statiques ne peuvent pas retourner des interfaces",
        "On ne peut pas injecter une fausse Fabrique pour les tests (méthode statique impossible à remplacer)",
        "Les méthodes statiques violent automatiquement OCP"
      ],
      correct: 2,
      expl: "Les méthodes <strong>statiques couplent fortement</strong> : on ne peut pas injecter une MockPizzeriaFactory pour les tests unitaires. L'instance injectée (non-statique) permet de passer une fausse implémentation en test."
    },
    {
      q: "Dans Abstract Factory, le Client peut-il utiliser plusieurs FabriquesConcretes différentes en même temps ?",
      opts: [
        "Non — un Client ne peut utiliser qu'une seule FabriqueConcrete à la fois",
        "Oui — un Client peut avoir IngredientsItaliens pour les entrées et IngredientsBelges pour les desserts si voulu",
        "Non — cela violerait la cohérence des familles",
        "Oui, mais seulement via l'interface FabriqueAbstraite"
      ],
      correct: 1,
      expl: "Techniquement <strong>possible</strong> mais généralement contre l'intention du pattern : l'Abstract Factory garantit la cohérence d'une famille. Mélanger les familles peut casser la cohérence. Le pattern est conçu pour qu'un seul contexte = une seule famille cohérente."
    },
    {
      q: "Dans Factory Method, quel participant instancie réellement le ProduitConcret ?",
      opts: [
        "Le Client qui appelle creerProduit()",
        "La classe abstraite Créateur",
        "Le CréateurConcret dans son implémentation de creerProduit()",
        "L'interface Produit via une méthode statique"
      ],
      correct: 2,
      expl: "<strong>Le CréateurConcret</strong> : PizzeriaCharleroi.creerPizza() contient new MargheritaCharleroi(). C'est la décision d'instanciation qui est déléguée aux sous-classes — c'est l'essence du pattern."
    }"""

NEW_STRUCTURE = """    {
      q: "Dans Composite, Box_A contient Box_B(Produit_1(5€)) et Produit_2(10€). Quel est le résultat de getPrice() sur Box_A ?",
      opts: [
        "10€ — seulement Produit_2, Box_B est ignorée",
        "15€ — Box_A appelle getPrice() sur Box_B(5€) et Produit_2(10€), somme 5+10",
        "5€ — seulement Box_B",
        "0€ — Box_A délègue tout à Box_B"
      ],
      correct: 1,
      expl: "Box_A itère ses enfants : Box_B.getPrice() → Produit_1.getPrice() retourne 5€, Box_B retourne 5€. Produit_2.getPrice() retourne 10€. Box_A somme : <strong>5 + 10 = 15€</strong>."
    },
    {
      q: "Dans Décorateur, la référence #composant est-elle généralement publique, privée ou protégée ?",
      opts: [
        "Toujours publique pour être accessible aux sous-classes",
        "Protected — accessible aux DécorateursConcrets mais pas au Client extérieur",
        "Privée — exposée via un getter public",
        "Statique et partagée entre toutes les instances"
      ],
      correct: 1,
      expl: "<strong>Protected</strong> est le choix habituel : <code>protected Boisson composant</code> dans CondimentDecorateur. Les DécorateursConcrets (Lait, Chantilly) héritent et peuvent appeler composant.getCost(). Le Client ne l'utilise pas directement."
    },
    {
      q: "Quel est le résultat de new Lait(new Café()).getCost() si Café retourne 1€ et Lait ajoute 0.20€ ?",
      opts: [
        "0.20€ — seulement le prix de Lait",
        "1€ — seulement le prix de Café",
        "1.20€ — Lait délègue à Café (1€) et ajoute sa contribution (0.20€)",
        "2.20€ — les deux prix sont additionnés deux fois"
      ],
      correct: 2,
      expl: "<strong>1.20€</strong> : Lait.getCost() appelle composant.getCost() (Café retourne 1€) puis ajoute 0.20. return composant.getCost() + 0.20 = <strong>1.20€</strong>."
    },
    {
      q: "Dans Composite, pourquoi met-on généralement add(Composant) sur le Composé et non sur l'interface Composant ?",
      opts: [
        "Les Feuilles ne devraient pas avoir de méthode add() — les forcer via l'interface serait trompeur ou inutile",
        "Pour des raisons de performance Java",
        "Car add() n'est pas une opération standard",
        "Car l'interface Composant ne peut pas avoir de méthodes avec paramètres"
      ],
      correct: 0,
      expl: "Choix de <strong>sécurité vs transparence</strong>. Si add() est dans l'interface, les Feuilles seraient forcées de l'implémenter (levant souvent une exception). En la mettant sur le Composé seulement, le compilateur empêche add() sur une Feuille."
    },
    {
      q: "Dans Décorateur, que se passe-t-il si on oublie d'appeler composant.operation() dans le DécorateurConcret ?",
      opts: [
        "Le programme plante avec une NullPointerException",
        "La chaîne continue normalement",
        "Le comportement de l'objet enveloppé est perdu — seul le comportement du Décorateur s'exécute",
        "ComposantAbstrait est appelé comme fallback"
      ],
      correct: 2,
      expl: "Si Lait oublie d'appeler composant.getCost(), <strong>le Café n'est jamais calculé</strong>. Lait retournerait 0.20€ au lieu de 1.20€. La délégation est obligatoire — sans elle, la chaîne est rompue."
    },
    {
      q: "Dans Composite, le Composé lui-même implémente-t-il l'interface Composant ?",
      opts: [
        "Oui — Box implémente Item, ce qui permet de l'imbriquer dans d'autres Box",
        "Non — le Composé a un type distinct pour éviter la confusion",
        "Non — seules les Feuilles implémentent Composant",
        "Oui, mais seulement si le Composé ne contient que des Feuilles"
      ],
      correct: 0,
      expl: "Oui — c'est <strong>l'essence du Composite</strong> : Box implémente Item. Cela permet à une Box de contenir d'autres Box. Sans ça, l'imbrication récursive serait impossible."
    },
    {
      q: "Dans Décorateur, comment appelle-t-on le mécanisme où chaque objet passe l'appel à l'objet qu'il contient ?",
      opts: [
        "Héritage en cascade",
        "Polymorphisme multiple",
        "Surcharge de méthode",
        "Délégation (forwarding) — chaque Décorateur appelle composant.operation() pour passer la main à l'objet suivant"
      ],
      correct: 3,
      expl: "<strong>Délégation</strong> : Lait.getCost() dit 'laisse Café calculer son prix, je rajoute juste ma contribution'. Différent de super — on appelle via une référence à un objet externe."
    },
    {
      q: "Dans Composite, peut-on avoir une profondeur arbitraire d'imbrication ?",
      opts: [
        "Oui — Box peut contenir Box qui contient Box... La récursion s'arrête aux Feuilles",
        "Non — maximum 3 niveaux de profondeur",
        "Non — le pattern ne supporte que 2 niveaux",
        "Oui, mais seulement si tous les Composants sont du même type"
      ],
      correct: 0,
      expl: "Oui, <strong>profondeur arbitraire</strong> : une commande peut avoir des boîtes dans des boîtes. getPrice() sur la racine calcule tout grâce à la récursion. La profondeur n'est limitée que par la mémoire disponible."
    },
    {
      q: "Dans Décorateur, est-il sécuritaire de passer null comme composant au constructeur ?",
      opts: [
        "Oui, c'est un cas valide prévu par le pattern",
        "Oui, cela retourne automatiquement 0",
        "Oui, si le Décorateur vérifie null en interne",
        "Non — composant.operation() causerait une NullPointerException"
      ],
      correct: 3,
      expl: "En pratique, <strong>null est invalide</strong> : Lait.getCost() appelle composant.getCost() → NullPointerException si composant est null. Le constructeur devrait valider composant != null pour échouer tôt."
    },
    {
      q: "Dans Composite, une Box vide (sans enfants) que retourne getPrice() ?",
      opts: [
        "Une exception — une Box vide est invalide",
        "0 — elle parcourt une liste vide, la somme reste 0",
        "null — aucune valeur calculable",
        "Le prix par défaut de l'interface"
      ],
      correct: 1,
      expl: "<strong>0</strong> : la boucle sur la liste vide ne s'exécute pas, la somme reste 0. Box_A(Produit_1(10€) + BoxVide()) = 10 + 0 = 10€. Comportement naturel et correct."
    },
    {
      q: "Dans Décorateur, pourquoi préfère-t-on la composition à l'héritage pour ajouter des comportements ?",
      opts: [
        "L'héritage est statique (défini à la compilation). La composition est dynamique (composée à l'exécution)",
        "L'héritage est plus lent",
        "L'héritage permet l'héritage multiple en Java",
        "La composition est plus lisible"
      ],
      correct: 0,
      expl: "<strong>Dynamisme</strong> : avec l'héritage, CaféLaitChantilly doit exister avant la compilation. Avec le Décorateur, new Chantilly(new Lait(new Café())) se compose à l'exécution selon la commande du client. On évite l'explosion de sous-classes."
    },
    {
      q: "Dans Composite, si on retire une Box de l'arbre, ses enfants disparaissent-ils du calcul ?",
      opts: [
        "Oui — retirer un nœud retire tout son sous-arbre du point de vue du parent",
        "Non — les enfants restent liés directement au parent du nœud retiré",
        "Non — il faut retirer chaque enfant manuellement d'abord",
        "Oui, mais seulement les Feuilles directes"
      ],
      correct: 0,
      expl: "Oui — quand on retire Box_B de Box_A, tout le sous-arbre de Box_B disparaît du calcul. Les objets Java continuent d'exister en mémoire si d'autres références les pointent, mais ne font plus partie de la hiérarchie."
    },
    {
      q: "Dans Décorateur new Vanille(new Chantilly(new Lait(new Café()))), combien d'appels à getCost() s'enchaînent ?",
      opts: [
        "1 appel — Vanille calcule tout directement",
        "2 appels — Vanille et Café seulement",
        "4 appels — Vanille appelle Chantilly, Chantilly appelle Lait, Lait appelle Café",
        "3 appels — seulement les Décorateurs, pas Café"
      ],
      correct: 2,
      expl: "<strong>4 appels</strong> : Vanille → Chantilly → Lait → Café. Café retourne 1€. Lait retourne 1.20€. Chantilly retourne 1.70€. Vanille retourne 1.70 + son prix. Chaque maillon de la chaîne s'exécute."
    },
    {
      q: "Quel avantage le Composite offre-t-il par rapport à une List plate pour une hiérarchie imbriquée ?",
      opts: [
        "La List est moins performante",
        "La List supporte l'héritage, pas le Composite",
        "Il n'y a pas vraiment d'avantage",
        "Le Composite encapsule la récursion — getPrice() sur la racine calcule TOUT automatiquement dans tous les niveaux"
      ],
      correct: 3,
      expl: "Avec une List plate, il faudrait coder la récursion à chaque appel. <strong>Le Composite encapsule la récursion</strong> : getPrice() sur Box_A sait automatiquement descendre dans tous les sous-arbres. Transparence totale pour le Client."
    },
    {
      q: "Peut-on combiner Composite et Décorateur dans la même application ?",
      opts: [
        "Oui — ex: arbre de fichiers (Composite) où chaque fichier peut être décoré avec des permissions (Décorateur)",
        "Non — les deux patterns utilisent la même interface et entrent en conflit",
        "Non — Composite est statique, Décorateur dynamique",
        "Oui, mais seulement s'ils partagent exactement la même interface"
      ],
      correct: 0,
      expl: "Oui, ils sont <strong>complémentaires</strong> : Composite pour représenter la hiérarchie (Dossier/Fichier), Décorateur pour enrichir dynamiquement les éléments (fichier chiffré, compressé, avec droits restreints...). Chaque pattern joue son rôle indépendamment."
    }"""

NEW_COMPORTEMENT = """    {
      q: "Dans Strategy, si on a 5 algorithmes de tri, combien de classes ConcreteStrategy faut-il créer ?",
      opts: [
        "1 classe avec 5 méthodes différentes",
        "5 classes — une par algorithme de tri (BubbleSortStrategy, QuickSortStrategy...)",
        "1 classe avec un paramètre de type",
        "Autant que de Contexts différents"
      ],
      correct: 1,
      expl: "<strong>5 classes</strong> : BubbleSortStrategy, QuickSortStrategy, MergeSortStrategy... — chacune implements SortStrategy. Chaque algorithme est encapsulé dans sa propre classe. Pas de if/else, pas de switch."
    },
    {
      q: "Dans Observer Pull, si Orageux a changé plusieurs fois depuis la dernière notification, que reçoit JeanMichel quand il appelle getEtat() ?",
      opts: [
        "L'état ACTUEL — le dernier état. Les états intermédiaires sont perdus",
        "L'historique complet de tous les changements",
        "L'état au moment précis où notifie() a été appelée",
        "Une exception car l'état a changé trop souvent"
      ],
      correct: 0,
      expl: "getEtat() retourne l'<strong>état courant</strong> au moment de l'appel. Les états intermédiaires ne sont pas stockés par défaut. Si Orageux est passé de 'soleil' à 'nuageux' à 'pluie', JeanMichel ne voit que 'pluie'."
    },
    {
      q: "Dans Strategy, le Context peut-il avoir une Strategy par défaut initialisée dans son constructeur ?",
      opts: [
        "Oui — le Context peut initialiser #strategy avec une ConcreteStrategy par défaut",
        "Non — une Strategy doit toujours être injectée explicitement",
        "Oui, mais seulement via une classe abstraite",
        "Non — cela violerait DIP"
      ],
      correct: 0,
      expl: "Oui — <code>this.strategy = new BancontactStrategy()</code> dans le constructeur est valide. Le Client peut ensuite la changer avec setStrategy(). Une Strategy par défaut améliore l'ergonomie sans sacrifier la flexibilité."
    },
    {
      q: "Dans Observer, un même objet peut-il être à la fois Sujet ET Observateur ?",
      opts: [
        "Oui — un objet peut implémenter les deux interfaces et participer aux deux rôles",
        "Non — les rôles sont mutuellement exclusifs",
        "Oui, mais seulement s'il hérite d'une classe commune",
        "Non — cela créerait une boucle infinie"
      ],
      correct: 0,
      expl: "Oui — courant dans les architectures événementielles : ServiceMétéo observe CapteurTemperature (Observateur) et notifie AppMobile (Sujet). <strong>Les chaînes de notification</strong> sont possibles tant qu'il n'y a pas de cycle."
    },
    {
      q: "Dans Observer Push, les données envoyées dans actualise() peuvent-elles être d'un type quelconque ?",
      opts: [
        "Oui — le type est défini dans l'interface Observateur (actualise(String), actualise(MeteoData)...)",
        "Non — ce doit toujours être une String",
        "Non — ce doit être un objet du type du Sujet",
        "Non — ce doit être un type primitif Java"
      ],
      correct: 0,
      expl: "Le type est <strong>défini par le contrat de l'interface</strong> Observateur. Les génériques Java permettent même <code>Observateur&lt;T&gt;</code> pour une interface typée et réutilisable."
    },
    {
      q: "Dans Strategy, si on utilise toujours la même ConcreteStrategy, le pattern apporte-t-il encore de la valeur ?",
      opts: [
        "Non — sans changement, un appel direct vaut mieux",
        "Oui — OCP, testabilité (injection d'un mock), et flexibilité future sont préservés",
        "Non — c'est de l'over-engineering dans ce cas",
        "Oui, mais il faudrait Abstract Factory à la place"
      ],
      correct: 1,
      expl: "<strong>OCP et testabilité</strong> : même avec une seule Strategy active, le pattern permet d'injecter un MockStrategy pour les tests, d'ajouter PayPal demain sans toucher au Context."
    },
    {
      q: "Dans Strategy, si la signature de la méthode change (payer(double) → payer(double, String devise)), que faut-il modifier ?",
      opts: [
        "Seulement le Context",
        "Seulement les ConcreteStrategies à modifier",
        "L'interface Strategy ET toutes les ConcreteStrategies",
        "Rien — le polymorphisme gère les différences de signature"
      ],
      correct: 2,
      expl: "Changer l'interface = <strong>casser tout le contrat</strong> : PaiementStrategy, Visa, Bancontact, PayPal... tous doivent être modifiés. Le pattern est robuste aux ajouts de Strategies, pas aux changements de contrat d'interface."
    },
    {
      q: "Dans Observer, plusieurs Sujets différents peuvent-ils notifier le même Observateur ?",
      opts: [
        "Oui — un Observateur peut s'abonner à plusieurs Sujets simultanément",
        "Non — un Observateur est toujours lié à un seul Sujet",
        "Oui, mais seulement en mode Pull",
        "Non — chaque Observateur doit avoir sa propre interface par Sujet"
      ],
      correct: 0,
      expl: "Oui — JeanMichel peut s'abonner à Orageux ET à AlerteInondation. Si les deux appellent actualise() sur JeanMichel, il réagit aux deux. <strong>L'abonnement multiple</strong> est naturel dans le pattern."
    },
    {
      q: "Dans Strategy, comment le Context reçoit-il la Strategy selon les bonnes pratiques ?",
      opts: [
        "Via une variable globale statique",
        "Via injection dans le constructeur ou setStrategy() — injection de dépendances",
        "Via une Factory Method interne qui crée la bonne Strategy",
        "Via un switch dans execute() selon le type de données"
      ],
      correct: 1,
      expl: "<strong>Injection de dépendances</strong> : new SystemePaiement(new Visa()) ou setStrategy(new Bancontact()). Les deux respectent DIP et facilitent les tests (injection de mock)."
    },
    {
      q: "Dans Observer, un Observateur peut-il se désabonner pendant que notifie() parcourt la liste ?",
      opts: [
        "Oui, sans problème",
        "Non, c'est techniquement impossible",
        "Oui si notifie() travaille sur une copie de la liste — sinon ConcurrentModificationException",
        "Non, mais il sera ignoré au prochain appel"
      ],
      correct: 2,
      expl: "Si un Observateur appelle retirer(this) dans actualise() pendant l'itération → <strong>ConcurrentModificationException</strong>. Solution : notifie() travaille sur une copie snapshot : <code>new ArrayList&lt;&gt;(observateurs)</code>."
    },
    {
      q: "strategy.payer(50) dans le Context est un exemple de quel concept fondamental de la POO ?",
      opts: [
        "Encapsulation — les données sont cachées",
        "Héritage — la méthode est héritée",
        "Polymorphisme — la même signature s'exécute différemment selon l'implémentation concrète",
        "Abstraction — la méthode est abstraite"
      ],
      correct: 2,
      expl: "<strong>Polymorphisme</strong> : strategy.payer(50) fait des choses différentes selon si strategy est Visa ou Bancontact. La bonne implémentation est choisie dynamiquement — polymorphisme d'exécution (late binding)."
    },
    {
      q: "Dans Observer, notifie() est-elle déclenchée par le Client ou en interne après modifieEtat() ?",
      opts: [
        "Toujours par le Client externe",
        "Toujours statique",
        "Toujours abstraite dans chaque SujetConcret",
        "En interne — modifieEtat() appelle notifie() automatiquement. Le Client modifie l'état, pas la notification"
      ],
      correct: 3,
      expl: "Flux standard : Client appelle <code>orageux.modifieEtat(\"pluie\")</code> → modifieEtat() met à jour l'état ET appelle notifie() → notifie() appelle actualise() sur chaque observateur. <strong>Le Client déclenche le changement, pas la notification.</strong>"
    },
    {
      q: "Dans Strategy, le Context dépend-il des ConcreteStrategies ou seulement de l'interface Strategy ?",
      opts: [
        "Uniquement de l'interface Strategy — il ne connaît pas Visa, Bancontact... C'est DIP appliqué",
        "Des ConcreteStrategies, car il les instancie",
        "Ni de l'un ni de l'autre",
        "Des ConcreteStrategies via le polymorphisme"
      ],
      correct: 0,
      expl: "<strong>DIP appliqué</strong> : SystemePaiement stocke <code>PaiementStrategy strategy</code> (interface). Il appelle strategy.payer() sans jamais faire new Visa() en interne. Les ConcreteStrategies sont créées et injectées par le Client."
    },
    {
      q: "Observer Pull vs Push : lequel est préférable si chaque Observateur n'a besoin que d'une partie des données ?",
      opts: [
        "Push — plus simple à implémenter",
        "Pull — chaque Observateur prend seulement ce dont il a besoin via getEtat()",
        "Les deux modes sont équivalents",
        "Ni l'un ni l'autre"
      ],
      correct: 1,
      expl: "<strong>Pull est préférable</strong> : si le Sujet a 50 attributs mais JeanMichel n'a besoin que de la température et MarieJosée que des précipitations, le Pull évite d'envoyer 50 champs à chacun. Chacun appelle ce qu'il veut."
    },
    {
      q: "Dans Strategy, peut-on passer des paramètres de configuration à une ConcreteStrategy lors de sa création ?",
      opts: [
        "Oui — via le constructeur de la ConcreteStrategy (ex: new VisaStrategy(apiKey, timeout))",
        "Non — les ConcreteStrategies ne peuvent pas avoir de constructeurs avec paramètres",
        "Oui, mais seulement via des méthodes statiques",
        "Non — tous les paramètres doivent passer par la méthode de l'interface"
      ],
      correct: 0,
      expl: "Oui — <code>new VisaStrategy(\"api_key\", 30)</code> est valide. La ConcreteStrategy peut avoir son propre état de configuration. L'interface définit juste la méthode principale. Création et utilisation sont séparées."
    }"""

NEW_SOLID = """    {
      q: "Une classe UserService contient createUser(), sendWelcomeEmail() et logActivity(). Combien a-t-elle de responsabilités ?",
      opts: [
        "1 — tout concerne les utilisateurs",
        "2 — création et notification",
        "3 — création, email et logging sont trois responsabilités distinctes",
        "4 — une responsabilité par méthode"
      ],
      correct: 2,
      expl: "<strong>3 responsabilités</strong> : logique métier, envoi d'emails (dépend d'un service mail), logging (dépend d'un système de log). Solution : UserRepository, EmailService, ActivityLogger — chacun a une seule raison de changer."
    },
    {
      q: "Pingouin extends Oiseau surcharge voler() en levant une exception. Que suggère LSP comme solution ?",
      opts: [
        "Supprimer voler() de Oiseau",
        "Rendre voler() optionnelle avec une implémentation vide par défaut",
        "Créer une classe OiseauTerrestre",
        "Créer une interface Volable séparée — seuls les oiseaux qui volent l'implémentent. Pingouin extends Oiseau sans implémenter Volable"
      ],
      correct: 3,
      expl: "Solution LSP : <code>interface Volable { void voler(); }</code>. Aigle implements Volable, Pingouin n'implémente pas Volable. Du code qui attend un Volable sait que la méthode fonctionnera sans exception."
    },
    {
      q: "Interface Vehicule avec accelerer(), freiner() et rechargerBatterie(). Une Ferrari (essence) doit implémenter rechargerBatterie() vide. Quel principe est violé ?",
      opts: [
        "ISP — Ferrari ne devrait pas être forcée d'implémenter rechargerBatterie()",
        "SRP — Vehicule a trop de responsabilités",
        "OCP — on ne peut pas étendre Vehicule",
        "LSP — Ferrari ne peut pas substituer Vehicule"
      ],
      correct: 0,
      expl: "<strong>ISP</strong> : solution — <code>Vehicule</code> (accelerer, freiner) et <code>VehiculeElectrique extends Vehicule</code> (rechargerBatterie). Ferrari implements Vehicule, Tesla implements VehiculeElectrique."
    },
    {
      q: "FactureService doit fonctionner avec MySQL, PostgreSQL et MongoDB. Quel principe guide la conception ?",
      opts: [
        "SRP — chaque BDD a sa propre classe",
        "OCP — on peut ajouter des BDs sans modifier FactureService",
        "DIP — FactureService dépend d'une interface FactureRepository, les trois BDs l'implémentent",
        "LSP — les BDs peuvent se substituer"
      ],
      correct: 2,
      expl: "<strong>DIP</strong> : FactureService(FactureRepository repo). MySQLFactureRepo, PostgresFactureRepo, MongoFactureRepo implémentent FactureRepository. Changer de BDD = changer l'injection, pas le code de FactureService."
    },
    {
      q: "Interface IAnimal avec voler(), nager(), courir(), grimper(). Un Serpent doit implémenter toutes les méthodes. Quel principe est violé ?",
      opts: [
        "SRP",
        "OCP",
        "DIP",
        "ISP — le Serpent est forcé d'implémenter voler(), courir(), grimper() qu'il ne peut pas faire"
      ],
      correct: 3,
      expl: "<strong>ISP</strong> : solution — interfaces séparées : Volable, Nageable, Coureur, Grimpeur. Serpent implements Nageable seulement. Chaque classe prend exactement les capacités dont elle a besoin."
    },
    {
      q: "Pourquoi la couche Service ne devrait-elle pas importer directement javax.persistence.EntityManager ?",
      opts: [
        "SRP — Service aurait trop de responsabilités",
        "DIP — Service (haut niveau) ne devrait pas dépendre de la technologie de persistance (bas niveau). Passer par une interface Repository",
        "OCP — on ne peut pas étendre EntityManager",
        "LSP — EntityManager ne peut pas être substitué"
      ],
      correct: 1,
      expl: "<strong>DIP</strong> : Service → interface UserRepository ← UserRepositoryJPA. Si on change de JPA à JDBC ou à un mock de test, Service ne change pas. La couche métier est isolée des détails techniques."
    },
    {
      q: "Chien.toString() retourne 'Chien: Rex', Chat.toString() retourne 'Chat: Minou'. LSP est-il respecté ?",
      opts: [
        "Oui — Chien et Chat peuvent substituer Animal, le contrat de toString() est honoré",
        "Non — les valeurs retournées sont différentes, LSP est violé",
        "Oui, mais seulement si toString() retourne void",
        "Non — des comportements trop différents violent LSP"
      ],
      correct: 0,
      expl: "<strong>LSP respecté</strong>. Le contrat de toString() est de retourner une représentation textuelle. Chien et Chat l'honorent. LSP ne dit pas que le retour doit être identique, mais que le contrat est respecté."
    },
    {
      q: "Quel principe guide le fait de déclarer List<Animal> au lieu de ArrayList<Animal> ?",
      opts: [
        "SRP",
        "DIP — on dépend de l'abstraction List (interface) plutôt que d'ArrayList (concrète)",
        "OCP",
        "ISP"
      ],
      correct: 1,
      expl: "<strong>DIP à petite échelle</strong> : si on change ArrayList pour LinkedList, seule la ligne new ArrayList<>() change. Tout le code qui utilise animaux via l'interface List reste intact."
    },
    {
      q: "Classe Formulaire avec valider(), sauvegarder() et afficher(). Combien de raisons de changer a-t-elle ?",
      opts: [
        "1 — tout concerne le formulaire",
        "2 — logique et affichage",
        "3 — règles de validation, technologie de persistance, et format d'affichage",
        "4 — une par méthode"
      ],
      correct: 2,
      expl: "<strong>3 raisons de changer</strong> : règles métier de validation, technologie de sauvegarde, format d'affichage. Solution : ValidateurFormulaire, FormulaireRepository, FormulaireRenderer."
    },
    {
      q: "Quel principe guide la création d'une interface PaymentGateway que PayPal, Stripe et Braintree implémentent ?",
      opts: [
        "SRP",
        "OCP",
        "LSP",
        "DIP — le code dépend de l'abstraction PaymentGateway, pas des implémentations concrètes"
      ],
      correct: 3,
      expl: "<strong>DIP</strong> : le code dépend de PaymentGateway (interface). On peut changer de prestataire en changeant l'injection. C'est aussi OCP : on ajoute Google Pay sans modifier le code existant."
    },
    {
      q: "Quel principe est respecté si changer Log4j pour SLF4J ne nécessite aucune modification du code métier ?",
      opts: [
        "SRP",
        "OCP",
        "DIP — le code métier dépend d'une interface Logger, pas de Log4j concret",
        "LSP"
      ],
      correct: 2,
      expl: "<strong>DIP</strong> : le code appelle logger.info() via une interface Logger. Log4jLogger et SLF4JLogger implémentent Logger. Changer de framework = changer la configuration d'injection, pas le code métier."
    },
    {
      q: "Interface Employe avec travailler(), prendreConge() et prendreCafe(). Un Freelance implémente prendreConge() vide. Quel principe est violé ?",
      opts: [
        "ISP — Freelance est forcé d'implémenter prendreConge() qui ne le concerne pas",
        "SRP",
        "OCP",
        "LSP"
      ],
      correct: 0,
      expl: "<strong>ISP</strong> : solution — Travailleur (travailler()) et SalarieCDI (prendreConge(), prendreCafe()). Freelance implements Travailleur seulement. Pas de méthodes vides."
    },
    {
      q: "AutrucheVolante extends Oiseau améliore voler() sans casser les invariants. LSP est-il respecté ?",
      opts: [
        "Oui — AutrucheVolante peut substituer Oiseau partout sans altérer le comportement attendu",
        "Non — on ne peut pas modifier le comportement hérité",
        "Non — AutrucheVolante viole SRP",
        "Oui mais seulement si voler() est final dans Oiseau"
      ],
      correct: 0,
      expl: "<strong>LSP respecté</strong> : AutrucheVolante améliore voler() mais respecte le contrat — elle peut voler. Partout où un Oiseau est attendu, AutrucheVolante fonctionne. LSP ne dit pas que le comportement doit être identique, juste compatible."
    },
    {
      q: "Interface Notification avec envoyerEmail(), envoyerSMS(), envoyerPush(). ServiceEmail implémente les deux autres vides. Quel principe est violé ?",
      opts: [
        "SRP",
        "ISP — ServiceEmail ne devrait dépendre que de EmailNotifier",
        "OCP",
        "DIP"
      ],
      correct: 1,
      expl: "<strong>ISP</strong> : solution — EmailNotifier (envoyerEmail()), SMSNotifier (envoyerSMS()), PushNotifier (envoyerPush()). ServiceEmail implements EmailNotifier seulement. Pas de méthodes vides."
    },
    {
      q: "Quel principe SOLID correspond à la 'cohésion' — toutes les méthodes d'une classe travaillent vers le même but ?",
      opts: [
        "SRP — une classe cohérente a une seule responsabilité et une seule raison de changer",
        "OCP",
        "LSP",
        "DIP"
      ],
      correct: 0,
      expl: "<strong>SRP</strong> et cohésion sont liés : une classe très cohérente a naturellement une seule raison de changer. Une classe peu cohérente (méthodes disparates) a plusieurs raisons de changer — SRP est probablement violé."
    },
    {
      q: "calculerPrime(Employe e) appelle des méthodes propres à Manager non définies dans Employe. Quel principe est violé ?",
      opts: [
        "SRP",
        "OCP",
        "ISP",
        "LSP — la méthode ne peut plus accepter n'importe quel Employe sans risque de ClassCastException"
      ],
      correct: 3,
      expl: "<strong>LSP violé</strong> : si en interne on fait ((Manager)e).getBonus(), passer un EmployéStandard lèvera ClassCastException. La méthode rompt le contrat de substitutabilité."
    },
    {
      q: "Classe Logger avec info(), warn(), error() et formatMessage(). SRP est-il respecté ?",
      opts: [
        "Probablement oui — toutes les méthodes servent le logging. formatMessage est un helper interne",
        "Non — formatter est une responsabilité totalement distincte",
        "Non — 4 méthodes violent toujours SRP",
        "Oui uniquement si Logger est statique"
      ],
      correct: 0,
      expl: "<strong>SRP probablement respecté</strong> : toutes les méthodes servent la responsabilité de logging. formatMessage est un détail d'implémentation interne. Si formatMessage devenait réutilisable ailleurs, on pourrait alors la séparer."
    },
    {
      q: "Quel principe est respecté quand Chien.faireDuBruit() et Chat.faireDuBruit() substituent Animal.faireDuBruit() sans problème ?",
      opts: [
        "SRP",
        "OCP",
        "LSP — Chien et Chat respectent le contrat sans casser les invariants d'Animal",
        "ISP"
      ],
      correct: 2,
      expl: "<strong>LSP respecté</strong> : le contrat de faireDuBruit() est de retourner un son. Chien et Chat l'honorent chacun à leur façon. LSP n'exige pas un résultat identique — il exige la compatibilité avec le contrat."
    },
    {
      q: "Interface Stockage avec lire(f), ecrire(f) et compresser(f). StockageCloud n'a pas besoin de compresser. Quel principe suggère de séparer ?",
      opts: [
        "SRP",
        "ISP — StockageCloud ne devrait pas être forcé d'implémenter compresser()",
        "DIP",
        "OCP"
      ],
      correct: 1,
      expl: "<strong>ISP</strong> : solution — StockageBasique (lire, ecrire) et StockageCompresse extends StockageBasique (compresser). StockageCloud implements StockageBasique. Pas de méthodes vides."
    },
    {
      q: "Quel principe est violé si ServiceCommande hérite de MySQLServiceCommande pour accéder à la BDD ?",
      opts: [
        "SRP — ServiceCommande fait trop de choses",
        "OCP — on ne peut pas l'étendre",
        "DIP — l'héritage couple fortement ServiceCommande (haut niveau) à MySQL (bas niveau)",
        "ISP — l'interface héritée est trop grande"
      ],
      correct: 2,
      expl: "<strong>DIP</strong> : ServiceCommande hérite de MySQLServiceCommande → couplage fort. Si on veut PostgreSQL, tout change. Solution : injecter CommandeRepository (interface). Changer de BDD = changer l'injection seulement."
    },
    {
      q: "Si tout le code utilise List<Forme> au lieu d'ArrayList<Forme>, que se passe-t-il quand on change ArrayList pour LinkedList ?",
      opts: [
        "Il faut changer toutes les déclarations de type",
        "Seule la ligne new ArrayList<>() change en new LinkedList<>() — le reste du code est intact",
        "Il faut modifier toutes les méthodes qui utilisent la liste",
        "Rien ne change, les deux sont identiques"
      ],
      correct: 1,
      expl: "<strong>DIP payant</strong> : une seule ligne change. Tout le code qui appelle .add(), .get(), boucle sur la liste via l'interface List reste intact. C'est l'intérêt de dépendre d'abstractions."
    }"""

def insert_before_close(text, cat_marker, next_marker, new_q):
    start = text.find(cat_marker)
    if next_marker:
        end = text.find(next_marker, start)
        close = text.rfind('\n  ],', start, end)
    else:
        pool_end = text.find('\n};\n\n// ', start)
        close = text.rfind('\n  ]', start, pool_end)
    return text[:close] + ',\n' + new_q + text[close:]

content = insert_before_close(content, '  creation: [', '\n\n  structure: [', NEW_CREATION)
content = insert_before_close(content, '  structure: [', '\n\n  comportement: [', NEW_STRUCTURE)
content = insert_before_close(content, '  comportement: [', '\n\n  solid: [', NEW_COMPORTEMENT)
content = insert_before_close(content, '  solid: [', None, NEW_SOLID)

with open('C:/Users/layeu/Downloads/javastudy/qcm.html', 'w', encoding='utf-8') as f:
    f.write(content)

for cat in ['creation', 'structure', 'comportement', 'solid']:
    cats = ['creation', 'structure', 'comportement', 'solid']
    start = content.find(f'  {cat}: [')
    if cat != 'solid':
        nxt = cats[cats.index(cat)+1]
        end = content.find(f'  {nxt}: [', start)
    else:
        end = content.find('\n};', start)
    count = content[start:end].count('correct:')
    print(f'{cat}: {count} questions')

print('Done!')
