# slackmoji

Python tool for downloading custom Slack emojis from a given team domain.

## Setup

Requirements:

* [Python 3.7.3](https://www.python.org/downloads/release/python-373/)
* [Slack API token](https://api.slack.com/custom-integrations/legacy-tokens)

Installation:

```bash
pip install -r requirements.txt
```

## Usage

Basic Usage:

```bash
python main.py -d MySlackTeam -t some-auth-token-1234
```

CLI Options:

```bash
--folder (-f) # Image output folder [default='images']
--domain (-d) # Slack team domain [required]
--token (-t) # Slack API token [required]
```

CLI Example:

```bash
python main.py --folder=emojis --domain=SLACK-TEAM --token=AUTH-TOKEN
```
