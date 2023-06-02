from fastapi.testclient import TestClient
from projet.main import app
from projet.routes.commande_route import CommandeSchema
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

def test_get_all_commandes():
    """
    Recuperer toutes les commandes
    :return:
    """
    response = client.get("/commande/")
    liste_reponse = response.json()
    assert response.status_code == 200
    assert type(liste_reponse) == list


def test_one_commande():
    """
    Recuperer une commande
    :return:
    """
    response = client.get("/commande/34")
    assert response.status_code == 200


def test_create_one_commande_ok():
    """
    Test creation de commande ok
    :return:
    """
    new_commande_data = {
        "codcde": 103,
        "datcde": "2020-10-10",
        "codcli": 1,
        "timbrecli": 1,
        "timbecde": 1,
        "timbrecde": 0,
        "nbcolis": 0,
        "cheqcli": 1.0,
        "idcondit": 1,
        "cdeComt": "Mon Commentaire",
        "barchive": 1,
        "bstock": 1
    }

    try:
        response = client.post("/commande/", json=new_commande_data)
        assert response.status_code == 200
    except IntegrityError:
        print("Erreur d'intégrité")
        raise Exception("Erreur d'intégrité")

    new_commande_compare = CommandeSchema(**client.get("/commande/103").json())

    assert new_commande_compare.codcde == new_commande_data["codcde"]
    assert new_commande_compare.timbrecli == new_commande_data["timbrecli"]
    assert new_commande_compare.cdeComt == new_commande_data["cdeComt"]


def test_create_one_commande_ko():
    """
    Test de creation de commande avec un champ date du mauvais type
    :return:
    """
    new_commande_data = {
        "codcde": 106,
        "datcde": "ma_data",
        "codcli": 1,
        "timbrecli": 1,
        "timbecde": 1,
        "timbrecde": 0,
        "nbcolis": 0,
        "cheqcli": 1.0,
        "idcondit": 1,
        "cdeComt": "Mon Commentaire",
        "barchive": 1,
        "bstock": 1
    }

    response = client.post("/commande/", json=new_commande_data)
    assert response.status_code == 422


def test_delete_one_commande_ok():
    """
    Test suppression de commande ok
    :return:
    """
    response = client.delete("/commande/103")
    assert response.status_code == 200


def test_delete_one_commande_ko():
    """
    Test suppression de commande avec id incorrect
    :return:
    """
    response = client.delete("/commande/-1")
    assert response.status_code == 404