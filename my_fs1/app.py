# from flask import Flask, render_template

# app = Flask(__name__)

# # Home route
# @app.route('/')
# def index():
#     return render_template('index.html')

# # About route
# @app.route('/about')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# Flask2

# from flask import Flask, Response
# import matplotlib.pyplot as plt
# import io

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h1>Hello Flask!</h1><p>Go to <a href='/plot'>/plot</a> to see the graph.</p>"

# @app.route("/plot")
# def plot():

#     plt.figure()
#     x = [1, 2, 3, 4, 5]
#     y = [1, 4, 9, 16, 25]
#     plt.plot(x, y, marker="o", color="blue")
#     plt.title("Simple Graph in Flask")
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     buf = io.BytesIO()
#     plt.savefig(buf, format="png")
#     buf.seek(0)
#     return Response(buf.getvalue(), mimetype='image/png')

# if __name__ == "__main__":
#     app.run(debug=True)

# flask 3

# from flask import Flask, render_template
# import matplotlib.pyplot as plt
# import io, base64

# app = Flask(__name__)

# @app.route("/")
# def index():
#     plt.figure()
#     x = [1, 2, 3, 4, 5]
#     y = [1, 4, 9, 16, 25]
#     plt.plot(x, y, marker="o", color="blue")
#     plt.title("Simple Graph in Flask (HTML)")
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     buf = io.BytesIO()
#     plt.savefig(buf, format="png")
#     buf.seek(0)
#     graph_url = base64.b64encode(buf.getvalue()).decode('utf8')
#     plt.close()

#     return render_template("index.html", graph_url=graph_url)

# # ✅ Add this about route
# @app.route("/about")
# def about():
#     return render_template("about.html")

# if __name__ == "__main__":
#     app.run(debug=True)


#flask 4
from flask import Flask, render_template, request, url_for
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import io, base64

app = Flask(__name__)

def fig_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close()
    return img_b64

categories = ["A", "B", "C", "D", "E"]
values = [23, 45, 12, 30, 18]
x = np.arange(1, 11)
y = np.array([2, 3, 5, 6, 7, 9, 11, 10, 12, 14])
hist_data = np.random.normal(loc=50, scale=12, size=300)

@app.route("/")
def home():
    menu = [
        {"name": "Bar", "endpoint": url_for('chart', ctype='bar')},
        {"name": "Pie", "endpoint": url_for('chart', ctype='pie')},
        {"name": "Line", "endpoint": url_for('chart', ctype='line')},
        {"name": "Histogram", "endpoint": url_for('chart', ctype='hist')},
    ]
    return render_template("index.html", menu=menu)

@app.route("/about")
def about():
    menu = [
        {"name": "Bar", "endpoint": url_for('chart', ctype='bar')},
        {"name": "Pie", "endpoint": url_for('chart', ctype='pie')},
        {"name": "Line", "endpoint": url_for('chart', ctype='line')},
        {"name": "Histogram", "endpoint": url_for('chart', ctype='hist')},
    ]
    return render_template("about.html", menu=menu)


@app.route("/chart/<ctype>")
def chart(ctype):
    title = ""

    if ctype == "bar":
        title = "Bar Chart"
        plt.figure()
        plt.bar(categories, values)
        plt.xlabel("Category")
        plt.ylabel("Value")
        plt.title(title)

    elif ctype == "pie":
        title = "Pie Chart"
        plt.figure()
        plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=90)
        plt.title(title)
        plt.axis("equal")

    elif ctype == "line":
        title = "Line Chart"
        plt.figure()
        plt.plot(x, y, marker="o")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(title)
        plt.grid(True, linestyle="--", alpha=0.5)

    elif ctype == "hist":
        title = "Histogram"
        plt.figure()
        plt.hist(hist_data, bins=20)
        plt.title(title)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.grid(True, linestyle="--", alpha=0.5)

    else:
        return "Unknown chart type.", 400

    img_b64 = fig_to_base64()
    menu = [
        {"name": "Bar", "endpoint": url_for('chart', ctype='bar')},
        {"name": "Pie", "endpoint": url_for('chart', ctype='pie')},
        {"name": "Line", "endpoint": url_for('chart', ctype='line')},
        {"name": "Histogram", "endpoint": url_for('chart', ctype='hist')},
    ]
    return render_template("chart.html", chart_title=title, img_b64=img_b64, menu=menu)

if __name__ == "__main__":
    app.run(debug=True)