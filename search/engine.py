



# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:29:19 2020

@author: a
"""


def get_page(url):
    try:
        import urllib.request
        seed = urllib.request.urlopen(url)
        page = (seed.read())
        page = str(page)
        return page
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    sayac = 10
    while tocrawl:
        page = tocrawl.pop()
        if sayac < 0:
            break
        if page not in crawled:
            sayac = sayac - 1
            content = get_page(page)
            outlinks = get_all_links(content)
            add_page_to_index(index, page, content)
            union(tocrawl, outlinks)
            graph[page] = outlinks
            crawled.append(page)
    return index, graph


def add_to_index(index, url, keyword):
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append(url)
        return
    index[keyword] = [url]


def add_page_to_index(index, url, content):
    for i in content.split():
        add_to_index(index, url, i)


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return []


def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


def quick_sort(pages, ranks):
    if len(pages) > 1:
        piv = ranks[pages[0]]
        i = 1
        j = 1
        for j in range(1, len(pages)):
            if ranks[pages[j]] > piv:
                pages[i], pages[j] = pages[j], pages[i]
                i += 1
        pages[i - 1], pages[0] = pages[0], pages[i - 1]
        quick_sort(pages[1:i], ranks)
        quick_sort(pages[i + 1:len(pages)], ranks)


def Look_up_new(index, ranks, keyword):
    pages = lookup(index, keyword)
    urls = []

    quick_sort(pages, ranks)

    for i in pages:
        urls.append(i)
    return urls

sonucbilgisi="dsfdsfsfdsf"
def final(site, keyword):
    index, graph = crawl_web(site)

    print(index)
    ranks = compute_ranks(graph)
    a = Look_up_new(index, ranks, keyword)
    sonucbilgisi = str(len(index)) + " tane sonuç arasından " + str(len(a)) + " tane eşleşme bulundu."
    print(sonucbilgisi)
    return a , sonucbilgisi


#site = input("lütfen site adresi giriniz:")
#keyword = input("lütfen kelim#eyi giriniz:")










