from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import FoundItem
from app.schemas import FoundItemCreate, FoundItemUpdate
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/found-items",
    tags=["Found Items"]
)


@router.post("/")
def create_found_item(
    item: FoundItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    found_item = FoundItem(
        **item.dict(),
        user_id=current_user.id
    )

    db.add(found_item)
    db.commit()
    db.refresh(found_item)

    return found_item


@router.get("/")
def get_found_items(
    status: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(FoundItem)

    if status:
        query = query.filter(
            FoundItem.status == status
        )

    return query.offset(skip).limit(limit).all()


@router.get("/{item_id}")
def get_found_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(FoundItem).filter(
        FoundItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    return item


@router.put("/{item_id}")
def update_found_item(
    item_id: int,
    item_data: FoundItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    item = db.query(FoundItem).filter(
        FoundItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
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
def delete_found_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    item = db.query(FoundItem).filter(
        FoundItem.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Found item not found"
        )

    if item.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Found item deleted"
    }