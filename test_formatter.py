from formatter import afficher, formater, produire


def test_afficher():

    assert afficher([1, 2, 3]) == "- 1\n- 2\n- 3"

    assert afficher([1, 2, 3], prefix="*") == "* 1\n* 2\n* 3"

    assert afficher([1, 2, 3], template="{element} {prefix}") == "1 -\n2 -\n3 -"

    assert afficher([1, 2, 3], formateur=lambda e, p, t: "bla") == "bla\nbla\nbla"


def test_formater():
    assert formater(1, "*", "[{prefix}] {element}") == "[*] 1"


def test_produire():

    assert list(produire([1, 2, 3])) == ["- 1", "- 2", "- 3"]

    assert list(produire([1, 2, 3], prefix="*")) == ["* 1", "* 2", "* 3"]

    assert list(produire([1, 2, 3], template="{element} {prefix}")) == [
        "1 -",
        "2 -",
        "3 -",
    ]
