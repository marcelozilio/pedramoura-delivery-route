
def validate_endereco_request(enderecos):

    if enderecos is None:
        raise ValueError("A lista de endereços pode ser vazia.")

    if len(enderecos) == 0:
        raise ValueError("A lista de endereços deve conter no mínimo 1 item.")

    if len(enderecos) > 10:
        raise ValueError("A lista de endereços deve conter no máximo 10 itens.")
