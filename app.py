from modules.clients import Client
from modules.account import Account
from modules.transactions import Transactions
from services.database import db


def login_user():
    try:
        cpf = input("Enter your CPF: ")

        for client in db["clients"]:
            if client.cpf == cpf:
                print(f"\nWelcome, {client.name}!\n")

                for acc in db["accounts"]:
                    if acc.client.cpf == cpf:
                        return acc

                print("Client registered but without an account. Creating account...")
                result = Account.open_account(db, cpf)
                print(result["mensagem"])
                return db["accounts"][-1]

        print("CPF not registered.")
        return None

    except Exception as e:
        print("Error during login:", e)
        return None