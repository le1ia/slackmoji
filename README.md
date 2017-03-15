# slackmoji

Python tool for downloading custom Slack emojis from a given team domain.

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
