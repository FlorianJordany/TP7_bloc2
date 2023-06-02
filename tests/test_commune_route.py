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