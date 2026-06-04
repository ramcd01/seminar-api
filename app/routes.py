from flask import Blueprint, jsonify, request
from .db import get_db_connection
import mysql.connector

bp = Blueprint('api', __name__)

# 5.3 헬스체크
@bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

# 5.1 세미나룸 CRUD
@bp.route('/api/rooms', methods=['GET'])
def get_rooms():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True, buffered=True)
    cur.execute("SELECT * FROM rooms")
    items = cur.fetchall()
    cur.close(); conn.close()
    return jsonify({"items": items, "count": len(items)})

@bp.route('/api/rooms/<int:id>', methods=['GET'])
def get_room(id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True, buffered=True)
    cur.execute("SELECT * FROM rooms WHERE id = %s", (id,))
    item = cur.fetchone()
    cur.close(); conn.close()
    return jsonify(item) if item else ("Not Found", 404)

@bp.route('/api/rooms', methods=['POST'])
def create_room():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO rooms (name, capacity, equipment) VALUES (%s, %s, %s)", 
                (data['name'], data['capacity'], data.get('equipment')))
    conn.commit()
    room_id = cur.lastrowid
    cur.close(); conn.close()
    return jsonify({"id": room_id, "message": "created"}), 201

@bp.route('/api/rooms/<int:id>', methods=['PUT'])
def update_room(id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE rooms SET name=%s, capacity=%s, equipment=%s WHERE id=%s", 
                (data['name'], data['capacity'], data.get('equipment'), id))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"id": id, "message": "updated"})

@bp.route('/api/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM rooms WHERE id=%s", (id,))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"id": id, "message": "deleted"})

# 5.2 예약 CRUD
@bp.route('/api/reservations', methods=['GET'])
def get_reservations():
    room_id = request.args.get('room_id')
    date = request.args.get('date')
    query = "SELECT * FROM reservations WHERE 1=1"
    params = []
    if room_id:
        query += " AND room_id = %s"
        params.append(room_id)
    if date:
        query += " AND date = %s"
        params.append(date)
    
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True, buffered=True)
    cur.execute(query, tuple(params))
    items = cur.fetchall()
    cur.close(); conn.close()
    return jsonify({"items": items, "count": len(items)})

@bp.route('/api/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO reservations (room_id, user_name, user_email, date, start_time, end_time, purpose) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (data['room_id'], data['user_name'], data['user_email'], data['date'], data['start_time'], data['end_time'], data['purpose']))
    conn.commit()
    res_id = cur.lastrowid
    cur.close(); conn.close()
    return jsonify({"id": res_id, "message": "reserved"}), 201

@bp.route('/api/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id=%s", (id,))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"id": id, "message": "cancelled"})
