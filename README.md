# gn-tech-api
API for requesting some weather data.

Dockerfile com estrutura para o ambiente virtual de python.

1 - Baixar o arquivo
2 - Acessar o diretório pelo prompt de comando e chamar o "Docker build ."
3 - Em seguida, seguir com o "Docker-Compose build"
4 - Por final, subir o Docker-Compose com Docker Compose up!

(IMPORTANTE: Certifique-se de que tenha o Docker instalado na máquina.)

Para ediçoes e modificaçoes no código, pode-se usar o seguinte código para testes:

Docker-Compose run --rm app sh -c "python manage.py <nomedoarquivo>"

O projeto é composto por uma pasta contendo o projeto de Django e o aplicativo de Django. Como não estava conseguindo instalar a library de "requests", tentei usar um venv e deixou-o salvo junto ao projeto, para qualquer coisa (não vai ser usado no momento). A lib requests não se encontra disponível para pip3 ou brew, infelizmente. Pesquisei e achei a urllib que substituiu bem para fazer as requisicoes de GET.

Qualquer coisa, a disposiçao para duvidas!

Muito Obrigado!
