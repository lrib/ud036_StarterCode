# ud036 Starter Code

O projeto é uma tarefa chamada 'Movie Trailer Website' do módulo 1 do curso de Full Stack Developer da Udacity, turma 16/JAN/2019.

O projeto é criado em função das seguintes características:

- Dever ser em Python;

- Deve conter uma estrutura de dados (ou seja, uma Classe Python) para armazenar seus filmes favoritos, incluindo o título, URL da capa 
(ou do cartaz) e link do YouTube para o trailer do filme;

- Deve conter instâncias dessa classe Python para representar seus filmes favoritos; agrupe todas as instâncias em uma lista;

- A página web é estática e é gerada a partir da execução do arquvio 'entertainment_center.py'.

## Preparação

A execução do script 'entertainment_center.py' faz uso da API do site themoviedb.org. Para fazer funcionar corretamente é necessário editar o arquivo 'entertainment_center.py' e na variável APIKEY_THMOVIEDB atribuir o valor da chave do API fornecida pelo registro do site themoviedb.org. 

Dentro do arquivo 'entertainment_center.py' contém uma lista (array_movie) com os nomes dos filmes que serão exibidos na página estatica, com os titulos do filme lançados nos Estados Unidos.

## Execução

Com o título dos filmes cadastrados na lista (array_movie) dentro do 'entertainment_center.py' e da adição da chave do API na variável APIKEY_THMOVIEDB no arquivo 'entertainment_center.py' executar o script. Se ocorrer algum erro na coleta da informação do titulo do filme pelo API, o dado do filme não será informado.

Com as informação cadastradas no arquvio 'entertainment_center.py', este irã coletar as informação dos filmes na base de dados do themoviedb.org e irá fornecer estas informações para serem utilizadas pelo arquvio 'fresh_tomatoes.py', como titulo, descrição, url do poster e url do trailer.

O arquivo 'fresh_tomatoes.py' recebe os dados do filme e quando executado é gerado o arquivo final fresh_tomatoes.html com a apresentação dos dados do filmes.

## Pré-requisitos do projeto:                
- Versão do Python: 2.7.10
- É necessário a instalação da lib requests
- É necessário a instalação da lib webbrowser
- É necessário possuir uma API_KEY para acesso da API do themoviedb.org

## Fontes consultadas:
https://realpython.com/api-integration-in-python/

http://docs.python-requests.org/en/master/

http://www.omdbapi.com/api

http://pep8online.com/checkresult

