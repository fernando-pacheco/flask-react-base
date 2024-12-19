from flask import make_response


def retorno_nao_autorizado():
    return make_response(
        {'message': 'Usuário não autorizado a realizar esta ação.'},
        403,
    )


def atualizar_objeto(kwargs, objeto):
    resposta = make_response({'message': 'Erro ao atulizar item.'}, 400)
    for campo, valor in kwargs.items():
        if campo not in ['usuario_id', 'Authorization'] and valor is not None:

            if campo == 'senha':
                objeto.definir_senha(valor)

            elif hasattr(objeto, campo):
                if isinstance(getattr(objeto, campo), bool):
                    valor = str(valor).lower() == 'true'

                setattr(objeto, campo, valor)

            else:
                resposta = make_response(
                    {'message': f'O campo {campo} não é válido.'},
                    400,
                )

    return objeto, resposta
