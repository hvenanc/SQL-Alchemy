from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, Integer, DECIMAL
from sqlalchemy.orm import sessionmaker

#Conexão
engine = create_engine("mysql+pymysql://root:root@localhost:3306/onibus")
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

#Base

class Linha(Base):

    __tablename__ = 'linhas'

    codigo = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False)
    tarifa = Column(DECIMAL(4,2), nullable = False)
    ar_condicionado = Column(String, nullable = False)
    integracao = Column(String, nullable = False)

    def __repr__(self):
        return f'{self.codigo}/{self.nome}' 

#Insert

linha = Linha(codigo = 4137,nome='UR-11/CAIS DE SANTA RITA',tarifa=4.10, ar_condicionado='NAO',integracao='NAO')
session.add(linha)
session.commit()

#Delete 

session.query(Linha).filter(Linha.codigo == 4137).delete()
session.commit()

# #Update

session.query(Linha).filter(Linha.codigo == 132).update({'tarifa' : 3.75})
session.commit()

#Select

data = session.query(Linha).all()
print(data)

#Fechar conexão

session.close()