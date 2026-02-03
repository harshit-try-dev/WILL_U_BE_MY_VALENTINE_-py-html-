
# Valentine Proposal Web App 💖


from flask import Flask, render_template
app = Flask(__name__)                #Creates the Flask app

@app.route("/")
def home():           #when someone opens the homepage.We simply return the Valentine page.
    return render_template("index.html")

if __name__ == "__main__":          #Run the app in debug mode
    app.run(debug=True)
