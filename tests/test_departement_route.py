from fastapi.testclient import TestClient
from projet.main import app

client = TestClient(app)

'''
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


def test_create_departement():
    new_departement_data = {
        "code_dept": "94",
        "nom_dept": "Val-de-Marne",
        "ordre_aff_dept": 5
    }

    response = client.post("/departement", json=new_departement_data)

    assert response.status_code == 200
    created_departement = response.json()
    assert created_departement["code_dept"] == new_departement_data["code_dept"]
    assert created_departement["nom_dept"] == new_departement_data["nom_dept"]
    assert created_departement["ordre_aff_dept"] == new_departement_data["ordre_aff_dept"]
    print(created_departement)

'''
def test_update_departement():
    departement_id = 92
    modifications = {
        "code_dept": "92",
        "nom_dept": "Hauts-de-Seine",
        "ordre_aff_dept": 6
    }
    response = client.put(f"/departement/{departement_id}", json=modifications)
    assert response.status_code == 200
    updated_client = response.json()
    print(updated_client)
