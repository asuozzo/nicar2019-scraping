# Web scraping with Python

Last updated March 10, 2019.

Authors:

- Geoff Hing
- Andrea Suozzo

## NICAR 2019 resources

- [Session repository](https://github.com/asuozzo/nicar2019-scraping)
- [Slides](https://docs.google.com/presentation/d/1WZmdW1lcXvo1gLQ_VanjWkCFTJVvu8T0md0is-2Sg60/edit)
- [Technical cheatsheet](https://github.com/asuozzo/nicar2019-scraping/blob/master/reference_cheatsheet.md)

## Before you scrape

- It's helpful to know [how the web and underlying protocols work](https://www.ire.org/events-and-training/event/3190/4173).
- Look at a sample of the pages. Make sure you look across years, jurisdictions.
- For heavily interactive pages, look at the requests being made using the "Network" tab of your browser's developer tools.
- Consider filing a public records request (you might get more fields).
- Search government data portals for the same data.
- Search GitHub to see if anyone has already written a scraper.
- Manually enter a few records to estimate time to do it manually.

## When to scrape

- You need the data repeatedly and you can imagine using it for multiple stories.
- There are too many records to enter by hand.
- Data is kept by an agency/jurisdiction where you know records requests will be slow or you might not get it.
- You have the time and want the programming practice.
- You want to demonstrate the value of your skills to the newsroom.

## Separate fetching of data and parsing

Benefits:

- Each program does one thing and is relatively simple.
- We can develop and test each parser separately.
- We don't have to repeat every network requests if we mess up one of our scripts.
- Scrape the highest priority information first, when you want to scrape more, the raw HTML is already downloaded.
- Use existing programs to handle parts of our job or run parts in parallel.
- Do tricky parts of the process manually.

[xargs](https://shapeshed.com/unix-xargs/), [GNU parallel](https://www.gnu.org/software/parallel/) and [GNU make](https://github.com/datamade/data-making-guidelines) can all be helpful for running your scraper on many URLs/files. 

## Useful Python libraries

[Requests](http://docs.python-requests.org/en/master/) is great for fetching data from the web.

[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) provides a Python interface for parsing HTML and navigating the document structure.

We've made a [technical cheatsheet](https://github.com/asuozzo/nicar2019-scraping/blob/master/reference_cheatsheet.md) for common command line, Python, Requests and Beautiful Soup uses. 

## Scraping challenges

### Automating complex interactions

If you need to automate complex interactions, like filling out JavaScript driven forms, in order to get the HTML you need to scrape, try [Selenium](https://www.seleniumhq.org/). There's a [Python package](https://selenium-python.readthedocs.io/index.html) for interacting with Selenium.

### Structuring large scraping jobs

[Scrapy](https://scrapy.org/) is a framework for organizing your scraping code. It also has facilities for parallelizing scraping, managing scraping processes and monitoring your scrapers.

It might be overkill for simple scrapers, but I would consider updating scrapers that need to run over time to use the framework.

## Other scraping tutorials

- [First web scraper](https://first-web-scraper.readthedocs.io/en/latest/)
- [fgregg/scraping-intro](https://github.com/fgregg/scraping-intro)
- [Automating the Boring Stuff, Chapter 11 - Web Scraping](https://automatetheboringstuff.com/chapter11/)
- [Web Scraping Reference: A Simple Cheat Sheet for Web Scraping with Python](https://blog.hartleybrody.com/web-scraping-cheat-sheet/)
- [Beautiful Soup 4 Cheatsheet](http://akul.me/blog/2016/beautifulsoup-cheatsheet/)

## Robots.txt references

- [A Beginners Guide to Robots.txt: Everything You Need to Know](https://www.semrush.com/blog/beginners-guide-robots-txt/)

## Other sites to practice scraping

- Simple table with links to follow: [Nuclear Reactor Units](https://www.nrc.gov/reactors/operating/list-power-reactor-units.html)
- Simple table with links + pagination/page url params: [FDA Warning Letters](https://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2018/default.htm)
- Simple site with tons of links (funky formatting on the question pages, tho): [J-archive](http://j-archive.com/)
- GET request w/ user agent headers & API key from browser inspection (returns JSON): [Airbnb](https://www.airbnb.com/)
- POST request w/ user agent headers & parameters (returns HTML): [Vermont Campaign Finance Filings](https://campaignfinance.sec.state.vt.us/Public/ViewFiledReports)
- Session/cookies: [ScrapeThisSite.com example](https://scrapethissite.com/pages/advanced/?gotcha=login)

