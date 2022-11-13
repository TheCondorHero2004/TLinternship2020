# TLinternship2020
# Jun Wang

Firstly, I create two keyword lists for Covid-related topics and economic topics, respectively.

CommonCrawl offers 9 crawls from January 2020 to December 2020, each giving a stream of webpages. For the web
pages given in one crawl, I first extract the contents from that webpage as a content string. Then, I search for the
Covid-related and economics-related keywords in the content string. My search is case-insensitive, because cases do
not really matter here (it is simply a matter of personal habit whether someone writes "COVID-19" or "Covid-19"). If
a webpage contains both Covid-related keywords and economics-related keyword, we can assume that the webpage discusses
or is relevant to the economic impacts of Covid-19.

For each webpage determined to be relevant, I append the url of the webpage to the output list. After having found 200
relevant webpages in each crawl, I move on to the next crawl to control runtime and ensure even coverage of the entire
year of 2020.
