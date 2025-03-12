import asyncio
from tiktok_scraper import TikTokScraper

async def main():
    # Initialize the scraper
    scraper = TikTokScraper(download_path="downloaded_videos")
    
    # Example 1: Scrape videos from a user's profile
    print("Scraping user profile...")
    user_videos = scraper.scrape_user("tiktok", limit=5)  # Replace with any username
    scraper.save_metadata(user_videos, "user_videos_metadata.csv")
    
    # Download the videos
    print("Downloading user videos...")
    await scraper.download_videos(user_videos)
    
    # Example 2: Scrape videos from a hashtag
    print("\nScraping hashtag...")
    hashtag_videos = scraper.scrape_hashtag("python", limit=5)  # Replace with any hashtag
    scraper.save_metadata(hashtag_videos, "hashtag_videos_metadata.csv")
    
    # Download the videos
    print("Downloading hashtag videos...")
    await scraper.download_videos(hashtag_videos)

if __name__ == "__main__":
    asyncio.run(main()) 