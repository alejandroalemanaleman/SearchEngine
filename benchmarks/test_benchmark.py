from queryEngine_V3 import execute

def test_benchmark_words_search(benchmark):
    words_path = "/Users/alejandroalemanaleman/Downloads/datamart_test/words"
    metadata2 = "/Users/alejandroalemanaleman/Downloads/datamart_test/metadatos/metadatos"
    metadata3 = "/Users/alejandroalemanaleman/Downloads/datamart_test/metadatos"
    datalake_path = "/Users/alejandroalemanaleman/Downloads/datalake_test"

    benchmark(execute, words_path, metadata3, datalake_path, "produced")
