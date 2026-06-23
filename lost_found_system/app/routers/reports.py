from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LostItem, FoundItem, Claim

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)


@router.get("/total-lost-items")
def total_lost_items(db: Session = Depends(get_db)):
    return {
        "total_lost_items": db.query(LostItem).count()
    }


@router.get("/total-found-items")
def total_found_items(db: Session = Depends(get_db)):
    return {
        "total_found_items": db.query(FoundItem).count()
    }


@router.get("/successful-claims")
def successful_claims(db: Session = Depends(get_db)):
    return {
        "successful_claims":
        db.query(Claim).filter(
            Claim.status == "Approved"
        ).count()
    }