from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def convert():
    tf = tree_formatter()
    tree = tf.extract_file_names()
    tf.set_directory_depth(tf.determine_depth(tree))
    tf.set_directory_names(tree)
    tf.create_tree_structure_file()
    tf.append_directory_structure()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)