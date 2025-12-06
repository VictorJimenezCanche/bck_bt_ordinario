from flask import Blueprint, jsonify 
from bson import ObjectId
from config.db import get_db

health_bp = Blueprint('health', __name__)


@health_bp.route('/', methods=['GET'])
def health():
    return jsonify({"mensaje": "El servidor está activo en el puerto 8080"}), 200