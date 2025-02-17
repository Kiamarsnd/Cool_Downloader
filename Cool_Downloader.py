import requests
from tqdm import tqdm
import os

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    if response.status_code == 200:
        with open(save_path, 'wb') as file, tqdm(
            desc=f"Downloading {os.path.basename(save_path)}",
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))
        return True
    else:
        return False

def main():
    while True:
        print("""
        *****************************************
        *   Cool Downloader --- By KiNG_CYReX   *
        *****************************************
        """)
        url = input("Please Enter The Download Llink: ")
        save_path = input("Please Enter The Save Path: ")

        success = download_file(url, save_path)

        if success:
            print("Download Completed Successfully.")
        else:
            print("Download Failed. There Was An Eerror During The Download.")

        restart = input("Do You Want To Perform Another Download? (yes/no): ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
