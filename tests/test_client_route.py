from fastapi.testclient import TestClient
from config.database import get_db
from projet.main import app
from projet.models import Client
from projet.routes.client_route import ClientSchema

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