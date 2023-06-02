from fastapi.testclient import TestClient
from projet.main import app
from projet.routes.conditionnement_route import ConditionnementSchema

client = TestClient(app)

# Routes conditionnement


def test_get_all_conditionnement():
    """
    ROUTE GET
    :return: TOUS LES CONDITIONNEMENT
    """
    try:
        response = client.get("conditionnement/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        print(response.json())
        print(f"\033[34mtest route conditionnement all Ok\033[0m")
    except Exception as e:
        print(f"\033[91Exception test_get_all_conditionnement : {str(e)}\033[0m")


def test_get_conditionnement_by_weight():
    """
    ROUTE GET
    :return: UN CONDITIONNEMENT ADAPTE AU POIDS DU COLIS
    """
    try:
        response = client.get("conditionnement/200")
        assert response.status_code == 200

        # Conversion de l'objet JSON en instance de ConditionnementSchema
        conditionnement = ConditionnementSchema(**response.json())

        assert isinstance(conditionnement, ConditionnementSchema)
        assert conditionnement.poidscondit == 200
        print(conditionnement)
        print(f"\033[34mtest route conditionnement par poids Ok\033[0m")
    except Exception as e:
        print(f"\033[91Exception test_get_conditionnement_by_weight : {str(e)}\033[0m")


def test_create_conditionnement():
    """
    ROUTE POST
    :return: UN NOUVEAU CONDITIONNEMENT CREER
    """
    # Données de test
    new_conditionnement_data = {
        "libcondit": "conditionnement test",
        "poidscondit": 100,
        "prixcond": 10,
        "ordreimp": 0
    }
    try:
        # Envoi de la requête POST
        response = client.post("conditionnement/", json=new_conditionnement_data)

        # Vérification de la réponse
        assert response.status_code == 200
        conditionnement_json = response.json()
        # Conversion de l'objet JSON en instance de ConditionnementSchema
        conditionnement_created = ConditionnementSchema(**conditionnement_json)
        # Vérification du type de l'objet (ConditionnementSchema)
        assert isinstance(conditionnement_created, ConditionnementSchema)

        # Vérification des propriétés du conditionnement créé
        assert conditionnement_created.libcondit == new_conditionnement_data["libcondit"]
        assert conditionnement_created.poidscondit == new_conditionnement_data["poidscondit"]
        assert conditionnement_created.prixcond == new_conditionnement_data["prixcond"]
        assert conditionnement_created.ordreimp == new_conditionnement_data["ordreimp"]

        print(conditionnement_created)
        print(f"\033[34mtest route création conditionnement Ok\033[0m")

        # Suppression du conditionnement
        delete_response = client.delete(f"/conditionnement/{conditionnement_created.idcondit}")
        # Vérification de la réponse de suppression
        assert delete_response.status_code == 200
        print(f"\033[36mLe conditionnement de test créé a bien été supprimé de la BDD\033[0m")

    except Exception as e:
        print(f"\033[91mException test_create_conditionnement : {str(e)}\033[0m")

# appel des tests


test_get_all_conditionnement()
test_get_conditionnement_by_weight()
test_create_conditionnement()
