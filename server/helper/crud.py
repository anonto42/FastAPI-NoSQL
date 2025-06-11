from sqlmodel import Session, SQLModel, select
from typing import Type, TypeVar, Optional, Dict, Any, List
from server.db.db_connection import engine

ModelType = TypeVar("ModelType", bound=SQLModel)

def create_item(model: Type[ModelType], data: dict) -> ModelType:
    
    with Session(engine) as session:
        db_obj = model(**data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

def read_item(model: Type[ModelType], item_id: Any) -> Optional[ModelType]:

    with Session(engine) as session:
        return session.get(model, item_id)
    
def get_items(
    model: Type[ModelType], 
    filters: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0
) -> List[ModelType]:
    with Session(engine) as session:
        query = select(model)
        
        if filters:
            for key, value in filters.items():
                column = getattr(model, key, None)
                if column is not None:
                    query = query.where(column == value)
        
        query = query.offset(offset).limit(limit)
        results = session.exec(query).all()
        return results

def update_item(model: Type[ModelType], item_id: Any, data: Dict[str, Any]) -> Optional[ModelType]:

    with Session(engine) as session:
        db_obj = session.get(model, item_id)
        if not db_obj:
            return None
        for key, value in data.items():
            setattr(db_obj, key, value)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

def delete_item(model: Type[ModelType], item_id: Any) -> bool:

    with Session(engine) as session:
        db_obj = session.get(model, item_id)
        if not db_obj:
            return False
        session.delete(db_obj)
        session.commit()
        return True
