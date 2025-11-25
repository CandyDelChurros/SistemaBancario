
try:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado = valor1 / valor2
    print(resultado)
except (ValueError, TypeError) as e:
    print(f"Erro {e.__class__} : Entrada inválida. Por favor, insira números inteiros.")
except ZeroDivisionError as e:
    print(f"Erro {e.__class__}: Divisão por zero não é permitida.")
except KeyboardInterrupt as e:
    print(f"Erro {e.__class__}: Operação interrompida pelo usuário.")
else:
    # Código a ser executado se não houver exceções
    print("Cálculo realizado com sucesso.")
finally:
    print("Fim da operação.")
    # fechamento de recursos, se necessário (arquivos, conexões, etc.)


def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    return True

# garantir que a função lança a exceção corretamente
try:
    validar_idade(-5)
except ValueError as e:
    print(f"Erro {e.__class__}: {e}")

# Exceção personalizada
# Base Exception
class ErroValidacao(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

class IdadeInvalidaError(ErroValidacao):
    
    def __init__(self, idade, codigo=404, mensagem="Idade inválida fornecida."):
        self.idade = idade
        self.codigo = codigo

        super().__init__(mensagem)
    def __str__(self):
        return super().__str__() + f" (Idade: {self.idade}, Código: {self.codigo})"