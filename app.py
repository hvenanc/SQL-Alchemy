from infra.repository.linha_repository import LinhaRepository

linha = LinhaRepository()

# dados = [{"codigo":101,"nome":"CIRCULAR (CONDE DA BOA VISTA / RUA DO SOL)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":102,"nome":"TI SANTA LUZIA / IBURA","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":104,"nome":"CIRCULAR (IMIP)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":106,"nome":"TI SANTA LUZIA / PARQUE AERONÁUTICA","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":107,"nome":"CIRCULAR (CABUGÁ / PREFEITURA)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":108,"nome":"BARRO / CEASA","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":115,"nome":"TI AEROPORTO / TI AFOGADOS","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":116,"nome":"CIRCULAR (PRÍNCIPE)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":117,"nome":"CIRCULAR (PREFEITURA / CABUGÁ)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":128,"nome":"UR-03 / BARRO (MILAGRES)","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":138,"nome":"ZUMBI DO PACHECO / TI TANCREDO NEVES","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":144,"nome":"UR-04 / TI TANCREDO NEVES","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":149,"nome":"TI CAVALEIRO / ZUMBI DO PACHECO","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"},{"codigo":200,"nome":"JABOATÃO (PARADOR)","tarifa":"4.10","ar-condicionado":"sim","integracao":"sim"},{"codigo":203,"nome":"ZUMBI DO PACHECO / BARRO (LOTEAMENTO)","tarifa":"4.10","ar-condicionado":"nao","integracao":"sim"}]
# for x in dados :

#     linha.insert(x['codigo'],x['nome'],x['tarifa'],x['ar-condicionado'],x['integracao'])
#linha.update(202,'T.I Barro/T.I Macaxeira(VARZEA)',4.10,'nao','sim')
response = linha.select()
print(response)