import queryEngine_V2, queryEngine_V3

words_path2 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V2/datamart/words"
words_path3 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V3/datamart/words"
metadata_path2 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V2/datamart/metadatos/metadatos"
metadata_path3 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V3/datamart/metadatos"
datalake_path2 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V2/datalake"
datalake_path3 = "/Users/alejandroalemanaleman/Downloads/PROJECT_DATA/V3/datalake"

#queryEngine_V2.execute(words_path2, metadata_path2, datalake_path2)
queryEngine_V3.execute(words_path3, metadata_path3, datalake_path3)