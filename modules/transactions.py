class Transactions:

    @staticmethod
    def find_account(db, number):
        for account in db["accounts"]:
            if account.number == number:
                return account
        return None
    
    @staticmethod
    def deposit(db, number, balance):
        try:
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Conta não encontrada")
            
            if balance <= 0:
                raise ValueError("Valor não pode ser menor que zero")
            
            account.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Deposito de R$ {balance:.2f} foi feito.",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Erro inesperado: {error}"}
    
    @staticmethod
    def withdraw(db, number, balance):
        try: 
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Conta não encontrada.")
            
            if balance <= 0:
                raise ValueError("Valor não pode ser menor que zero")
            
            if account.balance < balance:
                raise ValueError("Saldo Insuficiente")
            
            account.balance -= balance

            return {
                "status": "ok",
                "mensagem": f"Saque de R$ {balance:.2f} foi feito.",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Erro inesperado: {error}"}

    @staticmethod
    def transfer(db, number_from, number_to, balance):
        try:
            account_from = Transactions.find_account(db, number_from)
            account_to = Transactions.find_account(db, number_to)

            if account_from is None:
                raise ValueError("Conta de origem não encontrada.")
            
            if account_to is None:
                raise ValueError("Conta de Destino não encontrada.")
            
            if balance <= 0:
                raise ValueError("Valor não pode ser menor que zero.")
            
            if account_from.balance < balance:
                raise ValueError("Saldo Insuficiente")
            
            account_from.balance -= balance
            account_to.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Transferencia de R$ {balance:.2f} completa.",
                "origem": account_from.balance,
                "destino": account_to.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Erro inesperado: {error}"}

    @staticmethod
    def statement(db, number):
        try:
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Conta não encontrada.")
            
            return {
                "status": "ok",
                "cliente": account.client.name,
                "cpf": account.client.cpf,
                "agencia": account.bank,
                "conta": account.number,
                "tipo": account.type,
                "saldo": account.balance
            }
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Erro inesperado: {error}"}
