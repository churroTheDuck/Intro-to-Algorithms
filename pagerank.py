import os
import time

pages = []

class Page:
    def __init__(self, name, pageRank):
        self.name = name
        self.links = []
        self.backlinks = []
        self.pageRank = pageRank
    def add_link(self, target_page):
        if (target_page != self):
            self.links.append(target_page)
            target_page.add_back_link(self)
    def add_back_link(self, target_page):
        self.backlinks.append(target_page)
    def print_links(self):
        for page in self.links:
            print (page.name + ", ")
    def print_backlinks(self):
        for page in self.backlinks:
            print (page.name + ", ")
    def print_name(self):
        print(self.name)
d = 0.85
def pageRank(iteration):
    print(f"Iteration {iteration + 1}")
    newRanks = {}
    for page in pages:
        newPageRank = 0
        for backlink in page.backlinks:
             newPageRank += backlink.pageRank / len(backlink.links)
        newRanks[page] = (1 - d) / len(pages) + d * newPageRank
    for page in pages:
        page.pageRank = newRanks[page]
        print(f"Name: {page.name}, Rank: {page.pageRank:.2f}")
    term_size = os.get_terminal_size()
    print('=' * term_size.columns)

n = 5

page0 = Page("0.com", 1 / n)
page1 = Page("1.com", 1 / n)
page2 = Page("2.com", 1 / n)
page3 = Page("3.com", 1 / n)
supernode = Page("supernode", 1 / n)

page1.add_link(page0)
page2.add_link(page0)
page3.add_link(page0)

pages.append(page0)
pages.append(page1)
pages.append(page2)
pages.append(page3)
pages.append(supernode)

for page in pages:
    page.add_link(supernode)
for page in pages:
    supernode.add_link(page)

start = time.time()
for i in range(10**6):
    pageRank(i)
end = time.time()
print(f"End - Start = {end - start} seconds")