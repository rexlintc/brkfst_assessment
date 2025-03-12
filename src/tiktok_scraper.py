import asyncio
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

import aiohttp
import pandas as pd
from playwright.sync_api import sync_playwright
from tqdm import tqdm


class TikTokScraper:
    def __init__(self, download_path: str = "downloads"):
        """Initialize TikTok scraper.
        
        Args:
            download_path (str): Path to save downloaded videos
        """
        self.download_path = download_path
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        os.makedirs(download_path, exist_ok=True)

    def scrape_user(self, username: str, limit: int = 10) -> List[Dict]:
        """Scrape videos from a user's profile.
        
        Args:
            username (str): TikTok username
            limit (int): Maximum number of videos to scrape
            
        Returns:
            List[Dict]: List of video metadata
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Navigate to user's profile
            page.goto(f"https://www.tiktok.com/@{username}")
            page.wait_for_load_state("networkidle")
            
            videos = []
            last_height = page.evaluate("document.documentElement.scrollHeight")
            
            with tqdm(total=limit, desc=f"Scraping @{username}'s videos") as pbar:
                while len(videos) < limit:
                    # Extract video information
                    new_videos = page.evaluate("""
                        () => {
                            const videos = document.querySelectorAll('div[data-e2e="user-post-item"]');
                            return Array.from(videos).map(video => {
                                const link = video.querySelector('a');
                                const desc = video.querySelector('div[data-e2e="user-post-item-desc"]');
                                return {
                                    url: link ? link.href : null,
                                    description: desc ? desc.innerText : null,
                                    timestamp: new Date().toISOString()
                                }
                            });
                        }
                    """)
                    
                    videos.extend([v for v in new_videos if v["url"] and v not in videos])
                    pbar.update(len(new_videos))
                    
                    # Scroll down
                    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
                    page.wait_for_timeout(1000)  # Wait for content to load
                    
                    new_height = page.evaluate("document.documentElement.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
            
            browser.close()
            return videos[:limit]

    async def download_video(self, video_url: str, output_path: str):
        """Download a TikTok video.
        
        Args:
            video_url (str): URL of the video
            output_path (str): Path to save the video
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(video_url, headers=self.headers) as response:
                if response.status == 200:
                    with open(output_path, 'wb') as f:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            f.write(chunk)

    def scrape_hashtag(self, hashtag: str, limit: int = 10) -> List[Dict]:
        """Scrape videos from a hashtag.
        
        Args:
            hashtag (str): Hashtag to scrape (without #)
            limit (int): Maximum number of videos to scrape
            
        Returns:
            List[Dict]: List of video metadata
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Navigate to hashtag page
            page.goto(f"https://www.tiktok.com/tag/{hashtag}")
            page.wait_for_load_state("networkidle")
            
            videos = []
            last_height = page.evaluate("document.documentElement.scrollHeight")
            
            with tqdm(total=limit, desc=f"Scraping #{hashtag} videos") as pbar:
                while len(videos) < limit:
                    # Extract video information
                    new_videos = page.evaluate("""
                        () => {
                            const videos = document.querySelectorAll('div[data-e2e="challenge-item"]');
                            return Array.from(videos).map(video => {
                                const link = video.querySelector('a');
                                const desc = video.querySelector('div[data-e2e="challenge-item-desc"]');
                                return {
                                    url: link ? link.href : null,
                                    description: desc ? desc.innerText : null,
                                    timestamp: new Date().toISOString()
                                }
                            });
                        }
                    """)
                    
                    videos.extend([v for v in new_videos if v["url"] and v not in videos])
                    pbar.update(len(new_videos))
                    
                    # Scroll down
                    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
                    page.wait_for_timeout(1000)  # Wait for content to load
                    
                    new_height = page.evaluate("document.documentElement.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
            
            browser.close()
            return videos[:limit]

    def save_metadata(self, metadata: List[Dict], filename: str):
        """Save metadata to CSV file.
        
        Args:
            metadata (List[Dict]): List of video metadata
            filename (str): Output filename
        """
        df = pd.DataFrame(metadata)
        df.to_csv(filename, index=False)
        print(f"Metadata saved to {filename}")

    async def download_videos(self, metadata: List[Dict]):
        """Download videos from metadata.
        
        Args:
            metadata (List[Dict]): List of video metadata
        """
        tasks = []
        for i, video in enumerate(metadata):
            if video["url"]:
                output_path = os.path.join(self.download_path, f"video_{i}.mp4")
                task = asyncio.create_task(self.download_video(video["url"], output_path))
                tasks.append(task)
        
        await asyncio.gather(*tasks) 