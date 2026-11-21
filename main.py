from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

users_db = {
    1 : {"id" : 1, "name" : "mario", "email" : "mario@gmail.com"},
    2 : {"id" : 2, "name" : "anna", "email" : "anna@gmail.com"},
    3 : {"id" : 3, "name" : "luigi", "email" : "luigi@gmail.com"}
}
class User(BaseModel):
    id: int
    name: str
    email: str
      
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None

app = FastAPI()

@app.get("/users")
def get_all_users():
    return list(users_db.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users")
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exist ")
    users_db[user.id] = user.dict()
    return {"message": "User created successfully"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user.dict()
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(user_id)
    return {"message": "User deleted successfully"}

@app.patch("/users/{user_id}")
def patch_user(user_id: int, user: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].update(user.model_dump(exclude_unset=True))
    return {"message": "User updated successfully"}





ESERCIZIO

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

prodotti_db = {
    1: {
        "id": 1,
        "nome": "Smartphone",
        "prezzo": 700,00,
        "categoria": "Elettronica",
        "azienda": "Apple",
        "descrizione": "Smartphone di ultima generazione",
        "rating": 4.5
    },
    2: {
        "id": 2,
        "nome": "Caffettiera",
        "prezzo": 24.50,
        "categoria": "Elettrodomestici",
        "azienda": "HomeStyle",
        "descrizione": "Caffettiera 3 tazzine",
        "rating": 4.0
    }
}


class Prodotto(BaseModel):
    id: int
    nome: str
    prezzo: float      # float per gestire i decimali (es. 19.99)
    categoria: str
    azienda: str
    descrizione: str
    rating: float      # float per gestire decimali tra 1 e 5 (es. 4.5)


class ProdottoUpdate(BaseModel):
    nome: str | None = None
    prezzo: float | None = None
    categoria: str | None = None
    azienda: str | None = None
    descrizione: str | None = None
    rating: float | None = None

app = FastAPI()

# --- GET ALL ---
@app.get("/prodotti")
def get_all_prodotti():
    return list(prodotti_db.values())

# --- GET BY ID ---
@app.get("/prodotti/{prodotto_id}")
def get_prodotto(prodotto_id: int):
    if prodotto_id not in prodotti_db:
        raise HTTPException(status_code=404, detail="Prodotto non trovato")
    return prodotti_db[prodotto_id]

# --- POST ---
@app.post("/prodotti")
def create_prodotto(prodotto: Prodotto):
    if prodotto.id in prodotti_db:
        raise HTTPException(status_code=400, detail="Prodotto gia esistente")
    prodotti_db[prodotto.id] = prodotto.model_dump()
    return {"message": "Prodotto creato con successo"}

# --- PUT ---
@app.put("/prodotti/{prodotto_id}")
def update_prodotto(prodotto_id: int, prodotto: Prodotto):
    if prodotto_id not in prodotti_db:
        raise HTTPException(status_code=404, detail="Prodotto non trovato")
    prodotti_db[prodotto_id] = prodotto.model_dump()
    return {"message": "Prodotto aggiornato con successo"}

# --- DELETE ---
@app.delete("/prodotti/{prodotto_id}")
def delete_prodotto(prodotto_id: int):
    if prodotto_id not in prodotti_db:
        raise HTTPException(status_code=404, detail="Prodotto non trovato")
    prodotti_db.pop(prodotto_id)
    return {"message": "Prodotto eliminato con successo"}

# --- PATCH ---
@app.patch("/prodotti/{prodotto_id}")
def patch_prodotto(prodotto_id: int, prodotto: ProdottoUpdate):
    if prodotto_id not in prodotti_db:
        raise HTTPException(status_code=404, detail="Prodotto non trovato")
    prodotti_db[prodotto_id].update(prodotto.model_dump(exclude_unset=True))
    return {"message": "Prodotto aggiornato con successo"}
































































