import requests
import media
import fresh_tomatoes

URL = 'http://api.themoviedb.org/3/search/movie'

APIKEY_THMOVIEDB = 'APIKEY'

# Executa o script

# Cria a matriz com os nomes dos filmes que serão apresentados ao detalhe

array_movie = ['Avatar', 'Inside Man', 'Saving private Ryan', 'Apollo 13', 'Toy story', 'The Rock']  # NOQA

# Apresenta a Key do API do site http://www.omdbapi.com

# Inicializa a matriz/lista movies

movies = []

# Faz um loop em todas as posições da matriz array_movie

for x in array_movie:

    """
    De acordo com o API do site www.omdbapi.com, faz necessario a
    busca de informaçãoes do filme na posição 1 da matriz array_movie
    """

    payload = {'api_key': APIKEY_THMOVIEDB, 'query': x}

    # Cria a solicitacao da API

    resp = requests.get(URL, params=payload)

    # Faz a requisiçao utilizando a API e enalisa a resposta.

    # A resposta deve ser 200. Informacao extradida do site:
    # https://www.themoviedb.org/documentation/api/status-codes

    # Caso a resposta nao seja 200, o processo deve ser ignorado
    # para este filme e com isto faz a adicao de x

    if resp.status_code != 200:

        # Se chegou aqui a resposta nao e 200
        # então não faz a gravacao dos dados.

        x = x + 1

    else:

        # Converte a resposta para JSON

        data = resp.json()

        # Extrai o Titulo do primeiro resultado

        temp_tittle = (data['results'][0]['title'])

        # Extrai a descricao do filme

        temp_plot = (data['results'][0]['overview'])

        # Extrai o poster do filme

        temp_postr = (data['results'][0]['poster_path'])

        # Completa com a URL de localização do poster

        temp_postr = 'https://image.tmdb.org/t/p/w500' + temp_postr

        # Extari o ID do filme, pois o API do Trailer esta em outro URL

        temp_id = (data['results'][0]['id'])

        # Faz acesso ao API do Filme, com o ID extraido do API anterior

        url1 = 'https://api.themoviedb.org/3/movie/' + str(temp_id) + '/videos?api_key=' + APIKEY_THMOVIEDB + '&language=en-US'  # NOQA

        # Extrai a informação do API do endereço acima

        resp2 = requests.get(url1)

        # Converte a informação em JSON

        data_id = resp2.json()

        # Extrai o ID do trailer do Youtube

        youtube_comp = data_id['results'][0]['key']

        # Completa o URL do Trailer com o ID localizado pelo JSON

        youtube_comp = 'https://www.youtube.com/watch?v=' + youtube_comp

        # Ao chegar aqui contem todas as informações para
        # chamar a classe Movie dentro o media.py

        temp_movies = media.Movie(temp_tittle,
                                  temp_plot,
                                  temp_postr,
                                  youtube_comp)

        # a variavel movies contem as entradas de filmes,
        # e com isso esta variavel é atualizada com os dados extraidos no loop.

        movies = movies + [temp_movies]

# Chama a função open_movies_page com
# os dados de movies na classe fresh_tomatoes

fresh_tomatoes.open_movies_page(movies)
