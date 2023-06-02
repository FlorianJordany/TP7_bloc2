from fastapi.testclient import TestClient
from projet.main import app

clients = TestClient(app)

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