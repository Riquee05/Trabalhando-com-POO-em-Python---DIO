O Poetry é uma ferramenta para gerenciar dependências e pacotes no Python, que visa simplificar o processo de gerenciamento de bibliotecas e dependências, além de facilitar a publicação de pacotes. Aqui estão os principais comandos e como utilizá-los:
Instalação do Poetry

Instalar o Poetry:



    curl -sSL https://install.python-poetry.org | python3 -

Após a instalação, você pode precisar adicionar o Poetry ao seu PATH, conforme as instruções fornecidas pela instalação.

Inicializando um Projeto com Poetry

Criar um novo projeto:



    poetry new nome_do_projeto

Inicializar o Poetry em um projeto existente:



    poetry init

Gerenciamento de Dependências

Adicionar uma dependência ao projeto:



    poetry add nome_do_pacote

Exemplo:



    poetry add requests

Adicionar uma dependência de desenvolvimento:



    poetry add --dev nome_do_pacote

Exemplo:



    poetry add --dev pytest

Remover uma dependência do projeto:



    poetry remove nome_do_pacote

Atualizar as dependências:



    poetry update

Usando o Ambiente Virtual do Poetry

O Poetry cria e gerencia automaticamente um ambiente virtual para o projeto.

Ativar o ambiente virtual:



    poetry shell

Executar comandos dentro do ambiente virtual:



    poetry run comando

Exemplo:



    poetry run python script.py

Publicação de Pacotes

Construir o pacote:



    poetry build

Publicar o pacote no PyPI:



    poetry publish --repository pypi

Gerenciamento de Arquivos de Configuração

O Poetry utiliza dois arquivos principais para gerenciar dependências e configurações do projeto: pyproject.toml e poetry.lock.

    pyproject.toml: Contém as configurações do projeto e as dependências especificadas.
    poetry.lock: Registra as versões exatas das dependências instaladas, garantindo que o ambiente seja replicável.

Exemplo de pyproject.toml

toml

    [tool.poetry]
    name = "meu_projeto"
    version = "0.1.0"
    description = ""
    authors = ["Seu Nome <seuemail@example.com>"]

    [tool.poetry.dependencies]
    python = "^3.8"
    requests = "^2.25.1"

    [tool.poetry.dev-dependencies]
    pytest = "^6.2.2"

Exemplo de Comandos Poetry

Criar um novo projeto:



    poetry new meu_projeto
    cd meu_projeto

Adicionar dependências:



    poetry add flask
    poetry add --dev black

Executar o ambiente virtual:



    poetry shell

Instalar todas as dependências listadas em pyproject.toml:



    poetry install

O Poetry simplifica significativamente o gerenciamento de dependências e ambientes em Python, proporcionando uma maneira mais eficiente e organizada de trabalhar com projetos Python.
