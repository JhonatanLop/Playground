-- Revisa ai depois:
-- 1. Quais as gravadoras que não possuem CDs cadastrados com preço inferior a 80,00?
SELECT grav_nome
FROM gravadora
WHERE grav_codigo in (
        SELECT grav_codigo
        FROM CD
        WHERE cd_preco_venda > 80
    )

-- 2. Quais os CDs que têm o preço igual ao maior preço de cada gravadora?
SELECT MAX(cd_preco_venda),
    grav_codigo
FROM CD
GROUP BY grav_codigo -- 3. Quais os CDs que têm preço inferior a qualquer outro CD da gravadora com código 10?
SELECT cd_nome
FROM CD
WHERE cd_preco_venda < ANY (
        SELECT cd_preco_venda
        FROM CD
        WHERE grav_codigo = 10
    );

-- 4. Quais CDs têm o preço de venda menor que a média de preço de venda de todas as gravadoras?
select cd_nome,
    cd_preco_venda
from cd
where cd_preco_venda < (
        select Avg(cd_preco_venda)
        from cd
    );

-- 5. Liste os nomes dos CDs que tenham preço de venda maior que 10,00 reais ou a gravadora seja a de código 3, ordenados por ordem alfabética decrescente dos nomes dos CDs. Exibir os nomes dos CDs em iniciando com a letra maiúscula.
select INITCAP(cd_nome)
from cd
where cd_preco_venda > 10
    or grav_codigo = 3;
    ORDER BY cd_nome desc

-- 6. Exibir o nome, a data de lançamento e nome da gravadora dos CDs que possuem data de lançamento em um intervalo de datas.
select cd.cd_nome,
    cd.cd_data_lancamento,
    gv.grav_nome
from cd
    join gravadora gv on cd.grav_codigo = gv.grav_codigo
where cd_data_lancamento between '12-NOV-23' and '14-NOV-23';

-- 7. Exibir o nome do Cd e de suas gravadoras, exiba também os CD´S que não possuam gravadoras
SELECT C.cd_nome,
    G.grav_nome
FROM CD C
    LEFT JOIN GRAVADORA G ON G.grav_codigo = C.grav_codigo

-- 8. Listar quantas músicas que há em cada CD. (Exibir código do CD e a quantidade de música).
SELECT cd_codigo,
    COUNT(mus_codigo) Quantidade
FROM FAIXA
GROUP BY cd_codigo

-- 9. Definir a qual categoria (cat_codigo) cada Cd pertence
SELECT cd.cd_codigo,
    cd.cd_nome,
    cd.cd_preco_venda,
    CASE
        WHEN cd.cd_preco_venda BETWEEN 5 AND 10 THEN 1
        WHEN cd.cd_preco_venda BETWEEN 11 AND 20 THEN 2
        WHEN cd.cd_preco_venda BETWEEN 21 AND 30 THEN 3
        WHEN cd.cd_preco_venda BETWEEN 31 AND 40 THEN 4
        WHEN cd.cd_preco_venda BETWEEN 41 AND 50 THEN 6
        WHEN cd.cd_preco_venda BETWEEN 51 AND 60 THEN 7
        WHEN cd.cd_preco_venda BETWEEN 61 AND 70 THEN 8
        ELSE NULL
    END AS cat_codigo
FROM CD cd;

-- 10. Listar o nome do CD indicado para cada CD gravado
SELECT c1.cd_nome,
    c2.cd_nome
FROM CD c1
    LEFT JOIN CD c2 ON c1.cd_indicado = c2.cd_codigo;

-- 11. A tabela CD_CATEGORIA possui 3 categorias cadastradas, conforme mostra a figura abaixo.
CAT_CODIGO MENOR_PRECO MAIOR_PRECO 1 5 10 2 11 20 3 21 30 4 31 40 5 31 40 6 41 50 7 52 60 8 61 70

-- 12. Liste o código, nome, preço de venda, o tempo de duração total, o nome da gravadora do CD de código 101.
SELECT c.cd_codigo,
    c.cd_nome,
    c.cd_preco_venda,
    SUM(m.mus_duracao) AS duracao_total,
    g.grav_nome
FROM CD c
    JOIN FAIXA f ON c.cd_codigo = f.cd_codigo
    JOIN MUSICA m ON f.mus_codigo = m.mus_codigo
    JOIN GRAVADORA g ON c.grav_codigo = g.grav_codigo
WHERE c.cd_codigo = 101
GROUP BY c.cd_codigo,
    c.cd_nome,
    c.cd_preco_venda,
    g.grav_nome;

-- 13. Listar o nome das gravadoras que possuem mais de 2 Cds relacionados a ela.
SELECT grav_nome
FROM GRAVADORA G
WHERE (
        SELECT COUNT(*)
        FROM CD C
        WHERE C.grav_codigo = G.grav_codigo
    ) > 2;

-- 14.Listar o nome da música de maior duração.
SELECT mus_nome
FROM MUSICA
WHERE mus_duracao = (
        SELECT MAX(mus_duracao)
        FROM MUSICA
    );


-- 15.Listar o nome das músicas, a faixa e o nome do CD em que está a música, apenas os Cds de código 102 e 103.
SELECT m.mus_nome,
    f.faixa_numero,
    c.cd_nome
FROM MUSICA m
    JOIN FAIXA f ON m.mus_codigo = f.mus_codigo
    JOIN CD c ON f.cd_codigo = c.cd_codigo
WHERE c.cd_codigo IN (102, 103);

-- 16.Listar (um único resultado) os autores (código autor, nome autor) com código menor que 10 e as músicas (código música, nome musica) com código menor que 15.(Utilizarem
SELECT aut_codigo,
    aut_nome
FROM AUTOR
WHERE aut_codigo < 10
UNION
SELECT mus_codigo,
    mus_nome
FROM MUSICA
WHERE mus_codigo < 15;