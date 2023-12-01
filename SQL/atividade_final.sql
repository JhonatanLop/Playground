create table Estado(
    est_cod number primary key,
    est_estado varchar(30)
);

create table Cidade(
    cid_cod number primary key,
    est_cod number(4),
    cid_nome varchar(30),
    constraint fk_est_cod FOREIGN KEY (est_cod) references Estado (est_cod)
);

create table Cargo(
    car_cod number primary key,
    car_descricao varchar(20)
);

create table Departamento(
    dep_cod number primary key,
    dep_descricao varchar(20)
);

create table Funcionario(
    fun_cod number primary key,
    fun_Logradouro varchar (20),
    fun_nome varchar(30),
    fun_salario number(8,2),
    car_cod number(4),
    fun_cep number(4),
    fun_nro number(4),
    cid_cod number(4),
    est_cod number(4),
    dep_cod number(4),
    CONSTRAINT fk_car_cod FOREIGN KEY (car_cod) references Cargo(car_cod),
    CONSTRAINT fk_cid_cod FOREIGN KEY (cid_cod) references Cidade(cid_cod),
    CONSTRAINT fk_est_cod_fun FOREIGN KEY (est_cod) references Estado(est_cod),
    CONSTRAINT fk_dep_cod FOREIGN KEY (dep_cod) references Departamento(dep_cod)
);

create or replace view Funcionario_View as select
    f.fun_cod,
    f.fun_nome,
    f.fun_Logradouro,
    cid.cid_nome,
    e.est_estado,
    car.car_descricao,
    d.dep_descricao
    from Funcionario f