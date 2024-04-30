import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    # we need to use a raw string (r prefix) lest the slash be interpreted as escape sequences
    extract_archive(r"C:\Users\kaufm\PycharmProjects\todo-app\Python Projects\To-Do\bonus\compressed.zip",
                    r"C:\Users\kaufm\PycharmProjects\todo-app\Python Projects\To-Do\bonus")
