from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def create_session():
    engine = create_engine('sqlite://', echo=True, future=True)
    session = Session(engine)
    return session
    
