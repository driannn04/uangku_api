from flask import jsonify, request
from config.database import get_db
from models.goal_model import Goal
from sqlalchemy.orm import Session

def get_all_goals():
    db: Session = next(get_db())
    data = db.query(Goal).all()
    return jsonify([{
        "id": g.id,
        "goal_name": g.goal_name,
        "target_amount": float(g.target_amount),
        "current_amount": float(g.current_amount or 0),
        "deadline": g.deadline,
        "status": g.status,
        "created_at": g.created_at
    } for g in data])

def get_goal(id):
    db: Session = next(get_db())
    g = db.query(Goal).get(id)
    if not g:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    return jsonify({
        "id": g.id,
        "goal_name": g.goal_name,
        "target_amount": float(g.target_amount),
        "current_amount": float(g.current_amount or 0),
        "deadline": g.deadline,
        "status": g.status,
        "created_at": g.created_at
    })

def add_goal():
    db: Session = next(get_db())
    body = request.json
    new_goal = Goal(**body)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return jsonify({"message": "Goal berhasil ditambahkan", "id": new_goal.id})

def update_goal(id):
    db: Session = next(get_db())
    g = db.query(Goal).get(id)
    if not g:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    body = request.json
    for key, value in body.items():
        setattr(g, key, value)
    db.commit()
    db.refresh(g)
    return jsonify({"message": "Goal diperbarui", "id": g.id})

def delete_goal(id):
    db: Session = next(get_db())
    g = db.query(Goal).get(id)
    if not g:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    db.delete(g)
    db.commit()
    return jsonify({"message": "Goal dihapus"})
