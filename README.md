# Teste Técnico Desenvolvedor(a) Python

Enunciado do teste técnico para a vaga de Desenvolvedor(a) Python.

## O problema

A equipe de desenvolvimento sinalizou que muitos projetos estão com versões de libs desatualizadas,
e para verificar todos os projetos levaria bastante tempo. Os desenvolvedores tiveram uma ideia, 
"que tal ler o arquivo requiments.txt e utilizar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html)"

## Solução

Você deve desenvolver um programa que leia o arquivo requirements.txt
listando todas as libs/versões validando pela api pública do PyPI.

A saída deverá estar no formato JSON seguinte:

```
[{
    "packageName": "Nome do pacote",
    "currentVersion": "Versão atual do pacote",
    "latestVersion": "Última versão do pacote",
    "outOfDate: true or false
}]
```

| ⚠️ | O Arquivo requirements.txt esta no root desse projeto. |
| --- | --- |

| ⚠️ | Sua solução deve usar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html). |
| --- | --- |

## Solução Definida

Decidi utilizar a data de upload das versões para definir uma ordenação entre elas. Dessa forma, posso encontrar a versão mais recente. Isso presume confiança nas informações de `upload_time` do PyPi. Além disso, decidi ignorar versões que não dispunham dessa informação.

Uma outra abordagem, que poderia tomar caso possuísse mais tempo, seria criar uma classe Parser para conseguir comparar duas versões diferentes a partir dos seus nomes. A complexidade dessa solução está no fato de que algumas versões não possuem três números (e.g. `1.21`, em comparação com `1.21.3`) e algumas versões possuem letras (e.g. `1.12b`). Dessa forma, uma simples comparação entre números em relação à posição não atenderia a todos os casos.

## Como executar

Para executar os testes, executar os seguintes comandos:

`docker-compose build test`
`docker-compose run test`

Para executar a aplicação, executar os seguintes comandos:

`docker-compose build app`
`docker-compose run app`
