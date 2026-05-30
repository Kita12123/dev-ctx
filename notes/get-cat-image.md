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

# Setup
1. Sign up for an account on [The Cat API](https://thecatapi.com/signup).
2. Input your email and other required information, then click "SUBMIT".
3. You will receive an email with your API key.
4. Copy the API key and set it as an environment variable named `CAT_API_KEY`.

# Getting Started
1. Get API Key from environment variable `CAT_API_KEY`.
2. You can get image of cats by GET request to this [URL](https://api.thecatapi.com/v1/images/search?api_key=${CAT_API_KEY}).
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
