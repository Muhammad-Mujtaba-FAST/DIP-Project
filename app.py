from flask import Flask, render_template_string
import nbformat
from nbconvert import HTMLExporter

app = Flask(__name__)

@app.route('/')
def serve_notebook():
    # Load the ipynb file
    with open('Main.ipynb', 'r') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    body, _ = html_exporter.from_notebook_node(notebook_content)

    return render_template_string(body)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)