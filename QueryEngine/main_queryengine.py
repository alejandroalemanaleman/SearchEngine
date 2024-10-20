import queryEngine_V2, queryEngine_V3

words_path = "/datamart/words"
metadata_path2 = "/datamart/metadatos/metadatos"
metadata_path3 = "/datamart/metadatos"
datalake_path = "/datalake"

queryEngine_V2.execute(words_path, metadata_path2, datalake_path)
#queryEngine_V3.execute(words_path, metadata_path3, datalake_path)