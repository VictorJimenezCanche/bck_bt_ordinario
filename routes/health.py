from flask import Blueprint, jsonify 
import os

health_bp = Blueprint('health', __name__)


@health_bp.route('/', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "service": "Backend Banco de Tiempo",
        "port": os.getenv("PORT", 8080),
        "message": "El servidor está activo y funcionando correctamente. Esto no lo deberias de ver:()"}), 200