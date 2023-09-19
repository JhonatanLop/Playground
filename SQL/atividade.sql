create database atividade;
create schema bd;

create user aluno with password 'Fatec';
grant select on database atividade to aluno;

create table if not exists bd.DEPARTAMENTO(
    dpt_id int,
    dpt_nome varchar(255),
    dpt_data_init DATE,
    CONSTRAINT dpt_id_pk PRIMARY KEY (dpt_id)
);

CREATE TABLE IF NOT EXISTS bd.LOCALIZACAO(
    lcz_departamento int,
    "LOCAL" varchar(255),
    CONSTRAINT lcz_pk PRIMARY KEY (lcz_departamento, "LOCAL"),
    CONSTRAINT lcz_dpt_fk FOREIGN KEY (lcz_departamento) REFERENCES bd.DEPARTAMENTO(dpt_id)
);

create table if not exists bd.PROJETO(
    prj_id int,
    prj_dpt_fk int,
    prj_titulo varchar(255),
    prj_descical varchar(255),
    prj_data date,
    CONSTRAINT prj_id_pk PRIMARY KEY (prj_id),
    CONSTRAINT prj_dpt_fk FOREIGN KEY (prj_dpt_fk) REFERENCES bd.DEPARTAMENTO(dpt_id)
);

create table if not exists bd.DEPENDENTE(
    dpd_id int,
    dpd_func_fk int,
    dpd_nome varchar(100),
    dpd_parentesco varchar(30),
    dpd_data_nasc date,
    CONSTRAINT dpd_id_pk PRIMARY KEY (dpd_id)
);

create table if not exists bd.FUNCIONARIO(
    func_id int,
    func_nome varchar(255),
    func_cpf varchar(255),
    func_salario numeric,
    func_endereco varchar(255),
    func_sexo char(1),
    func_dpd_fk int,
    func_dpt_fk int,
    CONSTRAINT func_id_pk PRIMARY KEY (func_id),
    CONSTRAINT func_dpd_fk FOREIGN KEY (func_dpd_fk) REFERENCES bd.DEPENDENTE(dpd_id),
    CONSTRAINT func_dpt_fk FOREIGN KEY (func_dpt_fk) REFERENCES bd.DEPARTAMENTO(dpt_id)
);

alter table bd.dependente add
    CONSTRAINT dpd_func_fk FOREIGN KEY (dpd_func_fk) REFERENCES bd.FUNCIONARIO(func_id);


create table if not exists bd.PARTICIPA(
    ptc_prj_fk int,
    ptc_func_fk int,
    ptc_horas time,
    CONSTRAINT ptc_pk PRIMARY KEY (ptc_prj_fk),
    CONSTRAINT ptc_func_fk FOREIGN KEY (ptc_prj_fk) REFERENCES bd.FUNCIONARIO(func_id),
    CONSTRAINT ptc_prj_fk FOREIGN KEY (ptc_func_fk) REFERENCES bd.PROJETO(prj_id)
);