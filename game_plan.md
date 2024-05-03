Author Network From DBLP Dataset

Desc: A network of ESTABLISHED authors in our dataset where each node is an
author which is in the top 20 cited authors of the top 20 fields in the
network, node size is determined by degree centrality, color is determined by
additonal field (field listed after computer science). Edges are directional
and represent an author citing another author, thickness is determined by
amount of citations towards that author.

Step 1: Retrieve top 20 authors in each of the top 20 fields with following code
```python
"""
This code creates a dictionary of the top 20 authors of each field in the DF.
Key = field name
Val = list of tuples w/ author name && citation counts
"""

exploded_df = citations_df.explode("Field of Study")
grouped = exploded_df.groupby("Field of Study")

top_influential_figures = {}

for field, group in grouped:
    author_citations = {}

    for index, row in group.iterrows():
        authors = row["Authors"].split(", ")
        for author in authors:
            author_citations[author] = author_citations.get(author, 0) + row["Citations"]

    sorted_authors = sorted(author_citations.items(), key=lambda x: x[1], reverse=True)
    top_influential_figures[field] = sorted_authors[:20]
```

With this dictionary, and a list of the top fields, we can trim this dictionary 
to only the top 20 fields in the dataset, from there, we can loop through the
dictionary and do the following:

for each field:
    get list of top authors
    for each author in top authors:
        create a list of each paper from author in dataset
        for each paper in paper list:
            grab each paper in the references section, and add list of authors current authors cited author list
        drop any duplicates in list

