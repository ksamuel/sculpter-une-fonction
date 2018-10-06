# Une fonction simple


def afficher(liste):
    for element in liste:
        print("-", element)


# Eviter les effets de bord


def afficher(liste):
    morceaux = []
    for element in liste:
        morceaux.append("- " + str(element))
    return "\n".join(morceaux)


# Rajouter des paramètres, et prévoir une valeur par defaut


def afficher(liste, prefix="-"):
    morceaux = []
    for element in liste:
        morceaux.append(prefix + " " + str(element))
    return "\n".join(morceaux)


# Préférer la méthode format


def afficher(liste, prefix="-", template="{prefix} {element}"):
    morceaux = []
    for element in liste:
        ligne = template.format(prefix=prefix, element=element)
        morceaux.append(ligne)
    return "\n".join(morceaux)


# Adopter le duck typing et le paramétrage dynamique


from itertools import chain


def afficher(iterable, *iterables, prefix="-", template="{prefix} {element}"):
    morceaux = []
    for element in chain(iterable, *iterables):
        ligne = template.format(prefix=prefix, element=element)
        morceaux.append(ligne)
    return "\n".join(morceaux)


# Proposer de l'injection de dépendance


def formater(element, prefix, template):
    return template.format(prefix=prefix, element=element)


def afficher(
    iterable, *iterables, prefix="-", template="{prefix} {element}", formateur=formater
):
    elements = chain(iterable, *iterables)
    morceaux = (formateur(element, prefix, template) for element in elements)
    return "\n".join(morceaux)


# Séparer le traitement des éléments du traitement de la collection


def formater(element, prefix, template):
    return template.format(prefix=prefix, element=element)


def produire(
    iterable, *iterables, prefix="-", template="{prefix} {element}", formateur=formater
):
    elements = chain(iterable, *iterables)
    return (formateur(element, prefix, template) for element in elements)


def afficher(
    iterable, *iterables, prefix="-", template="{prefix} {element}", formateur=formater
):
    return "\n".join(
        produire(
            iterable, *iterables, prefix=prefix, template=template, formateur=formateur
        )
    )


# Ajouter les types hints

from typing import Iterable, Generator, Callable, Any


def formater(element: Any, prefix: str, template: str) -> str:
    return template.format(prefix=prefix, element=element)


def produire(
    iterable: Iterable,
    *iterables: Iterable,
    prefix: str = "-",
    template: str = "{prefix} {element}",
    formateur: Callable = formater
) -> Generator[str, None, None]:
    elements = chain(iterable, *iterables)
    return (formateur(element, prefix, template) for element in elements)


def afficher(
    iterable: Iterable,
    *iterables: Iterable,
    prefix: str = "-",
    template: str = "{prefix} {element}",
    formateur: Callable = formater
) -> str:
    lignes = produire(
        iterable, *iterables, prefix=prefix, template=template, formateur=formateur
    )
    return "\n".join(lignes)


# Ajouter une docstring


def formater(element: Any, prefix: str, template: str) -> str:
    """ Retourne une représentation d'un objet selon un template

    Cette fonction est utilisée dans le contexte de produire() et afficher()
    afin de formater chaque éléments des itérables traités.

    Args:
        element: L'objet à formater

        prefix: Un préfix optionel a placer, généralement avant la
                représentation de l'objet (ceci peut changer selon le template)

        template: Le template utilisant la syntaxe de str.format() qui va
                  servir à choisir comment formater l'objet. Le template
                  possède à sa disposition les variables "prefix" et "element".

    Example:

        >>> formater(1, "*", "[{prefix}] {element}")
        '[*] 1'

    Returns:
        La réprésentation de l'objet sous forme de chaîne de caractères.
    """
    return template.format(prefix=prefix, element=element)


def produire(
    iterable: Iterable,
    *iterables: Iterable,
    prefix: str = "-",
    template: str = "{prefix} {element}",
    formateur: Callable = formater
) -> Generator[str, None, None]:
    """ Génère une version formatée avec `formateur` de chaque élément des itérables

    Args:
        iterable: Un itérable dont on veut formater les éléments

        iterables: Tout autre itérable qu'on souhaite concaténer au premier
                   avant le traitement.

        prefix: Un préfix optionel a placer, généralement avant la
                représentation de chaque objet (ceci peut changer selon le template)

        template: Le template utilisant la syntaxe de str.format() qui va
                  servir à choisir comment formater chaque objet. Le template
                  possède à sa disposition les variables "prefix" et "element".

        formateur: La fonction utilisée pour formateur chaque élément de
                   l'itérable. Par défaut, appelle formater()

    Example:

        >>> list(produire([1, 2, 3], "*", "[{prefix}] {element}"))
        ['[*] 1', '[*] 2', '[*] 3']

    Returns:
        Un générateur dont chaque élément est la une représentation sous forme
        de chaîne de caractères d'un des éléments des itérables passés en
        paramètres.
    """

    elements = chain(iterable, *iterables)
    return (formateur(element, prefix, template) for element in elements)


def afficher(
    iterable: Iterable,
    *iterables: Iterable,
    prefix: str = "-",
    template: str = "{prefix} {element}",
    formateur: Callable = formater
) -> str:
    """ Retourne une représentation sous forme de string des itérables

    Args:
        iterable: Un itérable dont on veut formater les éléments

        iterables: Tout autre itérable qu'on souhaite concaténer au premier
                   avant le traitement.

        prefix: Un préfix optionel a placer, généralement avant la
                représentation de chaque objet (ceci peut changer selon le template)

        template: Le template utilisant la syntaxe de str.format() qui va
                  servir à choisir comment formater chaque objet. Le template
                  possède à sa disposition les variables "prefix" et "element".

        formateur: La fonction utilisée pour formateur chaque élément de
                   l'itérable. Par défaut, appelle formater()

    Example:

        >>> print(afficher([1, 2, 3], "*", "[{prefix}] {element}")))
        [*] 1
        [*] 2
        [*] 3

    Returns:
        Une chaîne de caractères ou chaque ligne est la une représentation
        sous forme de chaîne de caractères d'un des éléments des itérables
         passés en paramètres.
    """
    lignes = produire(
        iterable, *iterables, prefix=prefix, template=template, formateur=formateur
    )
    return "\n".join(lignes)


# Laquelle de ces fonctions est la meilleure ?
