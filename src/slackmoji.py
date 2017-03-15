# pylint: disable = C0103, C0111

# Standard Library
import json
import mimetypes
from os import makedirs

# Third Party
import requests

def list_emojis(domain, token):
    url = r'https://%s.slack.com/api/emoji.list' % domain
    data = [('token', token)]
    response = requests.post(url, data=data)
    print "\nGot list of emojis from %s Slack domain!" % domain
    emojis = json.loads(response.text)["emoji"]
    return emojis

def download_emojis(emojis, folder):
    count = 0
    makedirs(folder)
    print "\nDownloading emojis to %s folder..." % folder
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
