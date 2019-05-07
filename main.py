import argparse

from src.slackmoji import get_emojis, download_emojis

# CLI Args
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', '--folder', help="Image output folder", default='images')
parser.add_argument('-d', '--domain', help="Slack team domain", required=True)
parser.add_argument('-t', '--token', help="Slack API token", required=True)
args = parser.parse_args()

def main():
    emojis = get_emojis(args.domain, args.token)
    download_emojis(emojis, args.folder)

if __name__ == '__main__':
    main()
