# FOREVIS

FOREVIS (Foreign Exchange Visualization)

Desenvolvido como projeto da disciplina INE5404, o FOREVIS é uma suíte para visualização de métricas de ativos financeiros variados, o nome faz alusão ao título do álbum do Raimundos, [Só no Forevis](https://en.wikipedia.org/wiki/S%C3%B3_no_For%C3%A9vis).

![Only in the ass](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ9sgtrDI-17LsLqaYCOgVrqiwOpTtwUjcbSxojLZs5GK8Bgdog)

Novas funcionalidades serão implementadas conforme a evolução do projeto, dê um watch nesse repositório caso queira ficar sabendo :D

## Executando o projeto

A estrutura do projeto usa o [Poetry](https://github.com/sdispater/poetry) como gerenciador de dependências, para instalar os pacotes necessários você só precisa instalar o Poetry e rodar `poetry install`. Caso não queira ou não consiga instalar o Poetry, instale os seguintes pacotes:

- matplotlib = "^3.1"
- pandas = "^0.25.3"
- numpy = "^1.17"
- mpl_finance = "^0.10.0"

Depois de ter as dependências instaladas, crie um arquivo o arquivo config/env.py e adicione sua chave de API nele, você pode conseguir uma chave na site da [alphavantage.co](https://www.alphavantage.co/).

```python
API_KEY = "SUA_CHAVE_AQUI";
```

Por enquanto o projeto tem que ser executado direto pelo entry point usando o Python, no futuro ele será distribuido como uma aplicação CLI. Para fazer uma consulta básica (métricas do Bitcoin levando em consideração preços em dólar americano) execute `python __init__.py`.

Podem também ser passados 3 parâmetros na consulta:

- `-from BTC`: criptomoeda de origem, sempre pesquisada por sua sigla no lugar de "BTC"
- `-to USD`: moeda de destino, sempre pesquisada por sua sigla no lugar de "USD"
- `-days 1000`: quantos dias serão plotados no gráfico, por exemplo, ao passar `-days 10` serão buscados apenas os 10 últimos dias de negociações

#### Autores

- Djalma [@djsouls](https://github.com/Djsouls)
- JVM [@leviosar](https://github.com/leviosar)