import os
import eventsWatcher
from indexers import indexerV2, indexerV3

datalake_path = "/Users/alejandroalemanaleman/Downloads/datalake_test"
datamart_path = "/Users/alejandroalemanaleman/Downloads/datamart_test"

if not os.path.exists(datalake_path):
    os.mkdir(datalake_path)

eventsWatcher.watch_directory(datalake_path, datamart_path, indexerV2.inverted_index)
#eventsWatcher.watch_directory(datalake_path, datamart_path, indexerV3.inverted_index)