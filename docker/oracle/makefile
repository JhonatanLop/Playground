# Makefile for Oracle Database Docker

# Nome do contêiner
CONTAINER_NAME = oracle_database

# Nome do volume
VOLUME_NAME = vl_oracle

# Imagem do Oracle Database e versão
ORACLE_IMAGE = my_oracle_image

.PHONY: build run stop clean

# Comando para construir a imagem do Oracle Database
build:
    docker build -t $(ORACLE_IMAGE) .

# Comando para executar o contêiner do Oracle Database
run:
    # Criação do volume para persistência dos dados
    docker volume create $(VOLUME_NAME)
    # Execução do contêiner com as configurações necessárias
    docker run -d -p 1521:1521 -p 5500:5500 \
        --name $(CONTAINER_NAME) \
        -v $(VOLUME_NAME):/opt/oracle/data \
        -e ORACLE_SID=mysid \
        -e 'ORACLE_PDB'=oracle \
        -e ORACLE_PWD=oracle \
        $(ORACLE_IMAGE)

# Comando para parar o contêiner do Oracle Database
stop:
    docker stop $(CONTAINER_NAME)

# Comando para limpar o ambiente removendo o contêiner e o volume
clean: stop
    docker rm $(CONTAINER_NAME)
    docker volume rm $(VOLUME_NAME)
