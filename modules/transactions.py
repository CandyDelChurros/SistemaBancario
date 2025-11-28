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
                raise ValueError("Account not found.")
            
            if balance <= 0:
                raise ValueError("Value must be greater than zero.")
            
            account.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Deposit of R$ {balance:.2f} completed.",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Unexpected error: {error}"}
    
    @staticmethod
    def withdraw(db, number, balance):
        try: 
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Account not found.")
            
            if balance <= 0:
                raise ValueError("Value must be greater than zero.")
            
            if account.balance < balance:
                raise ValueError("Insufficient balance.")
            
            account.balance -= balance

            return {
                "status": "ok",
                "mensagem": f"Withdrawal of R$ {balance:.2f} completed.",
                "saldo_atual": account.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Unexpected error: {error}"}

    @staticmethod
    def transfer(db, number_from, number_to, balance):
        try:
            account_from = Transactions.find_account(db, number_from)
            account_to = Transactions.find_account(db, number_to)

            if account_from is None:
                raise ValueError("Origin account not found.")
            
            if account_to is None:
                raise ValueError("Destination account not found.")
            
            if balance <= 0:
                raise ValueError("Value must be greater than zero.")
            
            if account_from.balance < balance:
                raise ValueError("Insufficient balance.")
            
            account_from.balance -= balance
            account_to.balance += balance

            return {
                "status": "ok",
                "mensagem": f"Transfer of R$ {balance:.2f} completed.",
                "origem": account_from.balance,
                "destino": account_to.balance
            }
        
        except ValueError as error:
            return {"status": "erro", "mensagem": str(error)}
        
        except Exception as error:
            return {"status": "erro", "mensagem": f"Unexpected error: {error}"}

    @staticmethod
    def statement(db, number):
        try:
            account = Transactions.find_account(db, number)

            if account is None:
                raise ValueError("Account not found.")
            
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
            return {"status": "erro", "mensagem": f"Unexpected error: {error}"}
