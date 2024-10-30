import os
import eventsWatcher
from indexers import indexerV2, indexerV3

datalake_path2 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V2/datalake"
datamart_path2 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V2/datamart"

datalake_path3 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V3/datalake"
datamart_path3 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V3/datamart"

#if not os.path.exists(datalake_path2):
#    os.mkdir(datalake_path2)

if not os.path.exists(datalake_path3):
    os.mkdir(datalake_path3)

#eventsWatcher.watch_directory(datalake_path2, datamart_path2, indexerV2.inverted_index)
eventsWatcher.watch_directory(datalake_path3, datamart_path3, indexerV3.inverted_index)