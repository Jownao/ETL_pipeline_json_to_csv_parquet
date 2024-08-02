# ETL_pipeline_json_to_csv_parquet

## Descrição

Este projeto tem como objetivo criar um pipeline ETL (Extract, Transform, Load) que lê arquivos JSON, realiza um cálculo de total e carrega os dados transformados em arquivos CSV ou Parquet, ou em ambos os formatos. O pipeline foi projetado para ser facilmente adaptável e escalável para diferentes fontes de dados e formatos de saída.

## Estrutura do Projeto

```
ETL_pipeline_json_to_csv_parquet
├── data
│   ├── coleta_dia01.json
│   ├── coleta_dia02.json
│   ├── coleta_dia03.json
├── .gitignore
├── README.md
├── __init__.py
├── etl.py
└── pipeline.py
```

## Arquivos

- **data/**: Contém os arquivos JSON de entrada.
  - `coleta_dia01.json`
  - `coleta_dia02.json`
  - `coleta_dia03.json`

- **.gitignore**: Arquivo que lista os arquivos e diretórios a serem ignorados pelo Git.

- **README.md**: Arquivo de documentação que você está lendo agora.

- **__init__.py**: Arquivo que indica ao Python que o diretório deve ser tratado como um pacote.

- **etl.py**: Contém as funções principais para o processo de ETL, incluindo a leitura de arquivos JSON, transformação dos dados e gravação dos resultados em CSV e Parquet.

- **pipeline.py**: Script que executa o pipeline ETL utilizando as funções definidas em `etl.py`.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o pipeline:

- `pandas`
- `pyarrow`
- `fastparquet`

Você pode instalá-las utilizando o comando:

```bash
pip install pandas pyarrow fastparquet
```

## Uso

1. **Preparação dos Dados**: Coloque seus arquivos JSON na pasta `data/`.

2. **Execução do Pipeline**: Execute o script `pipeline.py` para iniciar o processo ETL. O script lerá os arquivos JSON, calculará o total e salvará os resultados em arquivos CSV e Parquet.

```bash
python pipeline.py
```

3. **Saída**: Os arquivos de saída serão gerados na mesma pasta, com os nomes `dados.csv` e `dados.parquet`.


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull request.

---

Esse README fornece uma visão geral clara do projeto, suas dependências, estrutura e como usá-lo. Certifique-se de ajustar qualquer detalhe específico conforme necessário para seu projeto.
