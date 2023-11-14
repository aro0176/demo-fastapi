from sqlalchemy import Integer, String, Column
from connexion import Base


class Compta(Base):
    __tablename__ = "classification"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    numero = Column(String, nullable=False)
    nom_class = Column(String, nullable=False)