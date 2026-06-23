from fastapi import FastAPI

from app.database import engine
from app import models
from app.routers.found_items import router as found_items_router
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.lost_items import router as lost_items_router
from app.routers.matches import router as matches_router
from app.routers.claims import router as claims_router
from app.routers.reports import router as reports_router
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lost & Found Management System")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(lost_items_router)
app.include_router(found_items_router)
app.include_router(matches_router)
app.include_router(claims_router)
app.include_router(reports_router)


@app.get("/")
def home():
    return {"message": "Lost & Found API Running"}