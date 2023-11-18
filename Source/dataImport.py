import urllib.request
import os
import zipfile

import config


def download_data():
    url = config.DATA_URL
    destination_file = os.path.join(config.INPUT_PATH, "data.zip")
    extract_to_folder = config.INPUT_PATH

    if os.path.exists(destination_file):
        print(f"The file is already downloaded.")
    else:
        print("Downloading Data ...")
        urllib.request.urlretrieve(url, destination_file)

    if os.path.exists(os.path.join(extract_to_folder, config.CSV_DATA_FILE)):
        print(f"The file is already unzipped.")
    else:
        print("unzipping Data File ...")
        with zipfile.ZipFile(destination_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to_folder)

    return
