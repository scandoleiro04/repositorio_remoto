import json

ARQUIVO_AGENDA = "agenda.json"

def carregar_agenda():
    try:
        with open(ARQUIVO_AGENDA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os dados. O arquivo pode estar corrompido.")
        return []

def salvar_agenda(agenda):
    try:
        with open(ARQUIVO_AGENDA, "w", encoding="utf-8") as arquivo:
            json.dump(agenda, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

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

def exibir_contato(contato):
    status = "(Favorito)" if contato["favorito"] else ""
    print(f"{contato['nome']} - {contato['telefone']} {status}")

def adicionar_contato(agenda):
    try:
        nome = input("Nome: ").strip()
        if not nome:
            raise ValueError("O nome não pode estar vazio!")

        telefone = input("Telefone: ").strip()
        if not telefone:
            raise ValueError("O telefone não pode estar vazio!")

        favorito = input("Favorito (s/n): ").strip().lower() == 's'
        agenda.append({"nome": nome, "telefone": telefone, "favorito": favorito})
        salvar_agenda(agenda)
        print("Contato adicionado com sucesso!")

    except ValueError as e:
        print(f"Erro: {e}")

def listar_contatos(agenda):
    if not agenda:
        print("Nenhum contato na agenda.")
        return

    for contato in sorted(agenda, key=lambda x: x["nome"].lower()):
        exibir_contato(contato)

def buscar_contato(agenda):
    nome = input("Nome do contato: ").strip().lower()
    
    for contato in agenda:
        if contato["nome"].lower() == nome:
            exibir_contato(contato)
            return
    
    print("Contato não encontrado.")

def atualizar_contato(agenda):
    nome = input("Nome do contato a atualizar: ").strip().lower()
    
    for contato in agenda:
        if contato["nome"].lower() == nome:
            novo_telefone = input("Novo telefone (deixe vazio para manter): ").strip()
            if novo_telefone:
                contato["telefone"] = novo_telefone
                salvar_agenda(agenda)
                print("Contato atualizado com sucesso!")
            return
    
    print("Contato não encontrado.")    

def remover_contato(agenda):
    nome = input("Nome do contato a remover: ").strip().lower()
    nova_agenda = [c for c in agenda if c["nome"].lower() != nome]
    
    if len(nova_agenda) < len(agenda):
        agenda[:] = nova_agenda
        salvar_agenda(agenda)
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")

def favoritar_contato(agenda):
    nome = input("Nome do contato: ").strip().lower()
    
    for contato in agenda:
        if contato["nome"].lower() == nome:
            contato["favorito"] = not contato["favorito"]
            salvar_agenda(agenda)
            print("Status de favorito atualizado!")
            return
    
    print("Contato não encontrado.")       

def listar_favoritos(agenda):
    favoritos = [c for c in agenda if c["favorito"]]
    
    if favoritos:
        for contato in favoritos:
            exibir_contato(contato)
    else:
        print("Nenhum contato favorito.")

def main():
    agenda = carregar_agenda()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        opcoes = {
            '1': adicionar_contato,
            '2': listar_contatos,
            '3': buscar_contato,
            '4': atualizar_contato,
            '5': remover_contato,
            '6': favoritar_contato,
            '7': listar_favoritos
        }
        
        if opcao == '8':
            print("Saindo...")
            break
        elif opcao in opcoes:
            try:
                opcoes[opcao](agenda)
            except Exception as e:
                print(f"Erro inesperado: {e}")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
