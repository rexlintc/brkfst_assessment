# Social Media Influence Network

## Project Overview
This project aims to build two social media tools that can help with social media marketing. The first tool is building a network graph to identify influential users, communiities, and viral content. The second tool is building a content virality predictor.

## Part 1. Network Graph

In order to build a network graph that allows users to identify influential users, communities, and viral content, we will need relevant data to be able to glean those insights. There are several ways to identify influential users, but one of the most straightforward ways is how much reach does this user have. Reach can be observed in a network graph by the number of connections a user has. Communities can be observed in a network graph by proximity or how related nodes are with each other. Depending on what kind of data we gather, we can use clustering algorithms to identify different communities and groups within the network. Lastly viral content can potentially be gleaned from a network graph by observing whether content is relevant to clusters of influential users or communities.

Data required for network graph
1. Reach: Follower/following relationship
2. Account proximity: user traits/characteristics e.g. (common language, geography, time zone, etc.)
3. Hashtags: to identify content clusters among users

### Data Collection
My initial approach was to build an web scraper that can scrape social media data. However, I soon ran into challenges with social media platforms preventing automated access and data scraping through security measures such as online challenges that prove you are a human. Then I transitioned to gathering datasets that are already scraped by others and uploaded to Kaggle for public use. However, most of the data are not relevant for our use case and are often stale. Lastly, I found a useful tool called [gallery-dl](https://github.com/mikf/gallery-dl) that can scrape data from instagram without being blocked. By using a combination of data scraped from Wikipedia and this tool, I was able to scrap most recent 5 posts from the [top 50 instagram accounts](https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts).

## Part 2. Virality Predictor

The goal is to build a virality predictor for social media content. A model or system of models that is able to predict whether a post will become viral before it is actually viral. It can be a tool used to evaluate marketing campaigns that can help select potentially viral content to release.

### Success (Viral) Criteria

The first step in building this system is establishing the criteria and qualities of a viral posts. Here I will list a few examples but the exact criteria can be tweaked and optimized based on the client's priorities.

## Criterion of a viral post

Note that time is an important factor to viral posts. All of the standard engagement metrics below need to be factored by time to transform the metrics to be velocity based.

- Views over time
- Likes over time
- Comments over time
- Shares over time

## Qualities of a viral post

- Content sentiment
We need to gather insights on what kind of emotions and sentiment do viral content illicit. We should keep in mind that triggering content, such as violence and hate speech, often becomes viral but is not necessarily good. The system should have models in place that ensures the content is validated and aligns with the intentions and requirements determined by the client.
- Content quality
While this can be considered the standard and there are also often exceptions, viral content should have good quality in terms of photography and videography principles.
- Reach
A post can be viral within a specific region, but certain posts can become viral across multiple regions. Depending on the clients' needs, we can determine the qualities of viral posts specific to regions or qualities of viral posts that are global or multi region.

## Data Collection

### Label Data & Training Data

Given the metrics above, we need to collect data on viral posts in history to be used as both our label and training data.

I attempted to build my own scraper by building an AI agent but I ran out ot HuggingFace API credits so I decided to download datasets from Kaggle to start.

There are several options available on Kaggle but not all of them fit the use case and some of them are outdated.
