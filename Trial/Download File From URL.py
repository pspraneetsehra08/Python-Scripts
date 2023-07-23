import os
import requests

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image downloaded successfully: {save_path}")
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

def main():
    image_url = "https://example.com/image.jpg"  # Replace with the image URL you want to download
    save_location = "./downloaded_image.jpg"  # Replace with the desired path to save the image

    download_image(image_url, save_location)

if __name__ == "__main__":
    main()
