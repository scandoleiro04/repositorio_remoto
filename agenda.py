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

def listar_contatos(agenda):
    for contato in sorted(agenda, key=lambda x: x['nome']):
        print(f"{contato['nome']} - {contato['telefone']} {'(Favorito)' if contato['favorito'] else ''}")

def buscar_contato(agenda):
    nome = input("Nome do contato: ")
    for contato in agenda:
        if contato['nome'] == nome:
            print(f"{contato['nome']} - {contato['telefone']} {'(Favorito)' if contato['favorito'] else ''}")
            return
    print("Contato não encontrado.")

def atualizar_contato(agenda):
    nome = input("Nome do contato a atualizar: ")
    for contato in agenda:
        if contato['nome'] == nome:
            contato['telefone'] = input("Novo telefone: ") or contato['telefone']
            return
    print("Contato não encontrado.")    

def remover_contato(agenda):
    nome = input("Nome do contato a remover: ")
    agenda[:] = [c for c in agenda if c['nome'] != nome] 

def favoritar_contato(agenda):
    nome = input("Nome do contato: ")
    for contato in agenda:
        if contato['nome'] == nome:
            contato['favorito'] = not contato['favorito']
            return
    print("Contato não encontrado.")       

def listar_favoritos(agenda):
    for contato in agenda:
        if contato['favorito']:
            print(f"{contato['nome']} - {contato['telefone']} (Favorito)")    