from fastapi import APIRouter
from . import (
    client_route,
    # commande_router,
    commune_route,
    # conditionnement_router,
    # departement_router,
    # detail_router,
    # detail_objet_router,
    # enseigne_router,
    # objet_router,
    # objet_cond_router,
    # poids_router,
    # role_router,
    # role_utilisateur_router,
    # utilisateur_router,
    # vignette_router,
    # commande_route
)


def get_routes():
    router = APIRouter()
    router.include_router(client_route.router)
    router.include_router(commune_route.router)
    return router
