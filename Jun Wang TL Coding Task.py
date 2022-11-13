## Jun Wang TL Coding Exercise 2022/11/12
%pip install warcio
from warcio.archiveiterator import ArchiveIterator
import requests
import sys

covid = ['covid', 'covid-19', '2019-ncov','pandemic'] ## Keywords for searching
economy = ['economic', 'economy', 'stock', 'stocks', 'market','markets', 'money','finance','financial',
'business', 'businesses'] 
 ## Keywords for searching
pages = []   ##output list


entries = 0
## total webpages in search space
matching_entries = 0
## number of relevant webpages


archive = ["https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-05/warc.paths.gz", 
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-10/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-16/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-24/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-29/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-34/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-40/warc.paths.gz",
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-45/warc.paths.gz"
"https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-50/warc.paths.gz"]
## List of crawls from January 2020 to December 2020

for file_name in archive:
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    stream = None
    if file_name.startswith("http://") or file_name.startswith("https://"):
        stream = requests.get(file_name, stream=True).raw
    else:
        stream = open(file_name, "rb")

    for record in ArchiveIterator(stream):
        if record.rec_type == "warcinfo":
            continue

        if not ".com/" in record.rec_headers.get_header("WARC-Target-URI"):
            continue

        entries += 1
        contents = (record.content_stream().read().decode("utf-8", "replace"))
        ## extract text from webpage as string
        contents = contents.lower()
        ## use case-insensitive search
        covid_rel = False
        economy_rel = False
        for word in covid:
            if word in contents:
                covid_rel = True
                break
        ## search for covid keywords in webpage
        for word in economy:
            if word in contents:
                economy_rel = True
                break
        ## search for economy keywords in webpage
        rel = covid_rel and economy_rel
        ## webpages referring both to Covid and the economy are considered relevant
        if rel == True:
            matching_entries += 1
            pages.append(str(record.rec_headers.get_header("WARC-Target-URI")))
        ## append url to output list if webpage is relevant
        if matching_entries > 200:
            break
        ## Set quota of 200 matching pages to each of 9 crawls
        ## to control runtime


print ('There are ', matching_entries, ' related pages out of ', entries, ' searches.')
print (pages)
