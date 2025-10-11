# Desenvolvimento PySpark e PostgreSQL

Este repositório fornece um ambiente de desenvolvimento pré-configurado para projetos que utilizam PySpark, Pandas e PostgreSQL. O objetivo principal é padronizar e acelerar a configuração do ambiente de trabalho através do uso de Dev Containers e GitHub Codespaces.

---

## Sobre o Ambiente e a Tecnologia

Este é um template de ambiente de desenvolvimento baseado na especificação **Dev Containers** e projetado para ser executado na plataforma **GitHub Codespaces**. Ele automatiza a criação de um ambiente de desenvolvimento conteinerizado que já inclui todas as ferramentas e dependências necessárias.

### O que é um Dev Container?

Um **Dev Container (ou Contêiner de Desenvolvimento)** é um ambiente de desenvolvimento completo que roda dentro de um contêiner Docker. Trata-se de um padrão de código aberto que permite definir todos os componentes de um ambiente como código.

* **Como funciona?** Através de um arquivo de configuração (`.devcontainer/devcontainer.json`), você especifica tudo o que o projeto precisa: o sistema operacional base, versões de linguagens (Python, etc.), ferramentas, extensões do editor (VS Code) e configurações.
* **Qual o benefício?** Ele resolve o clássico problema do "mas na minha máquina funciona". Como o ambiente é definido em código, qualquer pessoa que abrir o projeto terá um ambiente **idêntico, consistente e reproduzível**, garantindo que o código se comporte da mesma forma para todos.

### O que é o GitHub Codespaces?

O **GitHub Codespaces** é um produto da GitHub que oferece ambientes de desenvolvimento completos na nuvem. Pense nele como "Dev Containers como um Serviço".

* **Como funciona?** O Codespaces lê a configuração do Dev Container (`.devcontainer/`) diretamente do seu repositório. Em seguida, ele utiliza essa configuração para construir e hospedar o seu ambiente em uma máquina virtual poderosa na nuvem. Você acessa este ambiente completo através do seu navegador, sem precisar instalar nada localmente.
* **Qual o benefício?** Ele combina o poder da padronização dos Dev Containers com a flexibilidade da nuvem. Você pode programar de qualquer dispositivo, ter acesso a recursos computacionais robustos sob demanda e começar a trabalhar em um projeto novo em questão de minutos, com o ambiente já 100% configurado.

---

## O que é este repositório?

Este é um template de ambiente de desenvolvimento baseado na especificação **Dev Containers** e projetado para ser executado na plataforma **GitHub Codespaces**.

Ele automatiza a criação de um ambiente de desenvolvimento conteinerizado que já inclui todas as ferramentas e dependências necessárias para iniciar um projeto de dados.

## Tecnologias Inclusas

O ambiente provisionado inclui as seguintes ferramentas:

* **Python 3.11:** Linguagem de programação base.
* **Apache Spark (via PySpark):** Plataforma para processamento de dados em larga escala.
* **Pandas:** Biblioteca para manipulação e análise de dados.
* **PostgreSQL:** Banco de dados relacional de código aberto.
* **Docker:** Plataforma de containerização que gerencia o ambiente.
* **GitHub Codespaces:** Plataforma de nuvem que hospeda e executa o ambiente.

---

## Principais Vantagens

* **Inicialização Rápida:** O ambiente fica pronto para uso em poucos minutos, eliminando a necessidade de instalações e configurações manuais.
* **Consistência:** Garante que todos os usuários operem com a mesma configuração de software e dependências, prevenindo problemas de compatibilidade entre diferentes máquinas.
* **Isolamento:** As ferramentas e bibliotecas são executadas dentro de containers, não interferindo com a configuração da máquina local do usuário.
* **Portabilidade:** O ambiente pode ser acessado de qualquer dispositivo com um navegador web, sem depender da potência do hardware local.

---

## Guia de Utilização

Para utilizar este ambiente, siga os passos abaixo.

### Passo 1: Criar um "Fork" do Repositório

É recomendado criar uma cópia pessoal deste repositório na sua conta do GitHub. Um "fork" permite que você modifique o código livremente.

1.  Clique no botão **"Fork"** no canto superior direito desta página.
2.  Na tela seguinte, confirme a criação do fork clicando em **"Create fork"**.

### Passo 2: Iniciar o GitHub Codespace

O Codespace irá construir e iniciar o ambiente de desenvolvimento.

1.  Na página do seu fork, clique no botão verde **`< > Code`**.
2.  Selecione a aba **"Codespaces"**.
3.  Clique em **"Create codespace on main"**.

O processo de inicialização pode levar alguns minutos, especialmente no primeiro uso. Ao final, uma nova aba será aberta com uma instância do VS Code funcional em seu navegador.

### Passo 3: Verificação do Ambiente

Para confirmar que todos os serviços estão operacionais e se comunicando, execute os scripts de teste localizados na pasta `src/`.

