---
name: get-cat-image
description: Get random image url. You can use it to get url for cover image, sample image, or test image from 'The Cat API'.
tags:
  - skill
cover: https://cdn2.thecatapi.com/images/cj9.jpg
env:
  - CAT_API_KEY
---
# When to use
- To get sample image.
- To be funny.
- To generate image of cats.

# What is 'The Cat API'?
'The Cat API' is a free API that provides random images of cats.
You can setup easily and get images of cats by using this API.
**reference:** [The Cat API Documentation](https://thecatapi.com/)

# Setup
1. Sign up for an account on [The Cat API](https://thecatapi.com/signup).
2. Input your email and other required information, then click "SUBMIT".
3. You will receive an email with your API key.
4. Copy the API key and set it as an environment variable named `CAT_API_KEY`.

# Getting Started
1. Get API Key from environment variable `CAT_API_KEY`.
2. You can get image of cats by GET request to URL: `https://api.thecatapi.com/v1/images/search?api_key=${CAT_API_KEY}`.
3. The response will be a JSON object containing the URL of the cat image. example:
```json
[
  {
    "breeds": [],
    "id": "cj9",
    "url": "https://cdn2.thecatapi.com/images/cj9.jpg",
    "width": 440,
    "height": 341
  }
]
```
4. You can use the 'url' field to display the cat image in your application or website.

# Extensions
- You can adjust th size of the image by adding `size` parameter to the request URL.
  - `size=thumb` for thumbnail images (200px on the longest side)
  - `size=small` for small images (400px on the longest side)
  - `size=med` for medium images (800px on the longest side)
  - `size=full` for full-size images (original size)

- You can get multiple images at once by adding `limit` parameter to the request URL.
  - `limit=5` to get 5 images at once.

# Workflow
- You can get image with a height of 400px or less for cover metadata of your note by flow like this:
  1. Get image url of cats by GET request to URL: `https://api.thecatapi.com/v1/images/search?api_key=${CAT_API_KEY}&size=small&limit=5`.
  2. Choose one with a height of 400px or less from the response and set it as cover metadata of your note.