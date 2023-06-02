from fastapi.testclient import TestClient
from config.database import get_db
from projet.main import app
from projet.models import Client
from projet.routes.client_route import ClientSchema
from projet.routes.commande_route import CommandeSchema
from projet.routes.conditionnement_route import ConditionnementSchema
from sqlalchemy.exc import IntegrityError

clients = TestClient(app)

################ CLIENT_ROUTE ################

# GET route /clients/ ( récupère tous les clients )
def test_get_all_clients():
    try:
        response = clients.get("/clients/")
        assert response.status_code == 200
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")


# GET route /clients/{client_id} ( récupère les infos d'un client en fonction de son ID )
def test_get_client():
    try:
        client_id = 1
        response = clients.get(f"/clients/{client_id}")
        assert response.status_code == 200
        data = response.json()
        print(data)

    except Exception as e:
        print(f"Erreur: {str(e)}")


# PUT route /client/update/{client_id} ( modifier les infos d'un client en fonction de son ID )
def test_update_client():
    client_id = 1
    modifications = {
        "genrecli": "Mrs",
        "nomcli": "Duval",
        "prenomcli": "Eude",
        "adresse1cli": "2 rue test",
        "adresse2cli": "",
        "adresse3cli": "",
        "villecli_id": 1,
        "telcli": "0606060606",
        "emailcli": "0606@0606.com",
        "portcli": "0606050504",
        "newsletter": 1
    }
    try:
        response = clients.put(f"/clients/update/{client_id}", json=modifications)
        assert response.status_code == 200
        updated_client = response.json()
        print(updated_client)
    except Exception as e:
        print(f"Erreur: {str(e)}")


# POST route /clients/create ( permet de créer un nouvel utilisateur )
def test_create_client():
    new_client_data = {
        "genrecli": "Mrs",
        "nomcli": "ULTIME",
        "prenomcli": "Eude",
        "adresse1cli": "2 rue test",
        "adresse2cli": "",
        "adresse3cli": "",
        "villecli_id": 1,
        "telcli": "0606060606",
        "emailcli": "0606@0606.com",
        "portcli": "0606050504",
        "newsletter": 1
    }

    try:
        response = clients.post("/clients/create", json=new_client_data)

        assert response.status_code == 200
        json_client = response.json()
        created_client = ClientSchema(**json_client)

        assert isinstance(created_client, ClientSchema)

        assert created_client.genrecli == new_client_data["genrecli"]
        assert created_client.nomcli == new_client_data["nomcli"]
        assert created_client.prenomcli == new_client_data["prenomcli"]
        assert created_client.adresse1cli == new_client_data["adresse1cli"]
        assert created_client.adresse2cli == new_client_data["adresse2cli"]
        assert created_client.adresse3cli == new_client_data["adresse3cli"]
        assert created_client.villecli_id == new_client_data["villecli_id"]
        assert created_client.telcli == new_client_data["telcli"]
        assert created_client.emailcli == new_client_data["emailcli"]
        assert created_client.portcli == new_client_data["portcli"]
        assert created_client.newsletter == new_client_data["newsletter"]
        print(created_client)

        created_client_id = json_client["codcli"]

        db = get_db()
        session = next(db)

        session.query(Client).filter_by(codcli=created_client_id).delete()
        session.commit()

        deleted_client = session.get(Client, created_client_id)
        assert deleted_client is None

    except Exception as e:
        print(f"Erreur: {str(e)}")


################ POIDS_ROUTE ################

# GET route /poids/ ( récupère tous les clients )
def test_get_all_poids():
    try:
        response = clients.get("/poids/")
        assert response.status_code == 200
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")


# GET route /poids/{id_poids} ( récupère les infos d'un poids en fonction de son ID  )
def test_get_poids():
    try:
        id_poids = 1
        response = clients.get(f"/poids/{id_poids}")
        assert response.status_code == 200
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")

################ VIGNETTE_ROUTE ################

# GET route /vignette/ ( récupère tous les clients )
def test_get_all_vignette():
    try:
        response = clients.get("/vignette/")
        assert response.status_code == 200
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")

# GET route /vignette/{id_vignette} ( récupère les infos d'un poids en fonction de son ID )
def test_get_vignette():
    try:
        id_vignette = 1
        response = clients.get(f"/vignette/{id_vignette}")
        assert response.status_code == 200
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")

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
