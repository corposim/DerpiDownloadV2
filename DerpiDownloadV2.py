#!/usr/bin/env python3
import requests, gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def downloadImages(button):
    search = builder.get_object("TagsEntry").get_text()
    pages = builder.get_object("PagesEntry").get_text()
    key = builder.get_object("ApiEntry").get_text()
    for page in range(int(pages)+1):
        url = "https://derpibooru.org/search.json?q={}&page={}&key={}".format(search, page, key)
        r = requests.get(url)
        results = r.json()
        for image in results['search']:
            filename = str(image['id']) + '.' + image['original_format']
            print(filename)
            file = requests.get("https:" + image['image'])
            with open("images/" + filename, 'wb') as fd:
                for chunk in file.iter_content(chunk_size=128):
                    fd.write(chunk)

handlers = {
    "onDestroy": Gtk.main_quit,
    "onButtonPressed": downloadImages
}

builder = Gtk.Builder()
builder.add_from_file("DerpiDownloaderV2.glade")
builder.connect_signals(handlers)
builder.get_objects()

window = builder.get_object("window1")
window.show_all()

Gtk.main()

builder = Gtk.Builder()
builder.add_from_file("DerpiDownloaderV2.glade")
