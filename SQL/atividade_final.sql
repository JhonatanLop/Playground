-- 1
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

insert into Estado (est_cod, est_estado) values (1, 'São Paulo');
insert into Estado (est_cod, est_estado) values (2, 'Rio de Janeiro');
insert into Estado (est_cod, est_estado) values (3, 'Minas Gerais');
insert into Estado (est_cod, est_estado) values (4, 'Bahia');
insert into Estado (est_cod, est_estado) values (5, 'Paraná');

insert into Cargo (car_cod, car_descricao) values (1,'Gerente');
insert into Cargo (car_cod, car_descricao) values (2,'Analista');
insert into Cargo (car_cod, car_descricao) values (3,'Assistente');
insert into Cargo (car_cod, car_descricao) values (4,'Estagiário');
insert into Cargo (car_cod, car_descricao) values (5,'Coordenador');

insert into Cidade (cid_cod, est_cod, cid_nome) values (1, 1, 'São Paulo');
insert into Cidade (cid_cod, est_cod, cid_nome) values (2, 2, 'Rio de Janeiro');
insert into Cidade (cid_cod, est_cod, cid_nome) values (3, 3, 'Belo Horizonte');
insert into Cidade (cid_cod, est_cod, cid_nome) values (4, 4, 'Salvador');
insert into Cidade (cid_cod, est_cod, cid_nome) values (5, 5, 'Curitiba');

insert into Departamento (dep_cod,dep_descricao) values (1,'Vendas');
insert into Departamento (dep_cod,dep_descricao) values (2,'RH');
insert into Departamento (dep_cod,dep_descricao) values (3,'Marketing');
insert into Departamento (dep_cod,dep_descricao) values (4,'TI');
insert into Departamento (dep_cod,dep_descricao) values (5,'Logisticca');

insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (1, 'Rua A', 'João', 5000.00, 1, 1234, 100, 1, 1, 1);
insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (2, 'Rua B', 'Maria', 4000.00, 2, 5678, 200, 2, 2, 2);
insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (3, 'Rua C', 'Pedro', 3500.00, 3, 9012, 300, 3, 3, 3);
insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (4, 'Rua D', 'Ana', 3000.00, 4, 3456, 400, 4, 4, 4);
insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (5, 'Rua E', 'Carlos', 2500.00, 5, 7890, 500, 5, 5, 5);

-- 2
create or replace view Funcionario_View as select
    f.fun_cod,
    f.fun_nome,
    f.fun_Logradouro,
    cid.cid_nome,
    e.est_estado,
    car.car_descricao,
    d.dep_descricao
    from Funcionario f, Cidade cid, Estado e, Cargo car, Departamento d
    where
    f.cid_cod = cid.cid_cod and
    f.car_cod = car.car_cod and
    f.est_cod = e.est_cod and
    f.dep_cod = d.dep_cod
    with read only;

-- 3
select * from Funcionario_View;

-- 4
select * from Funcionario;

-- 5
insert into Funcionario (fun_cod, fun_Logradouro, fun_nome, fun_salario, car_cod, fun_cep, fun_nro, cid_cod, est_cod, dep_cod) values (6, 'Rua D', 'Jhow', 10000.00, 4, 1725, 2627, 1, 1, 4);
select * from Funcionario_View where fun_nome = 'Jhow';

-- 6
alter table Funcionario add fun_obs varchar(255);
create or replace view Funcionario_View as select
    f.fun_cod,
    f.fun_nome,
    f.fun_Logradouro,
    f.fun_obs,
    cid.cid_nome,
    e.est_estado,
    car.car_descricao,
    d.dep_descricao
    from Funcionario f, Cidade cid, Estado e, Cargo car, Departamento d
    where
    f.cid_cod = cid.cid_cod and
    f.car_cod = car.car_cod and
    f.est_cod = e.est_cod and
    f.dep_cod = d.dep_cod
    with read only;

-- 7
select text from all_views where view_name = 'FUNCIONARIO_VIEW';

-- 8

--A respeito de uma view criada no Oracle, marque com X a (s) resposta(s) correta(s):
--( ) A. Por meio de uma view os dados apenas podem ser vistos. -- NÃO POIS É POSSÍVEL INSERIR/ALTERAR DADOS ATRAVÉZ DE UMA VIEW SE DECLARADA CORRETAMENTE
--( ) B. Tabela virtual na qual os dados estão fisicamente armazenados. -- NÃO, OS DADOS SÃO ARMAZENADOS NA TABELA, A VIEW É APENAS UMA REPRESETAÇÃO LÓGICA
--(X) C. Utilizada para evitar que usuários não autorizados tenham acesso a todos os dados de uma tabela.
--( ) D. Para remover uma view utilizamos o seguinte comando delete view <nome da view>. -- USA-SE "DROP VIEW <nome da view>;"