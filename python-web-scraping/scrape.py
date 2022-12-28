import pprint
import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(webpage.text, 'html.parser')

hn_links = soup.select('.titleline > a')
hn_subtext = soup.select('.subtext')


def sort_stories_by_votes(story_list):
    return sorted(story_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    stories = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # Only include stories that have 100 or more points
            if points > 99:
                stories.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(stories)


pprint.pprint(create_custom_hn(hn_links, hn_subtext))
