from german_article_classifier.datapipeline.transform import (
    remove_numbers,
    remove_punctuation,
    stop_word_removal,
    map_umlaut,
)


def test_remove_numbers():
    t1 = "5454545454, 454544,454,5 45454545sdajakwjka 48"
    t2 = "st4445 4154 .,48"

    res1 = remove_numbers(document=t1)
    res2 = remove_numbers(document=t2)

    assert res1 == ", ,, sdajakwjka "
    assert res2 == "st  .,"


def test_remove_punctuation():
    t1 = "asd."
    t2 = "!? as ?"
    t3 = "..@~}:Ls "

    assert remove_punctuation(document=t1) == "asd"
    assert remove_punctuation(document=t2) == " as "
    assert remove_punctuation(document=t3) == "Ls "


def test_stop_word_removal():
    t1 = "das uberalles"

    assert stop_word_removal(document=t1) == "uberalles"


def test_map_umlaut():
    t1 = "überalles"
    t2 = "ä"
    t3 = "öberr"
    t4 = "ëß"

    assert map_umlaut(document=t1) == "uberalles"
    assert map_umlaut(document=t2) == "a"
    assert map_umlaut(document=t3) == "oberr"
    assert map_umlaut(document=t4) == "eb"
