# pylint: disable = C0103, C0111

# Standard Library
import json
import mimetypes
from os import makedirs
from subprocess import check_output

# Third Party
import requests

def list_emojis(domain, token):
    script = ['bin/list_emojis.sh {0} {1}'.format(domain, token)]
    response = check_output(script, shell=True)
    print "\nGot list of emojis from %s Slack domain!" % domain
    return response

def download_emojis(emojis, folder):
    count = 0
    makedirs(folder)
    emojis = json.loads(emojis)["emoji"]
    print "\nDownloading emojis from list..."
    for name, url in emojis.iteritems():
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
            count = count + 1
    print "\nFinished downloading %s emojis!" % count
