import asyncio
import aiohttp

async def check_http3_support(url):
  """
  Checks if a URL supports HTTP/3.

  Args:
    url: The URL to check.

  Returns:
    A tuple of (url, supports_http3):
      - url: The original URL.
      - supports_http3: True if the URL supports HTTP/3, False otherwise.
  """
  try:
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as response:
        supports_http3 = response.headers.get("alt-svc") is not None
  except Exception:
    supports_http3 = False

  return url, supports_http3

async def main(url_list):
  """
  Checks a list of URLs for HTTP/3 support and generates a report.

  Args:
    url_list: A list of URLs to check.
  """
  results = await asyncio.gather(*[check_http3_support(url) for url in url_list])

  print("HTTP/3 Support Report:")
  print("-----------------------")
  for url, supports_http3 in results:
    status = "Supported" if supports_http3 else "Not Supported"
    print(f"{url}: {status}")

if __name__ == "__main__":
  url_list = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.instagram.com/",
    "https://twitter.com/",
    "https://www.amazon.com/",
    "https://www.bing.com/",
    "https://www.pinterest.com/",
    "https://www.yahoo.com/",
    "https://www.wikipedia.org/",
    "https://www.reddit.com/",
    "https://www.linkedin.com/",
    "https://www.tiktok.com/",
    "https://www.netflix.com/",
    "https://zoom.us/",
    "https://www.roblox.com/",
    "https://www.microsoft.com/en-us/",
    "https://www.msn.com/",
    "https://www.baidu.com/",
    "https://www.ebay.com/"
  ]

  asyncio.run(main(url_list))
