import os
import zipfile
import shutil
import urllib.request
import gdown
import subprocess

BASE_DIR = os.getcwd()

def extract_zip(extraction_folder, zip_name):
    if not os.path.exists(extraction_folder):
        os.makedirs(extraction_folder)
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extraction_folder)
    os.remove(zip_name)


def download_online_model(url):
        zip_name = url.split('/')[-1]

        if 'pixeldrain.com' in url:
            url = f'https://pixeldrain.com/api/file/{zip_name}'

        urllib.request.urlretrieve(url, zip_name)

        print('[~] Extracting zip...')
        extract_zip(BASE_DIR, zip_name)
        print('[+] Models successfully downloaded!')



url = 'https://pixeldrain.com/u/1eZUbSQK'

download_online_model(url)