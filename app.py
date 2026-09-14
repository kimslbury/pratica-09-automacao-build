"""Aplicação mínima usada para demonstrar automação de build."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


def build_info() -> dict[str, str]:
    """Retorna informações simples e determinísticas para o teste."""
    return {
        "application": "pratica-09-automacao-build",
        "status": "ok",
        "version": os.getenv("APP_VERSION", "local"),
    }


class BuildHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - nome exigido pelo servidor HTTP
        payload = json.dumps(build_info(), ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    server = HTTPServer(("0.0.0.0", 8000), BuildHandler)
    print("Servidor iniciado em http://0.0.0.0:8000", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

