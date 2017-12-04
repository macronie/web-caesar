from flask import Flask
from caesar import rotate_string
from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web Ceasar</title>
    </head>
    <body>
        <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
       </style>
"""

page_footer = """
    </body>
</html>
"""

web_caesar = """
      <!-- create your form here -->
        <form action="/" method = "post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            
            <input type="submit">
        </form>
"""

@app.route("/", methods=['POST'])
def encrypt():
    form = web_caesar
    no_of_rotation = int(request.form['rot'])
    encrypt_text = str(request.form['text'])
    encrypted_text = rotate_string(encrypt_text, no_of_rotation)
    content = page_header + form.format(encrypted_text) + page_footer
    return content

@app.route("/")
def index():
    form_text= " "

    content = page_header + web_caesar.format(form_text)+ page_footer
    return content

app.run()