from bs4 import BeautifulSoup
import aiohttp
import io
# Define a class named 'NEWS'.
class NEWS:
    # Constructor for the NEWS class. Currently, it does nothing.
    def __init__(self) -> None:
        pass

    # Asynchronous method 'get_async' to fetch news data.
    async def get_async(self) -> str:
        # Start an asynchronous HTTP session.
        async with aiohttp.ClientSession() as session:
            # Asynchronously request the webpage of Telegram's blog.
            async with session.get("https://telegram.org/blog") as response:
                # If the response status is not 200 (OK), raise an exception.
                if response.status != 200:
                    raise Exception("ERROR")

                # Read the response text (HTML content).
                html = await response.text()
                # Parse the HTML content using BeautifulSoup.
                soup = BeautifulSoup(html, "lxml")

                # Extract specific information from the parsed HTML.
                title = soup.find(class_='dev_blog_card_title').text
                lead = soup.find(class_='dev_blog_card_lead').text
                date = soup.find(class_='dev_blog_card_date').text
                url = "https://telegram.org" + soup.find(class_='dev_blog_card_link_wrap').get("href")

        # Start another asynchronous HTTP session to get the image URL.
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception("ERROR")

                html = await response.text()
                soup = BeautifulSoup(html, "lxml")

                # Extract the image URL.
                image_url = "https://telegram.org" + soup.find(class_="blog_wide_image").find('a').get("href")
                
        # Return the extracted data as a list.
        return [title, lead, date, url, image_url]

    # Asynchronous method 'download_photo' to download a photo from a URL.
    async def download_photo(self, url: str) -> io.BytesIO:
        # Start an asynchronous HTTP session.
        async with aiohttp.ClientSession() as session:
            # Asynchronously request the image URL.
            async with session.get(url) as response:
                # If the response status is not 200 (OK), raise an exception.
                if response.status != 200:
                    raise Exception("ERROR")

                # Read the binary data of the response (the image).
                data = await response.read()
                # Convert the binary data into a BytesIO object.
                photo_io = io.BytesIO(data)
                # Name the BytesIO object, mimicking a file.
                photo_io.name = 'photo.jpg'

                # Return the BytesIO object.
                return photo_io
