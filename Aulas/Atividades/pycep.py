import pycep_correios

Entrada = input("Digite seu CEP: ")
EntradaUsuario = pycep_correios.get_address_from_cep(Entrada)
print(EntradaUsuario)
