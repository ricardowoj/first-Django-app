# Atividade - Tutorial Django Framework

Atividade inicial sobre o tutorial do Django Framework.

## O que deve estar instalado

Para fazer o exercício, você deve ter instalado:

 * Python versão 3.5 (ou superior)
 * Django versão 2.2

Para garantir uma maior compatibilidade com o exercício, recomenda-se instalar os requisitos usando o comando:

```shell
pip install -r requirements.txt
```

## Como fazer

Nessa atividade, deve ser desenvolvida a aplicação de votação (*Polls*) presente no tutorial oficial do site do framework (https://docs.djangoproject.com/pt-br/2.2/intro/tutorial01/).

Basta seguir os passos dos 7 itens do tutorial. Os nomes de classes, métodos e comandos feitos no tutorial devem ser mantidos, para que os testes funcionem corretamente.

O projeto Django já está criado, então não há necessidade do primeiro comando (`django-admin startproject ...`).

Conforme for andando o projeto, execute o comando de testes do Django para saveriicar quais testes passaram e quais ainda não:

```shell
python manage.py test
```

Caso queira executar apenas um dos testes, por exemplo o *test_admin.py*, rode com o seguinte comando:

```shell
python manage.py test tutorial.tests.test_admin
```

## Como Funciona a Nota

Dentro do diretório `tutorial/tests` estão 5 arquivos de testes que serão utilizados para corrigir o exercício. Cada arquivo tem um conjunto de testes referentes ao que é ensinado no tutorial:

 * Configurações (_test_settings.py_).
 * Construção de Views (_test_views.py_).
 * Construção dos Modelos (_test_models.py_).
 * Construção de Testes (_test_tests.py_).
 * Configuração do Admin (_test_admin.py_).

Cada arquivo contém um conjunto testes e só é considerado correto se todos os testes dentro do conjunto passarem. Cada conjunto dá 2 pontos, ou seja, para tirar 10, todos os 5 conjuntos devem ser considerados corretos.

## Regras Importantes

Preencha os seus dados no arquivo **autor.json**, como nome completo, e-mail da faculdade e seu RA.

O mais importante é não renomear a pasta inicial _**tutorial**_ e os arquivos de teste dentro da pasta `tutorial/tests`. Qualquer alteração nesses arquivos de teste invalidará o exercício inteiro.

Erros de sintaxe do Python também acabarão invalidando o exerício (ou parte dele).