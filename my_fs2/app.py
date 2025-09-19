from flask import Flask, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io, base64

app = Flask(__name__)

def create_plot(plot_type):
    img = io.BytesIO()
    x = np.linspace(0, 10, 50)
    y = np.sin(x)

    plt.figure()

    if plot_type == "line":
        plt.plot(x, y, label="Sine Wave")
        plt.title("Line Chart")
        plt.legend()
    elif plot_type == "bar":
        plt.bar([1,2,3,4,5], [5,7,3,8,4])
        plt.title("Bar Chart")
    elif plot_type == "pie":
        plt.pie([10,20,30,40], labels=["A","B","C","D"], autopct="%1.1f%%")
        plt.title("Pie Chart")
    elif plot_type == "hist":
        plt.hist(np.random.randn(1000), bins=20, color="skyblue", edgecolor="black")
        plt.title("Histogram")
    elif plot_type == "scatter":
        plt.scatter(np.random.rand(50), np.random.rand(50), c="red")
        plt.title("Scatter Plot")
    elif plot_type == "area":
        plt.fill_between(x, y, alpha=0.5, color="green")
        plt.title("Area Chart")

    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return graph_url


@app.route("/")
def index():
    charts = {
        "Line Chart": create_plot("line"),
        "Bar Chart": create_plot("bar"),
        "Pie Chart": create_plot("pie"),
        "Histogram": create_plot("hist"),
        "Scatter Plot": create_plot("scatter"),
        "Area Chart": create_plot("area"),
    }
    return render_template("index.html", charts=charts)

if __name__ == "__main__":
    app.run(debug=True)