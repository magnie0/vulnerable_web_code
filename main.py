from flask import Flask, request, send_from_directory, render_template, abort
import os

app = Flask(__name__, static_url_path = "/images", static_folder = "images")

# Directory where files are stored for downloading
BASE_DIR = os.path.abspath("files")
@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/challenge1')
def chall1():
    return render_template('challenge1.html')

@app.route('/challenge2')
def chall2():
    return render_template('challenge2.html')

@app.route('/files/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        # Create path
        file_path = os.path.join(BASE_DIR, filename)
        print(file_path)

        # DANGEROUS open file from directory
        with open(file_path, 'rb') as f:
            content = f.read()
            print(content)
        return render_template('file_content.html', filename=filename, content=content)
        #return send_from_directory(BASE_DIR, filename)
    except FileNotFoundError:
        abort(404)
    except Exception as e:
        abort(500, str(e))

if __name__ == '__main__':
    app.run(debug=True)

#path traversal: curl --path-as-is http://127.0.0.1:5000/files/../../../../../../../etc/passwd
