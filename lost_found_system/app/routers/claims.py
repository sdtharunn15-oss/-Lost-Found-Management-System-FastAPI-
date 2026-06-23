from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Claim, FoundItem
from app.dependencies import get_current_user
from fastapi import BackgroundTasks
from app.utils.email import send_claim_approval_email
router = APIRouter(
    prefix="/api/v1/claims",
    tags=["Claims"]
)


@router.post("/{found_item_id}")
def create_claim(
    found_item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    found_item = db.query(FoundItem).filter(
        FoundItem.id == found_item_id
    ).first()

    if not found_item:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    claim = Claim(
        found_item_id=found_item_id,
        user_id=current_user.id
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim


@router.get("/")
def get_claims(
    status: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Claim)

    if status:
        query = query.filter(
            Claim.status == status
        )

    return query.all()


@router.put("/{claim_id}/approve")
def approve_claim(
    claim_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    claim.status = "Approved"

    found_item = db.query(FoundItem).filter(
        FoundItem.id == claim.found_item_id
    ).first()

    if found_item:
        found_item.status = "Claimed"

    other_claims = db.query(Claim).filter(
        Claim.found_item_id == claim.found_item_id,
        Claim.id != claim.id
    ).all()

    for c in other_claims:
        c.status = "Rejected"

    db.commit()
@router.put("/{claim_id}/approve")
def approve_claim(
    claim_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    return {"message": "Claim approved"}
    

@router.put("/{claim_id}/reject")
def reject_claim(
    claim_id: int,
    db: Session = Depends(get_db)
):
    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    claim.status = "Rejected"

    db.commit()

    return {"message": "Claim rejected"}