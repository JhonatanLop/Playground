-- 1)
-- Liste os CDs que possuem a data de lançamento maior que 01/06/2014 e o preço de venda maior que 30.50 ordenados pelo nome.
-- Exiba: (cd_nome,cd_preco_venda,cd_data_lançamento).

select cd_nome,cd_preco_venda,cd_data_lancamento from CD where cd_data_lancamento > '01/06/2014' and cd_preco_venda > 30.50 order by cd_nome;

-- 2)
-- Liste todas as gravadoras e os seus CDS, liste até mesmo as que não possuem CDs relacionados. Exiba: (grav_nome,cd_nome).
-- Resolva utilizando a Sintaxe Ansi e a da Oracle.

select CD.cd_nome, GRAVADORA.grav_nome from CD
left join GRAVADORA on CD.grav_codigo = GRAVADORA.grav_codigo;

-- 3)
-- Exibir a quantidade de músicas que cada autor possui. Exiba:Aut_Nome,Quantidade.

select autor.aut_nome, count(autor_musica.aut_codigo) as Quantidade from AUTOR
	 join autor_musica on autor.aut_codigo = autor_musica.aut_codigo
     GROUP by 1;

-- 4)
-- Exiba o nome do CD mais caro.

select cd_nome from CD where cd_preco_venda = (select max(cd_preco_venda) from CD);

-- 5)
-- Listar o nome do autor responsável pela música Pais e Filhos.

select aut_nome from AUTOR
    join autor_musica on autor.aut_codigo = autor_musica.aut_codigo
    join musica on autor_musica.mus_codigo = musica.mus_codigo
    where mus_nome = 'Pais e Filhos';

-- 6)
-- Exiba a duração correspondente ao código do CD de código 1.
select mus_duracao from cd
    join faixa on cd.cd_codigo = faixa.cd_codigo
    join musica on faixa.mus_codigo = musica.mus_codigo
    WHERE cd.cd_codigo = 1;

-- 7)
-- Crie as tabelas, usando DDL, do modelo lógico a seguir:

CREATE table if not exists Partido(
    idPartido serial primary key,
    siglaPartido VARCHAR(4),
    descricaoPartido varchar(30)
);

CREATE table if not exists Deputado(
    idDeputado serial primary KEY,
    idPartido int,
    nomeDeputado varchar(30),
    FOREIGN key (idPartido) references Partido(idPartido)
)

CREATE table if not exists Sessao(
    idSessao serial primary key,
    dataSessao date,
    horaSessao time,
    decisao varchar(4)
);

CREATE table if not exists Participacao(
    idSessao int,
    idDeputado int,
    primary key(idSessao,idDeputado),
    FOREIGN key (idSessao) references Sessao(idSessao),
    FOREIGN key (idDeputado) references Deputado(idDeputado)
);