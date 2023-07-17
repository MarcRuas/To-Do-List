import sqlite3 as sql

class dados:
    def __init__(self):
        self.db = sql.Connection("to_do.db")
        self.cursor = self.db.cursor()
        self.create_Table()

    def create_Table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Tarefa (id INTEGER PRIMARY KEY, elementos text)")

    def create(self, itens):
        self.cursor.execute("SELECT elementos FROM Tarefa WHERE elementos = ?", (itens,))
        resultado = self.cursor.fetchall()
        if resultado:
            print("Já existe essa tarefa")
        else:
            self.cursor.execute("INSERT INTO Tarefa (elementos) VALUES (?)", (itens,))
            self.db.commit()
            print("Tarefa adicionada com sucesso")

    def read(self):
        lista = []
        self.cursor.execute("SELECT * FROM Tarefa")
        resultado = self.cursor.fetchall()
        for r in resultado:
            lista.append(r)
        print(lista)
        return lista

    def update(self, itens):
        atualizar = "UPDATE Tarefa SET elementos = ? WHERE id = ?"
        self.cursor.execute(atualizar, itens)
        self.db.commit()

    def delete(self, itens):
        self.cursor.execute("DELETE FROM Tarefa WHERE id = ?", (itens,))
        self.db.commit()


