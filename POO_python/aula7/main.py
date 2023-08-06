from repositorio import Repositorio
from database import ProstgresDB, MysqlDB

db_con_ProstgresDb = ProstgresDB()
db_con_MsqlsDB = MysqlDB()
repo = Repositorio()

repo.insert(db_con_ProstgresDb)
repo.insert(db_con_MsqlsDB)

repo.select(db_con_ProstgresDb)
repo.select(db_con_MsqlsDB)