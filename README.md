# Ambiente de Laboratório - Data Collection and Storage

## Contexto Geral

Este repositório contém a infraestrutura completa para o laboratório da disciplina de Data Collection and Storage. O projeto utiliza o Docker Compose para provisionar uma stack moderna de engenharia de dados, permitindo que os alunos executem casos de uso práticos em um ambiente isolado, reprodutível e acessível diretamente pela nuvem através do GitHub Codespaces.

O objetivo é fornecer uma experiência prática com ferramentas padrão da indústria, focando em um na ingestão de dados que vai desde bancos operacionais (SQL e NoSQL), processos de pré-processamento e armazenagem até um data lakehouse, passando por uma plataforma de streaming de eventos em tempo real.

## Stack de Tecnologias

Este ambiente é composto pelos seguintes serviços, cada um em seu próprio contêiner, simulando uma arquitetura de dados moderna:

* **JupyterLab**: É o ambiente de desenvolvimento interativo principal. Através de notebooks (`.ipynb`), os alunos irão escrever e executar código Python e Spark para interagir com todos os outros serviços da stack.
    * **PySpark**: A biblioteca que permite usar o poder do Apache Spark em Python. É a principal ferramenta para processamento de dados em larga escala (ETL, pré-processamento, etc.).
    * **Apache Iceberg**: Um formato de tabela aberta de alto desempenho para data lakes. Ele será usado para criar e gerenciar as tabelas do nosso data lakehouse sobre os dados armazenados no MinIO.
* **MinIO**: Um servidor de armazenamento de objetos compatível com a API do Amazon S3. No nosso projeto, ele funciona como o **Data Lake**, o repositório central para armazenar dados brutos e processados em diversos formatos (CSV, Parquet, tabelas Iceberg, etc.).
* **PostgreSQL**: Um robusto banco de dados relacional (SQL). Ele simula uma **fonte de dados operacional** transacional, como um sistema de e-commerce ou um CRM, de onde os dados serão coletados.
* **MongoDB**: Um banco de dados não-relacional (NoSQL) orientado a documentos. Ele simula outra **fonte de dados operacional** comum, ideal para dados semiestruturados ou flexíveis.
* **Apache Kafka**: Uma plataforma de streaming de eventos distribuída. Funciona como o "sistema nervoso central" para o tráfego de dados em tempo real. Eventos de alteração dos bancos de dados serão publicados aqui.
* **Debezium (rodando no Kafka Connect)**: Uma ferramenta de **Captura de Dados de Mudança (CDC)**. O Debezium monitora os logs de transações do PostgreSQL, captura todas as inserções, atualizações e exclusões em tempo real e as publica como eventos no Kafka, sem a necessidade de modificar as aplicações originais.

## Estrutura do Projeto e Finalidade dos Arquivos

A estrutura de arquivos foi projetada para ser intuitiva e otimizada para a execução no GitHub Codespaces.

```
MBA-DATA-COLLECTION/
│
├── .devcontainer/
│   └── devcontainer.json      # Automatiza a configuração do ambiente no Codespaces.
│
├── notebooks/
│   ├── 00-Configuracao-Spark.ipynb
│   └── .gitkeep               # Garante a existência da pasta 'notebooks' no Git.
│
├── .gitignore                 # Define quais arquivos devem ser ignorados pelo Git.
├── docker-compose.yml         # "Planta baixa" da infraestrutura de serviços.
└── README.md                  # Este guia.
```

### `.devcontainer/devcontainer.json`

* **Finalidade**: Este é o arquivo que automatiza a experiência no GitHub Codespaces. Ele instrui a plataforma a:
    * **Utilizar o arquivo `docker-compose.yml` para definir os serviços.
    * **Conectar o editor de código ao contêiner principal (`jupyterlab`).
    * **Executar o comando `docker compose up -d` automaticamente após a criação do ambiente.
    * **Encaminhar as portas dos serviços (Jupyter, MinIO, etc.) e abrir o JupyterLab no navegador, tornando o ambiente pronto para uso sem qualquer intervenção manual.

### `notebooks/`

* **Finalidade**: Esta é a pasta de trabalho principal para os alunos.
    * **`00-Configuracao-Spark.ipynb`**: Contém o código essencial e reutilizável para inicializar a `SparkSession` com todas as dependências e configurações necessárias para se conectar ao MinIO, Iceberg, PostgreSQL e MongoDB. Este notebook deve ser o ponto de partida para todos os exercícios.
    * **`.gitkeep`**: Um arquivo vazio cuja única função é garantir que a pasta `notebooks`, mesmo que inicialmente vazia de outros arquivos, seja incluída no repositório Git.

### `.gitignore`

* **Finalidade**: Define uma lista de arquivos e pastas que o sistema de controle de versão Git deve ignorar. Isso é crucial para manter o repositório limpo, evitando o envio de arquivos de cache (`__pycache__`), logs, credenciais locais ou arquivos de configuração de editores de código (`.vscode/`, `.idea/`).

### `docker-compose.yml`

