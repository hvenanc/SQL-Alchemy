from infra.repository.linha_repository import LinhaRepository

linha = LinhaRepository()

#linha.insert(132,'ur-2 <Ibura>/t.i tancredo neves',4.10,'NAO','SIM')
linha.update(202,'T.I Barro/T.I Macaxeira(VARZEA)',4.10,'nao','sim')
response = linha.select()
print(response)