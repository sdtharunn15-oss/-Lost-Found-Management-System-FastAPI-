from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LostItem
from app.schemas import LostItemCreate, LostItemUpdate
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/lost-items",
    tags=["Lost Items"]
)


@router.post("/")
def create_lost_item(
    item: LostItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_item = LostItem(
        **item.dict(),
        user_id=current_user.id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.get("/")
def get_lost_items(
    category: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(LostItem)

    if category:
        query = query.filter(
            LostItem.category == category
        )

    return query.offset(skip).limit(limit).all()
    

@router.get("/{item_id}")
def get_lost_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    return item


@router.put("/{item_id}")
def update_lost_item(
    item_id: int,
    item_data: LostItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    if item.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    for key, value in item_data.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


@router.delete("/{item_id}")
def delete_lost_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Lost item not found"
        )

    if item.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    db.delete(item)
    db.commit()

    return {"message": "Lost item deleted"}