def download_file_from_google_drive(file_id: str, destination: str):
    import requests
    """
    Downloads a file from Google Drive given its file ID and saves it to the specified destination.
    The file must be accessible to everyone with the link.
    Args:
        file_id (str): The Google Drive file ID.
        destination (str): The local path to save the downloaded file.
    """
    URL = "https://drive.usercontent.google.com/u/0/uc"
    params = {"id": file_id, "export": "download"}
    response = requests.get(URL, params=params, stream=True)
    response.raise_for_status()
    with open(destination, "wb") as f:
        print(f"Downloading file to {destination}")
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
        f.close()

if __name__ == "__main__":
    download_file_from_google_drive("1Np_RB7uvQxViHzGwzl0IK_XKz15UA-f8", "template.docx")