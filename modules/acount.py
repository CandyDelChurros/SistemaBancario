class Account:
    def __init__(self, client, type, number, bank="001"):
        self.client = client
        self.type = type
        self.number = number
        self.balance = 0.0
        self.status = "Ativa"

    @staticmethod
    def generate_account_number(db):
        return str(1000 + len(db["accounts"])+1)
        
    @staticmethod
    def open_account(db, cpf, type="corrente"):
        try:
            if cpf.strip()== "":
                raise ValueError("Coloque o CPF!")
                
            if not cpf.isdigit() or len(cpf) !=11:
               raise ValueError("PRecisa ter 11 digitos")
                
            client_found = None
            for client in db["clients"]:
                if client.cpf == cpf:
                    client_found = client
                    break
                if client_found is None:
                    raise ValueError("Essa conta não existe")
                            
            numero_conta = Account.generate_account_number(db)

            account = Account(
                client=client_found,
                tupe=type,
                number=account_number
            )

            db["accounts"].append(account)

            return {
                "status": "ok",
                "mensagem": "Conta Criada!",
                "conta": {
                    "agencia": account.bank,
                    "numero": account.number,
                    "type": account.type,
                    "cpf": client_found.cpf,
                    "nome": client_found.name
                }
            }
        except ValueError as error:
            return {
                "status": "erro",
                "mensagem":str(error)
            }
        except Exception as error:
            return {
                "status": "erro",
                "mensagem":f"Erro ao criar conta: {error}"
            }
            
