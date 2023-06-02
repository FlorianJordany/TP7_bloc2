from fastapi.testclient import TestClient
from projet.main import app

client = TestClient(app)

def test_get_departement():
    # Préparation des données de test
    departement_id = 93

    # Appel de la route via TestClient
    response = client.get(f"/departement/{departement_id}")

    # Vérifications
    assert response.status_code == 200
    data = response.json()
    print(data)


def test_get_all_departement():
    response = client.get(f"/departement")
    assert response.status_code == 200
    data = response.json()
    print(data)