Abra o terminal integrado no VS Code (geralmente na parte inferior da tela) e execute os seguintes comandos:

* **Teste do Pandas:**
    ```bash
    python src/teste_pandas.py
    ```
    *(A saída esperada é a impressão de DataFrames com dados de produtos).*

* **Teste do Spark:**
    ```bash
    python src/teste_spark.py
    ```
    *(A saída deve ser similar à do teste do Pandas, mas processada pelo Spark).*

* **Teste de Conexão com o PostgreSQL:**
    ```bash
    python src/teste_postgres.py
    ```
    *(A saída esperada é uma mensagem de sucesso com a versão do PostgreSQL).*

A execução bem-sucedida de todos os scripts confirma que o ambiente está configurado corretamente.

---

## Salvando e Enviando Alterações para o GitHub (Fluxo Básico do Git)

Após modificar ou criar arquivos, você precisa salvar seu progresso no GitHub. Este é o ciclo padrão que você usará repetidamente.

### Passo 1: Verificar o Status das Alterações

Antes de tudo, veja o que você modificou. Este comando lista todos os arquivos novos, modificados ou deletados.

```bash
git status
```

### Passo 2: Adicionar as Alterações para "Empacotamento"

Adicione os arquivos que você deseja salvar ao "pacote" (Staging Area).

```bash
# Para adicionar TODOS os arquivos modificados e novos
git add .

# Ou, para adicionar um arquivo específico
git add src/seu_novo_arquivo.py
```

### Passo 3: Criar um "Pacote" de Salvamento (Commit)

Crie um ponto na história do projeto com as alterações que você adicionou. **É crucial escrever uma mensagem clara** que descreva o que você fez.

```bash
git commit -m "Sua mensagem descritiva aqui"

# Exemplo:
# git commit -m "Adiciona script para calcular vendas mensais"
```

### Passo 4: Enviar as Alterações para o GitHub

Envie o seu "pacote" (commit) para o seu repositório remoto no GitHub, atualizando o projeto na nuvem.

```bash
git push
```
O ciclo completo é: **`status` → `add` → `commit` → `push`**.

---

## Gerenciamento do Codespace

### Renomeando um Codespace

Por padrão, o GitHub gera nomes aleatórios para os Codespaces (ex: `fictional-space-engine-g45pr7q7wxf6p7r`), o que pode dificultar a identificação se você tiver vários. É uma boa prática renomeá-los para algo mais descritivo.

1.  Acesse a sua lista de Codespaces em: **[github.com/codespaces](https://github.com/codespaces)**.
2.  Encontre o Codespace que deseja renomear e clique no menu de três pontos (`...`).
3.  Selecione a opção **"Rename"** (Renomear) e insira o novo nome.

### Conectando ao Banco de Dados PostgreSQL

Você pode interagir diretamente com o banco de dados PostgreSQL de dentro do VS Code, sem precisar de ferramentas externas. Isso é possível graças a uma extensão que já vem pré-instalada neste ambiente.

**Passo a Passo para Conectar e Executar uma Consulta:**

1.  **Abra a Aba do Banco de Dados:**
    * Na barra de atividades do lado esquerdo do VS Code, clique no ícone que parece um cilindro (banco de dados).

2.  **Crie uma Nova Conexão:**
    * No painel da extensão, clique no ícone `+` para adicionar uma nova conexão.

3.  **Preencha os Detalhes da Conexão:**
    * Um formulário aparecerá. Preencha-o com as **exatas** credenciais definidas no arquivo `.devcontainer/docker-compose.yml`:
        * **Host:** `db`  *(Este é o nome do serviço do Postgres no Docker Compose. **Não use `localhost`**)*.
        * **User:** `myuser`
        * **Password:** `mypassword`
        * **Port:** `5432` *(padrão)*
        * **Database:** `mydb`
    * Clique no botão **"Connect"**.

4.  **Explore e Consulte o Banco de Dados:**
    * Se a conexão for bem-sucedida, você verá a conexão `db` listada no painel.
    * Você pode expandi-la para ver seu banco de dados (`mydb`), schemas (como `public`) e tabelas (se houver alguma).
    * Para executar uma consulta, clique com o botão direito na sua conexão ou no banco de dados e selecione **"New Query"**. Uma nova aba se abrirá.
    * Digite um comando SQL (ex: `SELECT version();` ou `SELECT * FROM sua_tabela;`) e clique no botão **"Run"** (ou use o atalho `Ctrl+Alt+E`). Os resultados aparecerão em uma tabela na parte inferior.

---

## Próximos Passos

Com o ambiente funcional, as seguintes ações podem ser realizadas:

* Modificar os scripts existentes na pasta `src/`.
* Adicionar novos scripts Python para desenvolver novas funcionalidades.
* Utilizar o ambiente para conectar-se a fontes de dados externas, processar informações e armazenar os resultados no banco de dados PostgreSQL.
