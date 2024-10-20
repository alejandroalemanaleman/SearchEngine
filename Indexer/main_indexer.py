import os
import eventsWatcher
from indexers import indexerV2, indexerV3

datalake_path = "/datalake"
datamart_path = "/datamart"

if not os.path.exists(datalake_path):
    os.mkdir(datalake_path)

eventsWatcher.watch_directory(datalake_path, datamart_path, indexerV2.inverted_index)
#eventsWatcher.watch_directory(datalake_path, datamart_path, indexerV3.inverted_index)