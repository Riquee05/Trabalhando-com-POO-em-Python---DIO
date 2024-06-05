O Pipenv é uma ferramenta de gerenciamento de dependências para Python que combina o melhor de pip e virtualenv. Ele cria e gerencia ambientes virtuais para seus projetos e simplifica o processo de instalação e atualização de pacotes, além de gerar arquivos Pipfile e Pipfile.lock para especificar e bloquear as dependências do projeto.
Instalando o Pipenv

Primeiro, você precisa instalar o Pipenv. Você pode fazer isso usando o pip:



    pip install pipenv

Usando o Pipenv
Criando e Gerenciando um Ambiente Virtual

Criar um novo ambiente virtual e instalar dependências:



    pipenv install nome_do_pacote

Exemplo:



    pipenv install requests

Isso cria um arquivo Pipfile com as dependências do seu projeto. Se você adicionar a flag --dev, o pacote será adicionado às dependências de desenvolvimento:



    pipenv install nome_do_pacote --dev

Ativar o ambiente virtual:



    pipenv shell

Desativar o ambiente virtual:



exit

Gerenciando Dependências

Instalar todas as dependências listadas no Pipfile:



    pipenv install

Adicionar uma nova dependência:



    pipenv install nome_do_pacote

Remover uma dependência:



    pipenv uninstall nome_do_pacote

Atualizar uma dependência:



    pipenv update nome_do_pacote

Atualizar todas as dependências:



    pipenv update

Arquivos Pipfile e Pipfile.lock

    Pipfile: Este arquivo contém as dependências do seu projeto. É parecido com o requirements.txt, mas é mais legível e organizado.
    Pipfile.lock: Este arquivo contém um bloqueio de versões exato das dependências instaladas. Isso garante que a instalação das dependências seja reproduzível e consistente em diferentes ambientes.

Executando Scripts com Pipenv

Você pode executar scripts Python diretamente no ambiente virtual gerenciado pelo Pipenv sem ativar manualmente o shell:



    pipenv run python script.py

Verificando Dependências de Segurança

O Pipenv pode verificar automaticamente suas dependências em busca de vulnerabilidades conhecidas:



    pipenv check

Exemplo Completo de Uso do Pipenv

Inicialize um novo projeto:



    mkdir meu_projeto
    cd meu_projeto
    pipenv install requests

Adicionar uma dependência de desenvolvimento:



    pipenv install --dev pytest

Ativar o ambiente virtual:



    pipenv shell

Criar e rodar um script:

python

# script.py
    import requests

    response = requests.get('https://httpbin.org/get')
    print(response.json())



    pipenv run python script.py

Verificar por vulnerabilidades:



    pipenv check

Com o Pipenv, você pode gerenciar dependências de forma mais eficiente e segura, mantendo um ambiente virtual isolado para cada projeto.