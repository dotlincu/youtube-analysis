from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve API keys from environment variables
API_KEY1 = os.getenv('API_KEY1')
API_KEY2 = os.getenv('API_KEY2')

config = {
  # Configuração da região da coleta -> Formato: ISO 3166-1 alpha-2
  "region_code": "BR",         

  # Configuração da linguagem da coleta -> Formato: ISO 639-1   
  "relevance_language": "pt",     

  # A coleta ocorre da data final para a data inicial -> [ano, mês, dia]
  "start_date": [2020, 1, 1], 
  "end_date": [2022, 1, 1],

  # API que receberá uma requisição PATCH com payload de um JSON contendo informações acerca da coleta
  # Mantenha uma string vazia "" Caso não tenha configurado
  "api_endpoint": "",
  # Intervalo, em segundos, entre cada envio de dados para a API
  "api_cooldown": 60,                                                   

  # Intervalo, em segundos, entre cada tentativa de requisição para a API apos falha
  "try_again_timeout": 60,                                              

  # Palavras que serão utilizadas para filtrar os títulos dos vídeos
  # "key_words": [
  #   "cassino", "blaze", "pix",
  # ], 
  "key_words": [
    "programacao", "java", "python", "dados"
  ], 

  # KEYs da API v3 do YouTube
  "youtube_keys": [
    API_KEY1,
    API_KEY2
    # "key 3",
    
  ],

  # Queries que serão utilizadas na pesquisa
  # "queries": [
  #   "cassino online", "Casas de aposta", "blaze", "tigrinho"
  # ]
  "queries": [
    "melhores cursos de programação", "java", "python", "banco de dados"
  ]
}
