from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LostItem, FoundItem

router = APIRouter(
    prefix="/api/v1/matches",
    tags=["Matches"]
)


@router.get("/")
def get_matches(db: Session = Depends(get_db)):
    lost_items = db.query(LostItem).all()
    found_items = db.query(FoundItem).all()

    matches = []

    for lost in lost_items:
        for found in found_items:

            if (
                lost.item_name.lower() == found.item_name.lower()
                and lost.category.lower() == found.category.lower()
                and lost.lost_location.lower() == found.found_location.lower()
            ):
                matches.append({
                    "lost_item_id": lost.id,
                    "found_item_id": found.id,
                    "item_name": lost.item_name,
                    "category": lost.category,
                    "location": lost.lost_location
                })

    return matches