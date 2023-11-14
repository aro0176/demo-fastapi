import pydantic as _pydantic


class Compta(_pydantic.BaseModel):
    numero: int
    nom_class: str

    class Config():
        from_attributes = True