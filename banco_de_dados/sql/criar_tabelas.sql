CREATE TABLE demonstracoes_contabeis (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil BIGINT,
    descricao TEXT,
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);

CREATE TABLE operadoras_ativas (
    registro_ans INTEGER,
    cnpj VARCHAR(14),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero VARCHAR(20),
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep CHAR(8),
    ddd CHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao INTEGER,
    data_registro_ans DATE
);
