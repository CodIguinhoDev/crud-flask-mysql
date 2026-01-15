from flask import Blueprint, jsonify, request
from app.database import conexao_bd
import pymysql


main_routes = Blueprint("main_routes", __name__)


@main_routes.route("/usuarios/<int:id>", methods=["GET"])
def listar_usuarios(id):
    conexao = conexao_bd()
    cursor = conexao.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id,))
    usuarios = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuarios is None:
        return jsonify({"Mensagem": "Usuário não encontrado"}), 404

    return jsonify(usuarios), 200



@main_routes.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()

    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")
    email = dados.get("email")
    data_nascimento = dados.get("data_nascimento")

    conexao = conexao_bd()
    cursor = conexao.cursor()

    sql = "INSERT INTO usuarios (nome, sobrenome, email, data_nascimento) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, sobrenome, email, data_nascimento))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@main_routes.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")
    email = dados.get("email")
    data_nascimento = dados.get("data_nascimento")

    
    conexao = conexao_bd()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    if usuario is None:
        cursor.close()
        conexao.close()
        return jsonify({"Mensagem": "Usuário não encontrado"}), 404

    sql = "UPDATE usuarios SET nome = %s, sobrenome = %s, email = %s, data_nascimento = %s WHERE id = %s"
    cursor.execute(sql, (nome, sobrenome, email, data_nascimento, id))
    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Usuário atualizado com sucesso"}), 200


@main_routes.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    conexao = conexao_bd()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    if usuario is None:
        cursor.close()
        conexao.close()
        return jsonify({"Mensagem": "Usuário não encontrado"}), 404

    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200
