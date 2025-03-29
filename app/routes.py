from flask import jsonify, request, Blueprint
import numpy as np
from datetime import datetime, timedelta, timezone
from app.transacaorepository import TransacaoRepository
from app.models import Transacao

main_routes = Blueprint('main_routes', __name__)
TransacaoRepository = TransacaoRepository()


@main_routes.route('/transacao', methods=['POST'])
def create_transacao():
    try:
        data = request.get_json()
        if not data or 'valor' not in data or 'dataHora' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Parse datetime
        try:
            data_hora = datetime.fromisoformat(data['dataHora'].replace('Z', '+00:00'))
        except ValueError:
            raise ValueError("Invalid datetime format. Use ISO 8601 (e.g., '2023-11-15T14:30:00Z')")

        # Create and validate
        transacao = Transacao(valor=data['valor'], dataHora=data_hora)
        validar_transacao(transacao)
        TransacaoRepository.addTransacao(transacao)

        return jsonify({'status': 'created'}), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 422
    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'error': 'Bad request'}), 400


@main_routes.route('/transacao', methods= ['DELETE'])
def delete_transacao():
    TransacaoRepository.limpar()
    return '', 200



@main_routes.route('/estatistica', methods=['GET'])
def get_estatistica():
    transacoes = TransacaoRepository.getTransacao()
    tempo_limite = datetime.now(timezone.utc) - timedelta(minutes=60)
    transacoes_recente = [
        t for t in transacoes if t.dataHora > tempo_limite
    ]
    if transacoes_recente:
        valores = np.array([t.valor for t in transacoes_recente])
        count = len(transacoes_recente)
        sum_valor = np.sum(valores)
        avg_valor = np.mean(valores)
        min = np.min(valores)
        max = np.max(valores)
    else:
        count = 0
        sum_valor = 0
        avg_valor = 0
        min= 0
        max= 0

    return jsonify({
        'Count': count,
        'Sum': sum_valor,
        'Avg': avg_valor,
        'Min': min,
        'Max': max
    })


def validar_transacao(transacao):
    if transacao.valor < 0:
        raise ValueError("Valor negativo não permitido")

    if transacao.dataHora > datetime.now(timezone.utc):
        raise ValueError("Data futura não permitida")
