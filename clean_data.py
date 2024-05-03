from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile 
from ijson import items

import pandas as pd
import numpy as np
import os

# Setup Kaggle API To Stream Dataset
api = KaggleApi()
api.authenticate()

# Initialize Lists To Store Data
# ids, titles, years, n_citations, doc_types, authors_list, venues, fos = [], [], [], [], [], [], [], []
refs = []

# DEBUG Stop Processing Objects After X Objects
IS_MAX_OBJECTS_ON = False
NUM_MAX_OBJECTS= 100000

# Grab Dataset and Place In CWD
if not (os.path.isfile("./citation-network-dataset.zip")):
    api.dataset_download_files('mathurinache/citation-network-dataset')
data_zf = ZipFile('citation-network-dataset.zip', 'r')


# Takes Values From JSON Entry and Appends Them To Colums
def process_json_obj(obj):
    #ids.append(obj.get('id'))
    #titles.append(' '.join(obj.get('title').split()))
    #years.append(obj.get('year'))
    #n_citations.append(obj.get('n_citation'))
    #doc_types.append(obj.get('doc_type'))
    #authors_names = ", ".join([author.get('name') for author in obj.get('authors', [])])
    #authors_list.append(authors_names)
    #venues.append(obj.get('venue', {}).get('raw', ''))
    refs.append(', '.join(map(str, obj.get("references", []))))
    


print("Making columns FROM JSON Data...")
# Create Columns From JSON Data
with data_zf:
    with data_zf.open('dblp.v12.json') as json:
        objects = items(json, 'item')
        for i, obj, in enumerate(objects):
            # DEBUG
            if IS_MAX_OBJECTS_ON and i >= NUM_MAX_OBJECTS - 1:
                break
            if obj.get('n_citation') >= 1:
                process_json_obj(obj)

print("Creating Dataframe from Columns...")
# Create a DataFrame From Our Columns
citations_df = pd.DataFrame({
    #'ID': ids,
    #'Title': titles,
    #'Year': years,
    #'Citations': n_citations,
    #'Document Type': doc_types,
    #'Authors': authors_list,
    #'Venue': venues,
    #'Field of Study': fos
    "References": refs,
})

print("Making CSV...")
with open("indexed_data.csv", "x") as csv:
  csv.write(citations_df.to_csv(index=False))

print("Finished making the CSV!")