from fastapi import APIRouter
from . import (
    client_route,
    commande_route,
    commune_route,
    departement_route,
    conditionnement_route,
    poids_route,
    vignette_route
)


def get_routes():
    router = APIRouter()
    router.include_router(client_route.router)
    router.include_router(commune_route.router)
    router.include_router(departement_route.router)
    router.include_router(commande_route.router)
    router.include_router(conditionnement_route.router)
    router.include_router(poids_route.router)
    router.include_router(vignette_route.router)
    return router
