# Clientes
## Instalação
Crie e ative a virtual env:

```sh
python3 -m venv venv
source venv/bin/activate
```

Faça download do projeto:

```sh
git clone https://github.com/caikesilva/clientes.git
```
Instale as dependencias:
```sh
pip install -r requirements.txt
```
Execute as migrações:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Crie um usuario e inicie o servidor:
```sh
python3 manage.py createsuperuser
python3 manage.py runserver
```
## Administração
Acesse a url de administração:
http://127.0.0.1:8000/admin/
## Aplicação
Acesse a url da aplicação e faça upload do arquivo .xlsx através do formulario.
http://127.0.0.1:8000/clientes/upload/

## API
Acesse o endpoint abaixo para retornar as mulheres de mereen.
http://127.0.0.1:8000/clientes-api/mulheres-mereen/
Exemplo de retorno:
```code
{
        "id": 306,
        "nome": "Joi",
        "sobrenome": "Gomes",
        "sexo": "F",
        "nascimento": "2000-26-80",
        "bairro": "Bairro 2",
        "cidade": "Meeren",
        "estado": "Westeros",
        "numero": 2
    },
```
Acesse o endpoint abaixo para filtrar e retornar pessoas pelo sexo.
http://127.0.0.1:8000/clientes-api/filtro/?sexo=M
Exemplo de retorno:
```code
{
        "id": 327,
        "nome": "José",
        "sobrenome": "Pedro",
        "sexo": "M",
        "nascimento": "9831-56-40",
        "bairro": "Bairro 3",
        "cidade": "Meeren",
        "estado": "Braavos",
        "numero": 1
    },
```