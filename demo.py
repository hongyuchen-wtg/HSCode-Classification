import logic
import threading
import time
import webview
from pywebio.input import input
from pywebio.output import put_markdown, put_button, clear, put_scope, clear_scope, put_text
from pywebio import start_server


def StartWindow():
    while True:
        clear()

        put_text("Data comes from `hyecm2.db.sand.wtg.zone/CW-RefDb-Trf-NZ-000015/NZCClassification`")
        inputChar = input("HS Code Description Queries (split queries by '/')", type="text")
        result = logic.HSCodeSearch(index, descriptions, hscodes, inputChar)

        scope_name = "result_scope"
        clear_scope(scope_name)
        put_scope(scope_name)
        put_markdown(f"## Query Results:\n{result}")

        btn_clicked = None
        def on_click():
            nonlocal btn_clicked
            btn_clicked = True

        put_button("Re-Query", onclick=on_click)

        while not btn_clicked:
            pass


def start_pywebio():
    start_server(StartWindow, port=8080)


if __name__ == "__main__":
    start = time.time()
    index, descriptions, hscodes = logic.Load()
    end = time.time()
    print(f"Model Loading Time: {end - start:.4f} s\n")
    
    # Use web
    start_server(StartWindow, port=8080)

    # Use window
    # threading.Thread(target=start_pywebio, daemon=True).start()
    # webview.create_window("UI Demo", "http://localhost:8080", width=1000, height=800)
    # webview.start()

