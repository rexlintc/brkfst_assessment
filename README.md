# Social Media

## Overview

## Part 1. Network Graph

The goal is to build a network graph to identify influential users, communities, and viral content.

### Influential users

In a graph of user network, we can identify influential users through several ways.

1. Follower/following relationship
2. Mentions
3. Hashtags - can be used to identify communities

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
