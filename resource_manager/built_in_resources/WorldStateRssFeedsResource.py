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


class WorldStateRssFeedsResource(Resource):
    def __init__(self):
        super().__init__(name="WorldStateRssFeedsResource",
                         description="")

        self.storage_root = f"storage/{self.name}"
        self.files = glob.glob(f"{self.storage_root}/data/*.yaml")

        self.feeds = ['http://feeds.bbci.co.uk/news/rss.xml',
                      'http://feeds.reuters.com/reuters/technologyNews']

        self.get_rss_feeds()

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

                # Check if file already exists, skip if it does
                if not (Path(f'{self.storage_root}/data') / filename).exists():
                    # Save the news item to a YAML file
                    with open(Path(f'{self.storage_root}/data') / filename, 'w') as file:
                        yaml.dump(entry, file)

    def query_rss_feeds(self, keyword=None, date=None):
        keyword = keyword
        date = date

        results = []

        # Search each file
        for filename in self.files:
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

        return {'results': results}
