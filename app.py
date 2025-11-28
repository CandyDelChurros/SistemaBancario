from modules.clients import Client
from modules.account import Account
from modules.transactions import Transactions
from services.database import db


def login_user():
    try:
        cpf = input("Entre com o CPF: ")

        for client in db["clients"]:
            if client.cpf == cpf:
                print(f"\nBem Vindo, {client.name}!\n")

                for acc in db["accounts"]:
                    if acc.client.cpf == cpf:
                        return acc

                result = Account.open_account(db, cpf)
                print(result["mensagem"])
                return db["accounts"][-1]

        print("CPF Não encontrado.")
        return None

    except Exception as e:
        print("Erro", e)
        return None

def register_user():
    try:
        name = input("Nome: ")
        cpf = input("CPF: ")
        phone = input("Telefone - Celular: ")

        response = Client.sign_client(db, name, cpf, phone)
        print(response["mensagem"])

        if response["status"] == "ok":
            acc_res = Account.open_account(db, cpf)
            print(acc_res["mensagem"])
            return db["accounts"][-1]

        return None

    except Exception as e:
        print("Erro:", e)
        return None

def operations_menu(account):
    while True:
        print(f"Cliente: {account.client.name} | Account: {account.number}")
        print("1 - Deposito")
        print("2 - Saque")
        print("3 - Transferencia")
        print("4 - Boleto")
        print("5 - Logout")
        option = input("Escolha um numero: ")

        try:

            if option == "1":
                value = float(input("Valor do Deposito: "))
                r = Transactions.deposit(db, account.number, value)
                print(r["mensagem"])

            elif option == "2":
                value = float(input("Valor do Saque: "))
                r = Transactions.withdraw(db, account.number, value)
                print(r["mensagem"])

            elif option == "3":
                to_acc = input("Conta para transferencia: ")
                value = float(input("Amount: "))
                r = Transactions.transfer(db, account.number, to_acc, value)
                print(r["mensagem"])

            elif option == "4":
                r = Transactions.statement(db, account.number)
                for k, v in r.items():
                    print(f"{k}: {v}")

            elif option == "5":
                break

            else:
                print("Escolha uma opção certa!")

        except ValueError:
            print("Numero invalido")
        except Exception as e:
            print("Algo de errado aconteceu:", e)

def main():
    logged_account = None

    while True:

        if logged_account is None:
            print("1 - Registrar Cliente")
            print("2 - Login")
            option = input("Escolha 1 numero ")

            if option == "1":
                logged_account = register_user()

            elif option == "2":
                logged_account = login_user()

            else:
                print("Opção Invalida")

        else:
            operations_menu(logged_account)
            logged_account = None 


if __name__ == "__main__":
    main()
