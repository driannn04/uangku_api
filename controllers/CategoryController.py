from flask import jsonify, request
from config.database import get_db
from models.category_model import Category
from sqlalchemy.orm import Session

def get_all_categories():
    db: Session = next(get_db())
    data = db.query(Category).all()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "icon": c.icon,
        "color": c.color,
        "created_at": c.created_at
    } for c in data])

def get_category(id):
    db: Session = next(get_db())
    cat = db.query(Category).get(id)
    if not cat:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    return jsonify({
        "id": cat.id,
        "name": cat.name,
        "icon": cat.icon,
        "color": cat.color,
        "created_at": cat.created_at
    })

def add_category():
    db: Session = next(get_db())
    body = request.json
    new_cat = Category(**body)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return jsonify({"message": "Kategori berhasil ditambahkan", "id": new_cat.id})

def update_category(id):
    db: Session = next(get_db())
    cat = db.query(Category).get(id)
    if not cat:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    body = request.json
    for key, value in body.items():
        setattr(cat, key, value)
    db.commit()
    db.refresh(cat)
    return jsonify({"message": "Kategori diperbarui", "id": cat.id})

def delete_category(id):
    db: Session = next(get_db())
    cat = db.query(Category).get(id)
    if not cat:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    db.delete(cat)
    db.commit()
    return jsonify({"message": "Kategori dihapus"})
