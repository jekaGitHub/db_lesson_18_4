import os

from config import config
from utils import get_youtube_data, create_database, save_data_to_database
from dotenv import load_dotenv


load_dotenv()


def main():
    api_key = os.getenv('YT_API_KEY')
    channels_ids = [
        'UCMCgOm8GZkHp8zJ6l7_hIuA', # вДудь
        'UC1eFXmJNkjITxPFWTy6RsWg', # Редакция
    ]
    params = config()

    data = get_youtube_data(api_key, channels_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
