class Client:
    def __init__(self, name, cpf, phone):
        self.name = name
        self.cpf = cpf
        self.phone = phone

    def sign_client(db, name, cpf, phone):
        try:
            if name.strip() == "":
                raise ValueError("Por favor insira um nome!")

            if cpf.strip() == "":
                raise ValueError("Insira o CPF!")

            if not cpf.isdigit() or len(cpf) != 11:
                raise ValueError("O CPF deve ter exatamente 11 dígitos numéricos")

            if phone.strip() == "":
                raise ValueError("Insira o número")

            if not phone.isdigit():
                raise ValueError("O telefone deve conter somente números")

            if len(phone) != 11:
                raise ValueError("O telefone deve ter exatamente 11 dígitos")

            for client in db["clients"]:
                if client.cpf == cpf:
                    raise ValueError("Usuário já cadastrado com esse CPF")

            client = Client(name, cpf, phone)
            db["clients"].append(client)

            return {
                "status": "ok",
                "mensagem": "Usuário criado com sucesso!",
                "client": client
            }

        except ValueError as error:
            return {
                "status": "erro",
                "mensagem": str(error)
            }

        except Exception as error:
            return {
                "status": "erro",
                "mensagem": f"Erro inesperado ao cadastrar cliente: {error}"
            }
