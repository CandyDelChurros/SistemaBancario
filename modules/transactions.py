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
                raise ValueError("Saldo insuficiente")
            
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
            