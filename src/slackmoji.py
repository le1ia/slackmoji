import errno
import json
import mimetypes
from os import makedirs
from os.path import isdir
import sys

import requests

def create_folder(folder):
    try:
        makedirs(folder)
    except OSError as err:
        if err.errno == errno.EEXIST and isdir(folder):
            pass
        else:
            raise

def download_emojis(emojis, folder):
    count = 0
    create_folder(folder)
    print(f"\nDownloading emojis to {folder} folder...")
    for name, url in emojis.items():
        if 'alias' in url:
            continue
        else:
            res = requests.get(url)
            cont = res.headers['content-type']
            ext = mimetypes.guess_extension(cont)
            if ext == '.jpe':
                ext = '.jpg'
            output = folder + '/' + name + ext
            with open(output, 'wb') as fd:
                for chunk in res.iter_content(chunk_size=1024):
                    fd.write(chunk)
            count += 1
    print(f"\nFinished downloading {count} emojis!")

def get_emojis(domain, token):
    url = f"https://{domain}.slack.com/api/emoji.list"
    data = [('token', token)]
    response = requests.post(url, data=data)
    body = json.loads(response.text)
    try:
        emojis = body["emoji"]
        print(f"\nGot list of emojis from {domain} Slack domain!")
        return emojis
    except KeyError:
        error = body["error"]
        if error:
            print(f"\nERROR: {error}")
            sys.exit(1)
        else:
            raise
