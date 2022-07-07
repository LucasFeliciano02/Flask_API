import sqlite3


empregados = [
    {'nome': 'Lucas', 'cargo': 'Engenheiro', 'salario': '4000'},
    {'nome': 'Marcos', 'cargo': 'Analista', 'salario': '4000'},
    {'nome': 'Maria', 'cargo': 'Desenvolvedor', 'salario': '4000'},
]


conn = sqlite3.connect('enterprise.db')

cursor = conn.cursor()

for empregado in empregados:
    cursor.execute("""
                   INSERT INTO empregados (nome, cargo, salario)
                   VALUES (?, ?, ?)
                   """, (empregado['nome'], empregado['cargo'], empregado['salario']))


print('Dados inseridos com sucesso!')

# inserção de dados, requere o commit
conn.commit()

conn.close()
