from fastapi.testclient import TestClient
from projet.main import app

clients = TestClient(app)

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