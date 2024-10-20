import queryEngine_V2, queryEngine_V3

words_path = "/Users/alejandroalemanaleman/Downloads/datamart_test/words"
metadata_path2 = "/Users/alejandroalemanaleman/Downloads/datamart_test/metadatos/metadatos"
metadata_path3 = "/Users/alejandroalemanaleman/Downloads/datamart_test/metadatos"
datalake_path = "/Users/alejandroalemanaleman/Downloads/datalake_test"

queryEngine_V2.execute(words_path, metadata_path2, datalake_path)
#queryEngine_V3.execute(words_path, metadata_path3, datalake_path)