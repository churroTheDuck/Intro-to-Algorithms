pages = []

class Page:
    def __init__(self, name, pageRank):
        self.name = name
        self.links = []
        self.backlinks = []
        self.pageRank = pageRank
    def add_link(self, target_page):
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
def pageRank():
    print("Ranking pages...")
    newRanks = {}
    for page in pages:
        newPageRank = 0
        for backlink in page.backlinks:
             newPageRank += backlink.pageRank / len(backlink.links)
        newRanks[page] = (1 - d) + d * newPageRank
    for page in pages:
        page.pageRank = newRanks[page]
        print(f"Name: {page.name}, Rank: {page.pageRank}")

n = 4

page0 = Page("0.com", 1 / n)
page1 = Page("1.com", 1 / n)
page2 = Page("2.com", 1 / n)
page3 = Page("3.com", 1 / n)

page1.add_link(page0)
page2.add_link(page0)
page3.add_link(page0)

pages.append(page0)
pages.append(page1)
pages.append(page2)
pages.append(page3)

for i in range(20):
    pageRank()