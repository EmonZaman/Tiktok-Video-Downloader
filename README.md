# Tiktok Video Downloader API


### Prerequisites

- Python 3.8 or higher
- Flask
- Requests

### Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/EmonZaman/Tiktok-Video-Downloader.git
   ```

2. **Install Dependencies**:
    Navigate to the project directory and install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Run the application with the following command:

```bash
python app.py
```

The Flask server will start at http://127.0.0.1:5000/.


### Using the API
#### Endpoint: Get Video Links

- URL: /get_video_link
- Method: GET
- tiktok_url Params:
    - Required: tiktok_url=[string] (The Tiktok video URL)

### Testing the Endpoint
#### Via Web Browser

To test the endpoint via a web browser, simply navigate to the following URL (replace <tiktok_Video_URL> with the actual Facebook video URL):

```bash
http://127.0.0.1:5000/get_video_link?tiktok_url=<Tiktok_Video_URL>
```

For example:

```bash
http://127.0.0.1:5000/get_video_link?tiktok_url=https://www.tiktok.com/@jbiebsss/video/7324465895651183905?is_from_webapp=1&sender_device=pc&web_id=7322476429475022354

#### Via cURL

You can also use cURL in your command line:

```bash
curl "http://127.0.0.1:5000/get_video_link?tiktok_url=https://www.tiktok.com/@jbiebsss/video/7324465895651183905?is_from_webapp=1&sender_device=pc&web_id=7322476429475022354"
```

#### Via Postman

1. Open Postman: Launch the Postman application on your computer.

2. Create a New Request:
    - Click on the 'New' button or '+' tab to start a new request. Set the request method to GET by selecting it from the dropdown menu next to the URL input field.

3. Enter the URL:
    - In the URL input field, enter: http://127.0.0.1:5000/get_video_link

4. Add Query Parameters:
    - Below the URL input field, locate the section for entering query parameters.
    - In the `Key` field, enter `tiktok_url`.
    - In the `Value` field, enter the tiktok video URL. For example: https://www.tiktok.com/@jbiebsss/video/7324465895651183905?is_from_webapp=1&sender_device=pc&web_id=7322476429475022354

5. Send the Request:
    - Click the 'Send' button to execute the request.

6. View the Response:
    - The response will be displayed in the lower section of the Postman interface.
    - If successful, you should see a JSON response with the video title and download links.

Here's an illustration of what your Postman setup might look like:

- Method: GET
- URL: http://127.0.0.1:5000/get_video_link
- Query Params:
    - Key: `tiktok_url`
    - Value: https://www.tiktok.com/@jbiebsss/video/7324465895651183905?is_from_webapp=1&sender_device=pc&web_id=7322476429475022354
#### Sample Response:

The API responds with a JSON object containing the title of the video and download links:

```bash
{
    "video_link": "https://v19.tiktokcdn-us.com/8bfc481dd20ea625ff0794913705c147/65b443cf/video/tos/useast8/tos-useast8-ve-0068c004-tx2/o8NIAErgRu8QlAffOAgZb3JBHNnDEBF7VqvEgQ/?a=1233&ch=0&cr=13&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=930&bt=465&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&cs=0&ds=6&ft=4KLxRMzm8Zmo0HGi094jV_gEoKFrKsd.&mime_type=video_mp4&qs=0&rc=PDg4ZjVmNjxlOmc8ZGc7OEBpMzlyam85cmhxbzMzaTczNEAtNmEvYGNeNTIxNDQwLy8uYSNsZHNuMmRza2dgLS1kMTJzcw%3D%3D&l=2024012617422168AF9E3FF5E36713F922&btag=e00090000"
}
```


### Important Notice

#### Warning: This API cannot retrieve download links for private videos on tiktok. It only works with videos that are publicly accessible. If you attempt to fetch links for a private video, the API will not be able to retrieve the necessary data and will return an error message.

Always ensure that the URL provided is for a public tiktok video. This limitation is due to privacy restrictions on Facebook's platform.

### Troubleshooting

- Ensure that the provided URL is a valid tiktok video URL (e.g., https://www.tiktok.com/@jbiebsss/video/7324465895651183905?is_from_webapp=1&sender_device=pc&web_id=7322476429475022354).
- Check if the Flask server is running and accessible.
