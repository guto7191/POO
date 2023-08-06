class Repositorio:

    def select(self, db_connection: any):
        conection = db_connection.conectar()
        print(f"Conectei ao banco {conection}")
        print("Fazendo um select * FROM")
        db_connection.desconectar()
    

    def insert(self, db_connection: any):
        conection = db_connection.conectar()
        print(f"Conectei ao banco {conection}")
        print("Fazendo um insert values")
        db_connection.desconectar()
