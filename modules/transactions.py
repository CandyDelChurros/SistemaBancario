class Transactions:

    @staticmethod
    def find_account(db, number):
        for account in db["accounts"]:
            if account in db["accounts"]:
                if account.number == number:
                    return account
        return None
    
    @staticmethod
    def deposit(db,number, balance):
        try:
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Não existe")
            
            if balance <= 0:
                raise ValueError("Valor tem de ser maior que zero")
            
            account.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Deposito de R$ {balance:2.f} concluido",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Deu Erro"}
    
    @staticmethod
    def withdraw(db, number, balance):
        try: 
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Não existe")
            
            if balance <= 0:
                raise ValueError("Valor tem de ser maior que zero")
            
            if account.balance < balance:
                raise ValueError("Saldo Baixo")
            
            account.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Saque de R$ {balance:2.f} concluido",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Deu Erro"}

    @staticmethod
    def transfer(db, number_from, number_to, balance):
        try:
            account_from = Transactions.find_account(db, number_from)
            account_to = Transactions.find_account(db, number_to)

            if account_from is None:
                raise ValueError("Não existe")
            
            if account_to is None:
                raise ValueError("Conta de destino não encontrada")
            
            if balance <= 0:
                raise ValueError("Valor tem de ser maior que zero")
            
            if account_from.balace < balance:
                raise ValueError("Saldo baixo")
            
            account_from.balance -= balance
            account_to.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Tranferencia de R$ {balance:2.f} concluida",
                "origem": account_from.balance,
                "destino": account_to.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Deu Erro"}

    @staticmethod
    def statement (db,number):
        try:
            account = Transactions.find_account(db,number)

            if account is None:
                raise ValueError("Conta não existe")
            
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
            return {"status": "erro", "mensagem": f"Deu Erro"}

