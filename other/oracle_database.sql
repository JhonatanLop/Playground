CREATE DATABASE CASO_VENDAS;

CREATE TABLE CLIENTE(
    cli_id number constraint CLT_ID_PK primary key,
    cli_nome varchar(30),
    cli_cpf number,
    cli_ativo number
);

CREATE TABLE PEDIDO(
    id number constraint PED_ID_PK primary key,
    data date,
    valor_total number(8,2),
    cli_id number constraint CLI_PEDIDO_FK REFERENCES CLIENTE(cli_id)
);

CREATE TABLE PRODUTO(
    pdt_id number constraint ID_PRODUTO_PK primary KEY,
    pdt_descricao varchar,
    pdt_valor number
)

CREATE TABLE ITEM_PEDIDO(
    ped_id number constraint ITEM_PEDIDO_FK_PEDIDO REFERENCES PEDIDO(ped_id),
    pdt_id number constraint ITEM_PEDIDO_FK_CLIENTE REFERENCES CLIENTE(pdt_id),

)