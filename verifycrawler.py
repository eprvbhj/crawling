import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare")
        print(result.markdown[:10000])  # Print first 500 characters

if __name__ == "__main__":
    asyncio.run(main())