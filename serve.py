"""Preview the site at http://localhost:8000 with fresh assets."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class PreviewHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".css": "text/css",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).resolve().parent), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    with ThreadingHTTPServer(("127.0.0.1", 8000), PreviewHandler) as server:
        print("Inova Digital: http://localhost:8000", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
