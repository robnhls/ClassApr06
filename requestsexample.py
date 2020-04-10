import requests

url = "https://raw.githubusercontent.com/robnhls/ClassApr06/master/materials/py3master_1.8.pdf"
file_name = "new_py3master.pdf"

with requests.get(url, stream=True) as response:
    response.raise_for_status()  # raise an error for a bad status
    with open(file_name, "wb") as out_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                out_file.write(chunk)
