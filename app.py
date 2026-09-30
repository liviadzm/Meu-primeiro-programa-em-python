print("=== Sistema de Notas do Aluno ===")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"A media final e: {media:.2f}")
if media >=7:
    print("Status: APROVADO.")
else:
    print("Status: REPROVADO.")