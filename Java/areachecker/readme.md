# Atividade Avaliativa Final
> jhonatan Oliveira Lopes

## exercício AreaChecker

Um professor de uma faculdade precisa desenvolver um aplicativo para conferência de cálculos simples. Para isso ele convocou um aluno da disciplina de LP II para desenvolver uma solução que possibilite ao mesmo efetuar algumas conferências, a citar:

Conferência do cálculo da área das seguintes figuras geométricas:

    Quadrado
    Retângulo
    Círculo
    Triângulo
    Paralelograma
    Trapézio
    Hexágono
    Losango
    Cubo


Tudo isso através de um ponto único.

O mesmo resolveu nomear este projeto de AreaChecker.

Precisamos ajudá-lo a desenvolver essa solução e para isso usaremos uma IDE de sua preferência e a plataforma Java.

Mãos à obra!


Obsevação:

Todas classes que representam os objetos deverão implementar a interface abaixo.

```java
public interface Calculable {
      double calcularArea();
}
```

A instanciação das diversas abstrações que concentrarão os cálculos específicos deverá ser feita através de uma implementação do pattern Abstract Factory (https://refactoring.guru/design-patterns/abstract-factory). Este será o ponto de partida!

O professor também precisa de uma classe de teste (usando ou não uma ferramenta/framework específico) com no mínimo um cenário de teste para cada cálculo de área implementada.

Foco da Atividade

    - Convencionamento de Código
    - Estruturação das Classes da Aplicação
    - Estruturação e Organização em Pacotes
    - Polimorfismo

## Como executar:

1. baixe o arquivo na pasta ```project/areachecker.zip```
2. entre na pasta raiz do projeto
3. execute os comando em sequência:
    1. ```mvn clean install``` - para instalar as dependências
    2. ```mvn exec:java``` - para executar o projeto
    3. ```mvn test``` - para executar a rotina de testes