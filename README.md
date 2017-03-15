# slackmoji

Python tool for downloading custom Slack emojis from a given team domain.

Requirements
============

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Slack API token](https://api.slack.com/custom-integrations/legacy-tokens)

Setup
=====
```
pip install -r requirements.txt
```

Usage
=====
Basic Usage:
```
python main.py -d MySlackTeam -t some-auth-token-1234
```
CLI Options:
```
--folder (-f) # Image output folder [default='images']
--domain (-d) # Slack team domain [required]
--token (-t) # Slack API token [required]
```
CLI Example:
```
python main.py --folder=emojis --domain=MySlackTeam --token=some-auth-token-1234
```
