# -*- coding: utf-8 -*-
"""Optional local API proxy for the floor-plan recognition demo.

Set AI_API_KEY in the environment before starting this server. Never commit a
real key to the repository or expose it in browser-side JavaScript.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import ssl
import urllib.error
import urllib.request

API_BASE = os.environ.get("AI_API_BASE", "https://api.inferera.com/v1")
API_KEY = os.environ.get("AI_API_KEY", "")
PORT = int(os.environ.get("PORT", "8765"))


class ProxyHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_POST(self):
        if not self.path.startswith("/v1/"):
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
            return
        if not API_KEY:
            self._set_headers(503)
            self.wfile.write(json.dumps({"error": "AI_API_KEY is not configured"}).encode())
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        request = urllib.request.Request(
            API_BASE + self.path[3:],
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + API_KEY,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                request, timeout=300, context=ssl.create_default_context()
            ) as response:
                self._set_headers(response.status)
                self.wfile.write(response.read())
        except urllib.error.HTTPError as error:
            self._set_headers(error.code)
            self.wfile.write(error.read())
        except Exception as error:
            self._set_headers(502)
            self.wfile.write(
                json.dumps({"error": str(error), "type": "proxy_error"}).encode()
            )


if __name__ == "__main__":
    print(f"Local proxy: http://localhost:{PORT}/v1")
    HTTPServer(("127.0.0.1", PORT), ProxyHandler).serve_forever()
