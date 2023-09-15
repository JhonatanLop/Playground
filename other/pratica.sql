
create database fatec;
create SCHEMA aula1;
CREATE USER aluno WITH PASSWORD 'fatec';
grant all PRIVILEGES on fatec to aluno;

create table departamento(
    cod_departamento serial PRIMARY KEY cod_departamento_pk,
    dp_nome varchar(255),
    dp_data_inicial date
);

create table localizacao(
    lc_cod_depart int,
    "local" int,
    PRIMARY KEY(lc_cod_depart,"local") localizacao_cod_lcl_pk
);

create table projeto(
    cod_funk
)