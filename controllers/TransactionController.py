from flask import jsonify, request
from config.database import get_db
from models.transaction_model import Transaction
from sqlalchemy.orm import Session

def get_all_transactions():
    db: Session = next(get_db())
    data = db.query(Transaction).all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "amount": float(t.amount),
        "type": t.type,
        "category_id": t.category_id,
        "note": t.note,
        "date": t.date,
        "created_at": t.created_at,
        "updated_at": t.updated_at
    } for t in data])

def get_transaction(id):
    db: Session = next(get_db())
    tx = db.query(Transaction).get(id)
    if not tx:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    return jsonify({
        "id": tx.id,
        "title": tx.title,
        "amount": float(tx.amount),
        "type": tx.type,
        "category_id": tx.category_id,
        "note": tx.note,
        "date": tx.date,
        "created_at": tx.created_at,
        "updated_at": tx.updated_at
    })

def add_transaction():
    db: Session = next(get_db())
    body = request.json
    new_tx = Transaction(**body)
    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)
    return jsonify({"message": "Transaksi berhasil ditambahkan", "id": new_tx.id})

def update_transaction(id):
    db: Session = next(get_db())
    tx = db.query(Transaction).get(id)
    if not tx:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    body = request.json
    for key, value in body.items():
        setattr(tx, key, value)
    db.commit()
    db.refresh(tx)
    return jsonify({"message": "Transaksi diperbarui", "id": tx.id})

def delete_transaction(id):
    db: Session = next(get_db())
    tx = db.query(Transaction).get(id)
    if not tx:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    db.delete(tx)
    db.commit()
    return jsonify({"message": "Transaksi dihapus"})
