# Title: Web Scraping com Python

# Importando as bibliotecas necessárias
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import csv 

# URL base do site
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Número total de páginas a serem extraídas
total_pages = 2

# Abrindo um arquivo CSV para escrita
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability', 'Rating', 'Image URL', 'Product URL'])

    # Iterando sobre cada página
    for page in range(1, total_pages + 1):
        # Construindo a URL da página atual
        url = base_url.format(page)

        # Fazendo a requisição ao site
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Analisando o conteúdo HTML da página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrando todos os produtos na página
        products = soup.find_all('article', class_='product_pod')

        # Iterando sobre cada produto e extraindo as informações
        for product in products:
            # Título do produto
            title = product.h3.a['title']

            # Preço do produto
            price = product.find('p', class_='price_color').text

            # Disponibilidade do produto
            availability = product.find('p', class_='instock availability').text.strip()

            # Avaliação do produto
            rating = product.p['class'][1]

            # URL da imagem do produto
            image_url = product.find('img')['src'].replace('..', 'https://books.toscrape.com')

            # URL do produto
            product_url = 'https://books.toscrape.com/catalogue/' + product.h3.a['href']

            # Escrevendo os dados no CSV
            writer.writerow([title, price, availability, rating, image_url, product_url])
            
            # Escrevendo as informações no terminal
            print('------------------------------------')
            print(f'Titulo: {title}')
            print(f'Preco: {price[1:]} Libras')
            print(f'Disponibilidade: {availability}')
            print(f'Avaliacao: {rating}')
            print(f'URL da imagem: {image_url}')
            print(f'URL do produto: {product_url}')
            
print('Dados extraídos e salvos no arquivo products.csv')
