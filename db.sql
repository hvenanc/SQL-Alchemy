CREATE DATABASE IF NOT EXISTS onibus;

USE onibus;

CREATE TABLE IF NOT EXISTS linhas (
    codigo INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    tarifa DECIMAL(4,2) NOT NULL,
    ar_condicionado VARCHAR(3) NOT NULL,
    integracao VARCHAR(3) NOT NULL,
    PRIMARY KEY(codigo)
);

INSERT INTO linhas (codigo, nome, tarifa,ar_condicionado,integracao)
VALUE (132,"UR-2(IBURA)/T.I TANCREDO NEVES",4.10,"NAO","SIM");