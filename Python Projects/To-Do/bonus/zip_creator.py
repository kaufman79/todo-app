import zipfile
# pathlib will automatically create filepaths (by automatically concantonating) if you give it multiple strings using
# the .path() function.
# which is needed cause otherwise you have to write out the filepath but operating systems differ in their syntax of
# filepaths, with mac using backslash and PC using forward slash (IIRC)
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

# the below is just to test the function, which is a common thing to do I guess. It wont run unless you execute this
# file directly (instead of importing the function)

if __name__ == "__main__":
    make_archive(filepaths=["bonus3.py", "bonus2.1.py"], dest_dir="zipped_files")