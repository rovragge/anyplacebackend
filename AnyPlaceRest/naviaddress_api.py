import requests


class NaviAddressApi:

    def __init__(self):
        headers = {'Content-type': 'application/json'}
        body = {
            "password": "1qazxw2",
            "type": "email",
            "email": "volodin.kirill.a@gmail.com"
        }
        r = requests.post("https://staging-api.naviaddress.com/api/v1.5/sessions", headers=headers, json=body)
        self.token = r.json()['token']

    def get_naviaddress(self, container, naviaddress):
        url_pattern = "https://staging-api.naviaddress.com/api/v1.5/Addresses/{}/{}"
        url = url_pattern.format(container, naviaddress)
        r = requests.get(url)
        return r.json()['result']

    def create_naviaddress(self, lat, lng,
                           address_type="free",
                           default_lang="en"):
        headers = {'auth-token': self.token,
                   'Content-type': 'application/json'}
        body = {
            "address_type": address_type,
            "default_lang": default_lang,
            "lat": lat,
            "lng": lng
        }
        r = requests.post("https://staging-api.naviaddress.com/api/v1.5/Addresses", headers=headers, json=body)
        return r.json()['result'], r.status_code

    def confirm_naviaddress(self, container, naviaddress):
        url_pattern = "https://staging-api.naviaddress.com/api/v1.5/addresses/accept/{}/{}"
        url = url_pattern.format(container, naviaddress)
        headers = {'auth-token': self.token,
                   'Content-type': 'application/json'}

        r = requests.post(url, headers=headers)

        return r.json()['result'], r.status_code

    def update_naviaddress(self, container, naviaddress, name,
                           lang="en",
                           description=None,
                           map_visibility=None,
                           lat=None,
                           lng=None,
                           cover=None):
        url_pattern = "https://staging-api.naviaddress.com/api/v1.5/Addresses/{}/{}"
        url = url_pattern.format(container, naviaddress)
        body = {'lang': lang, 'name': name}
        if description is not None:
            body['description'] = description
        if map_visibility is not None:
            body['map_visibility'] = map_visibility
        if lat is not None and lng is not None:
            body['point'] = {'lat': lat, 'lng': lng}
        if cover is not None:
            body['cover'] = cover

        headers = {'auth-token': self.token,
                   'Content-type': 'application/json'}

        r = requests.put(url, headers=headers, json=body)
        return r.json()['result'], r.status_code

    def upload_image(self, image):
        headers = {'auth-token': self.token}
        url = "https://staging-api.naviaddress.com/api/v1.5/Images"
        r = requests.post(url, headers=headers, files={'file': image})
        return r.json(), r.status_code

    def delete_naviaddress(self, container, naviaddress):
        url_pattern = "https://staging-api.naviaddress.com/api/v1.5/Addresses/{}/{}"
        url = url_pattern.format(container, naviaddress)

        headers = {'auth-token': self.token,
                   'Content-type': 'application/json'}

        r = requests.delete(url, headers=headers)
        return r.json()['message'], r.status_code
