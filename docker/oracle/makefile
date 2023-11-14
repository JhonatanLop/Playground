# Makefile for Oracle Database Docker

# Nome do contêiner
CONTAINER_NAME = oracle_database

# Nome do volume
VOLUME_NAME = vl_oracle

# Imagem do Oracle Database e versão
ORACLE_IMAGE = oraclelinux:9

.PHONY: build run stop clean

build:
    docker build -t my_first_img_docker .

run:
    docker volume create $(VOLUME_NAME)
    docker run -d -p 1521:1521 -p 5500:5500 \
      --name $(CONTAINER_NAME) \
      -v $(VOLUME_NAME):/opt/oracle/oradata \
      $(ORACLE_IMAGE)

stop:
    docker stop $(CONTAINER_NAME)

clean: stop
    docker rm $(CONTAINER_NAME)
    docker volume rm $(VOLUME_NAME)
