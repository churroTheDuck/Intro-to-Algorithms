import os
import time
import pandas as pd

# pages = []

class Page:
    def __init__(self, id, name, pageRank):
        self.id = id
        self.name = name
        self.links = []
        self.backlinks = []
        self.pageRank = pageRank
    def add_link(self, target_page_id):
        if (target_page_id != self.id):
            self.links.append(target_page_id)
            pagesDict[target_page_id].add_back_link(self.id)
    def add_back_link(self, target_page_id):
        self.backlinks.append(target_page_id)
    def print_links(self):
        for page in self.links:
            print (pagesDict[page].name + ", ")
    def print_backlinks(self):
        for page in self.backlinks:
            print (pagesDict[page].name + ", ")
    def print_name(self):
        print(self.name)
    def __repr__(self):
        return f"Page (id: {self.id}, name: {self.name}, links: {self.links})"
d = 0.85
def pageRank(iteration):
    #print(f"Iteration {iteration + 1}")
    newRanks = {}
    for id in pagesDict:
        newPageRank = 0
        for backlink in pagesDict[id].backlinks:
             newPageRank += pagesDict[backlink].pageRank / len(pagesDict[backlink].links)
        newRanks[id] = (1 - d) / pageNumber + d * newPageRank
    for id in pagesDict:
        pagesDict[id].pageRank = newRanks[id]
        #print(f"Name: {pagesDict[id].name}, Rank: {pagesDict[id].pageRank}")
    #term_size = os.get_terminal_size()
    #print('=' * term_size.columns)

df = pd.read_csv("pagerank_wiki_data.csv", sep="\t")

pagesDict = {}
pageNumber = 0
countingPages = []

for _, row in df.iterrows():
    if (row["page_id_from"] not in pagesDict):
        countingPages.append(row["page_id_from"])
for _, row in df.iterrows():
    if row["page_id_to"] not in pagesDict:
        countingPages.append(row["page_id_to"])
#counting
pageNumber = len(countingPages)
        
for _, row in df.iterrows():
    if (row["page_id_from"] not in pagesDict):
        pagesDict[row["page_id_from"]] = Page(row["page_id_from"], row["page_title_from"], 1 / pageNumber)
# first pass creates Pages

for _, row in df.iterrows():
    if row["page_id_to"] not in pagesDict:
        pagesDict[row["page_id_to"]] = Page(row["page_id_to"], row.get("page_title_to", str(row["page_id_to"])), 1 / pageNumber)
    pagesDict[row["page_id_from"]].add_link(row["page_id_to"])
# second pass adds links between the Pages
# additionally, any pages that are linked to, but do not have a source, are created.

start = time.time()
for i in range(10):
    pageRank(i)

# coded with ai and Jake
with open("out.txt", "w+") as f:
    a = ""
    for id, page in sorted(pagesDict.items(), key=lambda item: item[1].pageRank, reverse=True):
        a += f"Name: {page.name}, Rank: {page.pageRank}" + "\n"
    f.write(a)
# end ai section

end = time.time()
print(f"End - Start = {end - start} seconds")