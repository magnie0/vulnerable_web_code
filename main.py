from flask import Flask, request, send_from_directory, render_template, render_template_string, abort, flash
import os
import mysql.connector
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




@app.route('/challenge3', methods=['GET', 'POST'])
def chall3():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        return '<html><body><h1>Result:</h1><p>' + user_input + '</p><a href="/challenge3">Go Back to writing data</a></body></html>'
    return render_template('challenge3.html')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #Connection as in https://knowledge-base.secureflag.com/vulnerabilities/sql_injection/sql_injection_python.html
        # Prepare database connection
        #db = pymysql.connect( user='root', host = 'localhost', passwd='')

        
        connection = mysql.connector.connect(database='webServer', host = 'localhost',
                                            user='testuser',password='testuser')
        cursor = connection.cursor()

        # Execute the vulnerable SQL query concatenating user-provided input.
        sqlRequest =  "select * from users where username ='"+username+"'and password ='"+password+"'"

        cursor.execute(sqlRequest)
        # If the query returns any matching record, consider the current user logged in.
        record = cursor.fetchone()
        #record = True
        if record:
            flash('Login successful! FLAG#wefrwaoipejprow3opo#', 'success')
            #return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('challenge2.html')

if __name__ == '__main__':
    app.secret_key = 'secretkey' #shouldnt be here in production
    app.run(debug=True)

#path traversal: curl --path-as-is http://127.0.0.1:5000/files/../../../../../../../etc/passwd
