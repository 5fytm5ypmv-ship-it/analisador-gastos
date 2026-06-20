import csv
from datetime import datetime

# Dados de exemplo (simula uma planilha de gastos)
gastos = [
    {"data": "2026-06-01", "categoria": "Alimentação", "descricao": "Mercado",     "valor": 320.50},
    {"data": "2026-06-03", "categoria": "Transporte",  "descricao": "Combustível", "valor": 180.00},
    {"data": "2026-06-05", "categoria": "Alimentação", "descricao": "Restaurante", "valor": 65.00},
    {"data": "2026-06-10", "categoria": "Saúde",       "descricao": "Farmácia",    "valor": 95.30},
    {"data": "2026-06-12", "categoria": "Lazer",       "descricao": "Cinema",      "valor": 45.00},
    {"data": "2026-06-15", "categoria": "Alimentação", "descricao": "Padaria",     "valor": 28.00},
    {"data": "2026-06-18", "categoria": "Transporte",  "descricao": "Uber",        "valor": 32.00},
    {"data": "2026-06-20", "categoria": "Saúde",       "descricao": "Academia",    "valor": 99.00},
]

print("=" * 40)
print("   ANALISADOR DE GASTOS PESSOAIS")
print("=" * 40)

# Total geral
total = sum(g["valor"] for g in gastos)
print(f"\nTotal do mês: R$ {total:.2f}")

# Total por categoria
print("\nGastos por categoria:")
categorias = {}
for g in gastos:
    cat = g["categoria"]
    categorias[cat] = categorias.get(cat, 0) + g["valor"]

for cat, valor in sorted(categorias.items(), key=lambda x: x[1], reverse=True):
    percentual = (valor / total) * 100
    print(f"  {cat:<15} R$ {valor:>7.2f}  ({percentual:.1f}%)")

# Maior gasto
maior = max(gastos, key=lambda x: x["valor"])
print(f"\nMaior gasto: {maior['descricao']} — R$ {maior['valor']:.2f}")

print("\n" + "=" * 40)