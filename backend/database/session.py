from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from .engine import engine

# From L11-18 + L13-17: Session dependency pattern
def get_session():
    with Session(engine) as session:
        yield session

# From L11-18: Annotated dependency for easier use
SessionDep = Annotated[Session, Depends(get_session)]