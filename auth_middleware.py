from functools import wraps
import jwt
from flask import request, abort
from flask import current_app

user = {
    "racf": "teste",
    "senha": "robo_aut_sust"
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Nenhum token encontrado",
                "data": None,
                "error": "Unauthorized"
            }, 401
        
        try: 
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user=data["racf"]
            if current_user is None:
                return {
                    "message": "Não Autenticado",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "message": "Algo de Errado",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)
    return decorated