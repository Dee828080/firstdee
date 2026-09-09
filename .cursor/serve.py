#!/usr/bin/env python3
"""Minimal static dev server for the firstdee site.

The site's markup lives in a file named ``html`` (no extension), so a plain
static file server would offer it as a download instead of rendering it. This
server maps ``/`` to that file and serves it as ``text/html`` while still
exposing the rest of the repository as normal static files.
"""

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))
INDEX_FILE = os.path.join(REPO_ROOT, "html")


class SiteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.serve_index()
            return
        super().do_GET()

    def serve_index(self):
        try:
            with open(INDEX_FILE, "rb") as fh:
                body = fh.read()
        except OSError:
            self.send_error(404, "Site markup not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    handler = partial(SiteHandler, directory=REPO_ROOT)
    server = ThreadingHTTPServer((HOST, PORT), handler)
    print(f"firstdee dev server running at http://{HOST}:{PORT} (serving {REPO_ROOT})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    main()