* **Finalidade**: Este é o coração da infraestrutura. É um arquivo declarativo que descreve todos os serviços (contêineres) que compõem o ambiente, suas imagens, configurações, variáveis de ambiente, portas mapeadas, volumes de dados e como eles se conectam através de uma rede virtual privada. Ele garante que toda a stack seja iniciada de forma orquestrada e reprodutível com um único comando.

### `README.md`

* **Finalidade**: É a porta de entrada e o guia principal do projeto. Ele contém as instruções essenciais sobre o que é o projeto, quais tecnologias utiliza e, mais importante, o passo a passo de como iniciar e utilizar o ambiente de laboratório.

## Execução do Ambiente na Nuvem (GitHub Codespaces)

Este é o método principal e recomendado. Ele é totalmente automatizado.

#### Pré-requisitos

* Uma conta GitHub com o **GitHub Student Developer Pack** ativo. Inscreva-se em [**education.github.com/pack**](https://education.github.com/pack) para obter uma quota mensal gratuita para o Codespaces.

#### Passo a Passo da Execução

1.  **Iniciar o Codespace**:
    * Navegue até o repositório do projeto no GitHub.
    * Clique no botão verde **`< > Code`**, selecione a aba **"Codespaces"** e clique em **"Create codespace on main"**.
2.  **Aguarde a Automação**:
    * O Codespace será criado. A configuração no arquivo `.devcontainer/devcontainer.json` irá **automaticamente**:
        1.  Iniciar todos os serviços da stack com `docker compose up -d`.
        2.  Encaminhar as portas necessárias (Jupyter, MinIO, entre outros.).
        3.  Abrir a interface do **JupyterLab em uma nova aba do seu navegador**.
    * O ambiente estará pronto para uso em poucos minutos, sem a necessidade de executar nenhum comando manual.

## Pontos de Acesso e Utilização

### Acesso aos Serviços no Codespaces

1.  O **JupyterLab** (`porta 8888`) abrirá automaticamente. A senha é `jupyterlab`.
2.  Para acessar outros serviços (como o MinIO Console), vá para a aba **"PORTS"** no painel inferior do Codespace.
3.  Clique no link **"Forwarded Address"** ao lado do serviço desejado (exemplo: MinIO Console na porta 9001).

### Utilizando os Notebooks

1.  No JupyterLab, navegue até a pasta `notebooks`.
2.  Abra o notebook **`00-Configuracao-Spark.ipynb`** e execute a célula para inicializar o Spark.
3.  Crie novos notebooks nesta pasta para os exercícios.

## Gerenciando o Ambiente Codespaces (MUITO IMPORTANTE)

Para evitar o consumo da sua quota gratuita, **sempre pare o Codespace quando não estiver usando**.

* **Como Parar**: Vá para [**github.com/codespaces**](https://github.com/codespaces), clique nos três pontos (`...`) ao lado do seu codespace e selecione **"Stop codespace"**.

## (Alternativa) Execução Local

Esta opção é para usuários que desejam rodar toda a infraestrutura diretamente em sua própria máquina, sem depender da nuvem.

### Pré-requisitos

1.  **Git**: Essencial para clonar o repositório.
2.  **Docker Desktop**: A aplicação que gerencia os contêineres.
    * **Usuários Windows**: É **obrigatório** ter o **WSL 2 (Windows Subsystem for Linux)** instalado e habilitado.

### Passo a Passo da Execução

1.  **Clonar o Repositório**:
    * Abra um terminal (Git Bash, PowerShell, etc.).
    * Navegue até o diretório onde deseja salvar o projeto e execute o comando:
        ```bash
        git clone <URL_DO_SEU_REPOSITORIO_NO_GITHUB>
        ```
    * Entre na pasta do projeto:
        ```bash
        cd <NOME_DA_PASTA_DO_PROJETO>
        ```
2.  **Iniciar a Infraestrutura**:
    * No terminal, dentro da pasta do projeto, execute:
        ```bash
        docker compose up -d
        ```
    * **Nota**: Na primeira vez, o Docker fará o download de todas as imagens, o que pode levar vários minutos. Nas execuções seguintes, o processo será quase instantâneo.

### Acesso aos Serviços (Localhost)

Quando rodando localmente, os serviços são acessados através do `localhost` no seu navegador ou ferramenta de BI:

* **JupyterLab**: `http://localhost:8888` (Senha: `jupyterlab`)
* **MinIO Console**: `http://localhost:9001` (Usuário/Senha: `minioadmin`)
* **Kafka Connect API**: `http://localhost:8083`
* **Spark UI**: `http://localhost:4040` (Fica ativo *após* iniciar uma `SparkSession` no Jupyter)
* **PostgreSQL**: `localhost:5432`
* **MongoDB**: `localhost:27017`

### Gerenciando o Ambiente Local

* Para **parar** os serviços (liberando CPU/RAM): `docker compose stop`
* Para **iniciar** novamente: `docker compose start`
* Para **parar e remover** os contêineres: `docker compose down`
* Para **reiniciar o ambiente do zero (deletando os dados)**: `docker compose down -v`
