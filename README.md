# Curso Django

> Criação do aplicativo Simple Mooc

See: https://www.udemy.com/course/python-3-na-web-com-django-basico-intermediario

>Framework de estilos: Pure CSS

See: https://purecss.io

>Biblioteca Javascript: YUI

See: https://yuilibrary.com

## Confiruração o ambiente:

* Instalar Pip
>* `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
>
>* `python3 get-pip.py`
>
>* Instalar Pip em Ubuntu e derivados
>  >* `sudo apt install python3-pip`

* Criar um Virtual Enviroment
>* Instalar o virtualenv:
>  >* `pip3 install virtualenv`
>* Rodar o comando:
>  >* `virtualenv venv -p '<path_ onde está a instalação do Python>'` 
>  >* Exemplo: `virtualenv venv -p /usr/lib/python3.8`
>
* Ativar o ambiente virtual
>* Acessar a pasta onde está o activate: 
>  >* `cd venv/bin`
>* Executar o comando para ativar
>  >* `. activate`

## Instalar o Django

> See: https://www.djangoproject.com/start/
>
> `pip install Django`
>
> Testando a instalação:
>* `python`
>* `import django`
 >* >* Se não apresentou erro, é porque funcionou.
## Django admin
> Na raiz do projeto executar o comando:
>
> `django-admin.py startproject simplemooc`
>
> 
## Criando tabelas no banco
> `python manage.py migrate --run-syncdb`

## Criando minha primeira aplicação:
> `python manage.py startapp core`
> 
> Django é baseado em apps, (Ver sessão arquivos instalados no arquivo: ./simplemooc/simplemooc/settings.py)

## Rodando
> Na pasta simplemooc executar o comando:
>* `python manage.py runserver`