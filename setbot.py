#Welcome to setbot, a tool to parse mtg set symbols for user flair on reddit
from pyquery import PyQuery as pq
from lxml import html
import requests
import praw
import urllib

URL = "https://magic.wizards.com/en/products/card-set-archive"

def main():

    session_requests = requests.session()

# Scrape rank data from navbar span
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    set_list = tree.xpath('//*[string-length(@id) = 3]/div/ul/li[2]/a/span[2]')

    # Dunno the syntax for the tool you're using
    # But internally all HTML elements are HTML Nodes
    # So basically
    # groups = getAllNodes('.card-set-archive-table')
    # for group in groups
    #     sets = group.getAllNodes('li.modern-format')
    #     for set in sets
    #         imageNode = set.getAllNodes('.icon img')
    #         imageUrl = imageNode.src
    #         downloadImage(imageUrl)

    print "%s" % set_list


if __name__ == '__main__':
    main()
