import fastapi as _fast
import sqlalchemy.orm as _orm
import schema, model
from connexion import engine
from connexion import get_db
from fastapi.middleware.cors import CORSMiddleware


model.Base.metadata.create_all(engine)


app = _fast.FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home')
def home():
    return 'home'


@app.get('/all')
def get_all(db: _orm.Session = _fast.Depends(get_db)):
    all_data = db.query(model.Compta).all()
    return all_data


@app.get('/one/{id}')
def get_one(id: int, db: _orm.Session = _fast.Depends(get_db)):
    one_data = db.query(model.Compta).filter(model.Compta.id==id)

    if not one_data.first():
        return '404'

    return one_data.first()


@app.post('/new')
def create_new(req: schema.Compta, db: _orm.Session = _fast.Depends(get_db)):

    new_compte = model.Compta(
        numero=req.numero,
        nom_class=req.nom_class
    )

    db.add(new_compte)
    db.commit()
    db.refresh(new_compte)

    return new_compte


@app.delete('/delete/{id}')
def delete_one(id: int, db: _orm.Session = _fast.Depends(get_db)):
    one_data = db.query(model.Compta).filter(model.Compta.id==id)

    if not one_data.first():
        return '404'
    
    one_data.delete(synchronize_session=False)
    db.commit()
    return 'success'


@app.put('/update/{id}')
def update_one(req: schema.Compta, id: int, db: _orm.Session = _fast.Depends(get_db)):
    one_data = db.query(model.Compta).filter(model.Compta.id==id)

    if not one_data.first():
        return '404'
    
    one_data.update(dict(req))
    db.commit()
    
    return 'succes'