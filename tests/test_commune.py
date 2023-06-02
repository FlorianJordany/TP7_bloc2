from fastapi.testclient import TestClient
from projet.main import app

client = TestClient(app)


def test_get_commune():
    # Préparation des données de test
    commune_id = 1

    # Appel de la route via TestClient
    response = client.get(f"/communes/{commune_id}")

    # Vérifications
    assert response.status_code == 200
    data = response.json()
    print(data)


def test_get_all_commune():
    response = client.get(f"/communes")
    assert response.status_code == 200
    data = response.json()
    print(data)


def test_create_commune():
    new_commune_data = {
        "dep": "93",
        "cp": "13550",
        "ville": "Aix"
    }

    response = client.post("/communes", json=new_commune_data)

    assert response.status_code == 200
    created_commune = response.json()
    assert created_commune["dep"] == new_commune_data["dep"]
    assert created_commune["cp"] == new_commune_data["cp"]
    assert created_commune["ville"] == new_commune_data["ville"]
    print(created_commune)


def test_update_commune():
    commune_id = 5
    modifications = {
        "dep": "92",
        "cp": "92100",
        "ville": "Boulogne"
    }
    response = client.put(f"/communes/{commune_id}", json=modifications)
    assert response.status_code == 200
    updated_client = response.json()
    print(updated_client)
