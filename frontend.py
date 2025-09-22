import config
import requests
from pywebio.input import input
from pywebio.output import put_markdown, put_button, clear, put_scope, clear_scope, put_text
from pywebio import start_server


def StartWindow():
    while True:
        clear()

        put_text("Data comes from `hyecm2.db.sand.wtg.zone/CW-RefDb-Trf-NZ-000015/NZCClassification`")
        inputChar = input(f"HS Code Description Queries (split queries by '{config.SEPARATOR}')", type="text")

        try:
            response = requests.get(f"http://localhost:{config.API_PORT}/query", params={"query": inputChar, "resultFormat": config.RESULT_FORMAT_UI})
            response.raise_for_status()
            data = response.json()
            result_text = data["result"]
        except Exception as e:
            result_text = f"Error: {str(e)}"

        scope_name = "result_scope"
        clear_scope(scope_name)
        put_scope(scope_name)
        put_markdown(f"## Query Results:\n{result_text}")

        btn_clicked = None
        def on_click():
            nonlocal btn_clicked
            btn_clicked = True

        put_button("Re-Query", onclick=on_click)

        while not btn_clicked:
            pass

if __name__ == "__main__":
    start_server(StartWindow, port=config.UI_PORT)