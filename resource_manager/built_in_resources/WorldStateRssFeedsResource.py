"""
Credit https://github.com/daveshap/ACE_WorldState/ for core logic of this resource.
"""

from resource_manager.Resource import Resource

import glob
import time
import re
import feedparser
import yaml
import email.utils
from pathlib import Path
import os
import random


class WorldStateRssFeedsResource(Resource):
    """
    Q: What does this resource provide?
    A: A list of world news result objects, each result has a title, summary, source, link and publish date. The
    results are also saved as .yaml files in the class's storage area.

    Q: What is this resource for?
    A: This resource enables layers to get a quick high level overview of the current world state from the
    perspective of several popular RSS feeds.

    Q: How might this resource be extended?
    A: A more diverse set of RSS news sources could be added, it could be made easier to query by date etc.
    Currently, it is a snapshot in time. The resource could be paired with longer term memory if that fits the use case.
    """
    def __init__(self):
        super().__init__(name="WorldStateRssFeedsResource",
                         description="Gets RSS news feeds, returns results, can be queried with keyword and/or date.")

        self.yaml_files = None  # folder created by get_rss_feeds, property assigned by query_rss_feeds.

        self.feeds = ['http://feeds.bbci.co.uk/news/rss.xml',
                      'http://feeds.reuters.com/reuters/technologyNews']

    def execute(self):
        self.get_rss_feeds()
        self.query_rss_feeds()

    def get_rss_feeds(self):

        # Fetch and parse each feed
        for url in self.feeds:
            feed = feedparser.parse(url)

            # Process each news item in the feed
            for item in feed.entries:
                # Parse the published date to a datetime object
                pub_date = email.utils.parsedate_to_datetime(item.published)

                # Create a dictionary with the relevant information
                entry = {
                    'timestamp': int(time.time()),
                    'source': url,
                    'published': pub_date.strftime('%Y-%m-%d'),
                    'link': item.link,
                    'title': item.title,
                    'summary': item.summary
                }

                # Clean the title to remove unsafe characters
                safe_title = re.sub('[^a-zA-Z0-9 \n\.]', '', item.title)
                safe_title = safe_title.replace(' ', '_')[:50]  # Replace spaces with underscores and limit length

                # Generate a unique filename based on the cleaned title
                filename = f"rss_{pub_date.strftime('%Y-%m-%d')}_{safe_title}.yaml"

                # Ensure the directory exists before attempting to write to it
                directory = Path(f'{self.storage_root}/data')
                os.makedirs(directory, exist_ok=True)  # this line creates the directory if it doesn't exist

                # Check if file already exists, skip if it does
                if not (directory / filename).exists():
                    # Save the news item to a YAML file
                    with open(directory / filename, 'w') as file:
                        yaml.dump(entry, file)

    def query_rss_feeds(self, keyword=None, date=None):
        keyword = keyword
        date = date

        self.yaml_files = glob.glob(f"{self.storage_root}/data/*.yaml")
        results = []

        # Search each file
        for filename in self.yaml_files:
            with open(filename, 'r') as file:
                entry = yaml.safe_load(file)

                # If a date was provided, skip entries from other dates
                if date and entry['published'] != date:
                    continue

                # If a keyword was provided, skip entries that don't contain the keyword
                if keyword and keyword.lower() not in entry['title'].lower() and keyword.lower() not in entry[
                    'summary'].lower():
                    continue

                results.append(entry)

        self.logger.debug(f"Query with [keyword: {keyword}, date: {date}] returned {len(results)} results")
        self.logger.debug(f"Sample Result: {random.choice(results)['title']}")

        return {'results': results}


if __name__ == "__main__":
    WSRF = WorldStateRssFeedsResource()
    WSRF.execute()
