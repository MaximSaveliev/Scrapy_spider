import scrapy
import base64
import json
import requests
import time
import random

class ProxyspiderSpider(scrapy.Spider):
    name = "proxyspider"
    
    def __init__(self, *args, **kwargs):
        super(ProxyspiderSpider, self).__init__(*args, **kwargs)
        self.api_base_url = "https://test-rg8.ddns.net/api"
        self.user_id = "t_a5670348"
        self.all_proxies = []
        self.verified_proxies = [
            "cmgydimv:bp4yxis3zm6l@38.154.227.167:5868",
            "cmgydimv:bp4yxis3zm6l@198.23.239.134:6540",
            "cmgydimv:bp4yxis3zm6l@207.244.217.165:6712",
            "cmgydimv:bp4yxis3zm6l@107.172.163.27:6543",
            "cmgydimv:bp4yxis3zm6l@173.211.0.148:6641",
            "cmgydimv:bp4yxis3zm6l@167.160.180.203:6754",
            "cmgydimv:bp4yxis3zm6l@104.239.105.125:6655",
            "cmgydimv:bp4yxis3zm6l@154.36.110.199:6853",
            "cmgydimv:bp4yxis3zm6l@45.151.162.198:6600",
            "cmgydimv:bp4yxis3zm6l@206.41.172.74:6634",
        ]
        self.responses = []
        self.start_time = time.time()

    def start_requests(self):
        # Loop through the pages
        for page in range(1, 6):
            URL = f"http://free-proxy.cz/en/proxylist/main/{page}"
            yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        # Specify the table by its ID 'proxy_list'
        for proxy in response.xpath('//table[@id="proxy_list"]/tbody/tr'):
            # Check if the row contains the script with base64 encoded IP or a valid IP
            encoded_ip_script = proxy.xpath('./td[1]/script/text()').re_first(r'Base64\.decode\("(.+?)"\)')
            plain_text_ip = proxy.xpath('./td[1]/text()').get()

            # If no IP is found, skip this row
            if not encoded_ip_script and not plain_text_ip:
                continue

            # Decode the base64 IP address if available
            if encoded_ip_script:
                decoded_ip = base64.b64decode(encoded_ip_script).decode('utf-8')
            else:
                decoded_ip = plain_text_ip.strip()

            # Extract the port number, if not available, skip this row
            port = proxy.xpath('./td[2]/span/text()').get()
            if not port:
                continue

            self.all_proxies.append(f"{decoded_ip}:{port}")

        # After collecting all proxies from all pages, call the method to post them
        if response.url.endswith(f"main/5"):
            self.post_proxies()

    def post_proxies(self):
        # Process proxies in batches of 10
        for i in range(0, len(self.all_proxies), 10):
            proxy_batch = self.all_proxies[i:i + 10]
            payload = {
                "user_id": self.user_id,
                "len": len(proxy_batch),
                "proxies": ', '.join(proxy_batch)
            }
            # Get a new token for each batch before posting
            form_token = self.get_form_token()
            if not form_token:
                self.logger.error("Failed to retrieve form token.")
                return
            
            # wait_time = random.uniform(15, 20)
            # self.logger.info(f"Waiting for {wait_time:.2f} seconds before the next request...")
            # time.sleep(wait_time)

            proxy = random.choice(self.verified_proxies)
            post_response = requests.post(
                f"{self.api_base_url}/post_proxies",
                headers=self.get_post_headers(),
                cookies=self.get_cookies(form_token),  # Pass cookies with the new token
                json=payload,
                proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}
            )

            if post_response.status_code == 200:
                post_data = post_response.json()
                self.save_response(post_data, proxy_batch)
            else:
                self.logger.error(f"Failed to post proxies: {post_response.text}")
        self.write_responses_to_file()

    def get_form_token(self):
        # Get the token and return the form_token
        token_response = requests.get(f"{self.api_base_url}/get_token", headers=self.get_headers())
        if token_response.status_code != 200:
            self.logger.error("Failed to retrieve token.")
            return None

        # Extract form_token from the Set-Cookie header
        set_cookie_header = token_response.headers.get('set-cookie', '')
        for cookie in set_cookie_header.split(';'):
            if 'form_token=' in cookie:
                return cookie.split('=')[1].strip()

        self.logger.error("form_token not found.")
        return None

    def get_headers(self):
        return {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,ru;q=0.8,ro-RO;q=0.7,ro;q=0.6",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }

    def get_post_headers(self):
        headers = self.get_headers()
        headers["content-type"] = "application/json"
        return headers

    def get_cookies(self, form_token):
        # Return the cookies to include in the POST request
        return {
            "x-user_id": self.user_id,
            "form_token": form_token  # Use the provided form_token
        }

    def save_response(self, response_data, proxy_batch):
        save_id = response_data.get("save_id")
        if save_id:
            self.responses.append({save_id: ", ".join(proxy_batch)})

    def write_responses_to_file(self):
        with open("result.json", "w") as f:
            json.dump(self.responses, f, indent=4)

        with open("time.txt", "w") as f:
            f.write("Elapsed Time: " + str(time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - self.start_time))))
            
