``` 
create table medico (
  med_codigo number primary key,
  med_nome varchar(30),
  med_salario number(10,2));

```
``` 
insert into medico(med_codigo, med_nome, med_salario) values(1,'JOÃO',20000);
```
``` status
1 rows affected
```
``` 
insert into medico(med_codigo, med_nome, med_salario) values(2,'GABRIEL',50000);
```
``` status
1 rows affected
```
``` 
insert into medico(med_codigo, med_nome, med_salario) values(3,'JOSÉ',60000)
```
``` status
1 rows affected
```
``` 
create view vw_medico as select
  medico.med_codigo,
  medico.med_nome,
  medico.med_salario
from medico;

```
``` 
select * from vw_medico;
```
| MED\_CODIGO | MED\_NOME | MED\_SALARIO |
| ----------:|:--------|-----------:|
| 1 | JOÃO | 20000 |
| 2 | GABRIEL | 50000 |
| 3 | JOSÉ | 60000 |

``` 
create or replace view medico_view (CÓDIGO, MEDICO)
AS SELECT medico.med_codigo, medico.med_nome from medico;
```
``` 
select * from medico_view;
```
| CÓDIGO | MEDICO |
| ------:|:------|
| 1 | JOÃO |
| 2 | GABRIEL |
| 3 | JOSÉ |

``` 
insert into medico_view values(4,'MARIA');
```
``` status
1 rows affected
```
``` 
select * from medico_view;
```
| CÓDIGO | MEDICO |
| ------:|:------|
| 1 | JOÃO |
| 2 | GABRIEL |
| 3 | JOSÉ |
| 4 | MARIA |

``` 
select * from medico;
```
| MED\_CODIGO | MED\_NOME | MED\_SALARIO |
| ----------:|:--------|-----------:|
| 1 | JOÃO | 20000 |
| 2 | GABRIEL | 50000 |
| 3 | JOSÉ | 60000 |
| 4 | MARIA | *null* |

``` 
create sequence dep_id_sql
increment by 10
start with 120
maxvalue 9999;
```
``` 
create table departamento(
  dep_cod number primary key,
  dep_nome varchar(30));
```
``` 
insert into departamento(dep_cod,dep_nome)values(dep_id_sql.nextval,'Vendas');
```
``` status
1 rows affected
```
``` 
insert into departamento(dep_cod,dep_nome)values(dep_id_sql.nextval,'RH');
```
``` status
1 rows affected
```
``` 
select * from departamento;
```
| DEP\_COD | DEP\_NOME |
| -------:|:--------|
| 120 | Vendas |
| 130 | RH |

``` 
alter sequence dep_id_seq restart with 1;
```
``` error
ORA-00933: SQL command not properly ended
```
[fiddle](https://dbfiddle.uk/2HTWeKq7)
