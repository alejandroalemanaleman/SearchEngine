import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# Handler que reacciona ante la creación de un nuevo archivo
class NewFileHandler(FileSystemEventHandler):
    def __init__(self, datamartPath, indexerFunction):
        self.indexerFunction = indexerFunction
        self.datamartPath = datamartPath

    def on_created(self, event):
        # Verifica si el evento es para un archivo y no para un directorio
        if not event.is_directory:
            bookDatalakePath = event.src_path
            self.indexerFunction(bookDatalakePath, self.datamartPath)
            print(bookDatalakePath)
            print(f"libro procesado {bookDatalakePath}")


# Función que observará el directorio
def watch_directory(inputPath, outputPath, indexerFunction):
    event_handler = NewFileHandler(outputPath, indexerFunction)  # Pasamos el callback al manejador
    observer = Observer()
    observer.schedule(event_handler, path=inputPath, recursive=False)

    observer.start()
    print(f"Observando el directorio: {inputPath}")

    try:
        while True:
            time.sleep(1)  # Mantiene el script en ejecución
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
