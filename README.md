# DerpiDownloadV2

A simple GUI for downloading images from Derpibooru, written in Python 3.6.

![screen shot of DerpiDownloader](https://puu.sh/Aw1ho/55aa3f3bc9.png)

Search goes into "tags"

"Pages" is how many pages (starting from page 1) to download. For example 1 will download the first page, and 5 will download pages 1-5, inclusive. 

"API key" is optional, and allows for the user to use their own filters and settings. Leaving blank will use the Default filter and download 15 images per page. Using your own API key will search using your currently active filter, and can download up to 50 images per page, depending on your settings. (Note that the downloader will not download hidden images, but will still download spoilered images). You can find your API key at https://derpibooru.org/users/edit and how many images are downloaded per page at https://derpibooru.org/settings under the Display tab. 

If you want to sort the search results, like by score, you can do so by adding `&sf=score` to the end of your search. For example, a search of "cute" will download the most recent images tagged with cute, and a search of "cute&sf=score" will download the highest scoring images tagged cute.

You can sort using `score`, `wilson`, `relevance`, `width`, `height`, `comments`, and `random`. You can also control the order by adding `&sd=desc` or `&sd=asc`.

## Installation

For now just git clone (or download zip and extract) into a directory and run DerpiDownloadV2.py. Make sure that you have an "images" directory alongside DerpiDownloadV2.py.

Requires Python 3 and the requests library. 
