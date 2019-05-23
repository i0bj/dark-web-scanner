#! /usr/bin/python

import sys
import time
import requests
import argparse


# Api rate limit is 30 queries per minute



def main():

    parser = argparse.ArgumentParser("This program will scan the dark web for specified content")

    parser.add_argument("-k", "--keyword", help="This will search for any search term ex: 'John Doe'")
    args = parser.parse_args()

    global keyword

    keyword = args.keyword

    # This will query the Dark Search API for information found on the dark web.
    api_prefix = "https://darksearch.io/api/search"
    query = {"query": keyword,
              "page": 1,
             }

    def tor_crawl():

        def update_progress(job_title, progress):
            length = 20 # modify this to change the length
            block = int(round(length*progress))
            msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
            if progress >= 1: msg += " DONE\r\n"
            sys.stdout.write(msg)
            sys.stdout.flush()

        for i in range(100):
            time.sleep(0.1)
            update_progress("Scanning DeepWeb for " + keyword, i/100.0)
        update_progress(keyword, 1)

        api_params = "{}".format(api_prefix)
        url_response = requests.get(api_params, params=query)
        # if url_response == 200:
        print(url_response.json())

    tor_crawl()


main()
