# TikTok Scraper

A Python-based scraper for gathering TikTok videos and their metadata.

## Features
- Scrape TikTok videos and metadata
- Support for user profiles and hashtags
- Asynchronous downloading for better performance
- Export data to CSV format

## Setup
1. Install Python 3.8 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install Playwright browsers:
```bash
playwright install
```

## Usage
```python
from src.tiktok_scraper import TikTokScraper

scraper = TikTokScraper()
# Scrape user profile
results = scraper.scrape_user("username")
# Scrape hashtag
results = scraper.scrape_hashtag("hashtag")
```

## Note
Please be mindful of TikTok's terms of service and rate limiting when using this scraper. 