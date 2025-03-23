def exibir_menu():
    print("""
    AGENDA DE CONTATOS
    1. Adicionar contato
    2. Listar contatos
    3. Buscar contato
    4. Atualizar contato
    5. Remover contato
    6. Favoritar/Desfavoritar contato
    7. Listar contatos favoritos
    8. Sair
    """)
def adicionar_contato(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    favorito = input("Favorito (s/n): ").lower() == 's'
    agenda.append({"nome": nome, "telefone": telefone, "favorito": favorito})    