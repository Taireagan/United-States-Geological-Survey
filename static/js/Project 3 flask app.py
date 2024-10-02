# Most recent flask app
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('mortgage_rate_data_2018_2022.json') as f:
    average_mortgage = json.load(f)

with open('median_hhi__data_2018_2022.json') as f:
    median_hhi = json.load(f)

with open('unemployment_data_2018_2022.json') as f:
    unemployment_data = json.load(f)

with open('us_rental_data_2018_2022.json') as f:
    rental_data = json.load(f)

with open('us_home_sales_data_2018_2022.json') as f:
    sales_data = json.load(f)

with open('us_home_value_data_2018_2022.json') as f:
    value_data = json.load(f)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<string:dataset>')
def get_data(dataset):
    if dataset == 'rental':
        return jsonify(rental_data)
    elif dataset == 'sales':
        return jsonify(sales_data)
    elif dataset == 'home_value':  # Change this to match HTML dropdown value
        return jsonify(value_data)
    elif dataset == 'average_mortgage':
        return jsonify(average_mortgage)
    elif dataset == 'median_hhi':
        return jsonify(median_hhi)
    elif dataset == 'unemployment_data':
        return jsonify(unemployment_data)
    else:
        return jsonify({'error': 'Dataset not found!'})


if __name__ == '__main__':
    app.run(debug=True)

# End

# Latest round of flask app

from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Function to load JSON data with error handling
def load_json(file_name):
    try:
        with open(file_name) as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return {}

# Load JSON data
average_mortgage = load_json('mortgage_rate_data_2018_2022.json')
median_hhi = load_json('median_hhi__data_2018_2022.json')
unemployment_data = load_json('unemployment_data_2018_2022.json')
rental_data = load_json('us_rental_data_2018_2022.json')
sales_data = load_json('us_home_sales_data_2018_2022.json')
value_data = load_json('us_home_value_data_2018_2022.json')

# Function to wrap data with appropriate key
def wrap_data_with_key(data, key_name):
    wrapped_data = {}

    # If the data is a list, iterate through it
    if isinstance(data, list):
        for item in data:
            # Iterate through each key-value pair in the dictionary
            for date, value in item.items():
                # Only process keys that are dates (skip RegionID, SizeRank, etc.)
                if isinstance(date, str) and date.count('-') == 2:  # Checking for date format (e.g., "2020-01-01")
                    wrapped_data[date] = {key_name: value}
    elif isinstance(data, dict):
        # Handle the case if the data is directly a dictionary
        for date, value in data.items():
            wrapped_data[date] = {key_name: value}

    return wrapped_data
# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to get the data
@app.route('/get_data/<string:dataset>')
def get_data(dataset):
    # Print the type of data to debug
    if dataset == 'rental':
        print(type(rental_data))  # Check the type of rental_data
        print(rental_data[0])
        return jsonify(wrap_data_with_key(rental_data, 'Rentals'))
    elif dataset == 'sales':
        print(type(sales_data))  # Check the type of sales_data
        print(sales_data[0])
        return jsonify(wrap_data_with_key(sales_data, 'Sales'))
    elif dataset == 'home_value':
        print(type(value_data))  # Check the type of home_value data
        print(value_data[0]) 
        return jsonify(wrap_data_with_key(value_data, 'Home Value'))
    elif dataset == 'average_mortgage':
        return jsonify(average_mortgage)
    elif dataset == 'median_hhi':
        return jsonify(median_hhi)
    elif dataset == 'unemployment_data':
        return jsonify(unemployment_data)
    else:
        return jsonify({'error': 'Dataset not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)

    # ENDDDDDDD


    console.log(response);
    let features = response.features;
    function getColor(depth) {
        let colorScale = d3.scaleLinear()
                    .domain([-10, 90])  // Range of depths
                    .range(["green", "red"]);  // Color scale 


                    return colorScale(depth);
                }


















from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('average_mortgage_2018_2022.json') as f:
    average_mortgage = json.load(f)

with open('median_hhi_2018_2022.json') as f:
    median_hhi = json.load(f)

with open('unemployment_data_2018_2022.json') as f:
    unemployment_data = json.load(f)

with open('us_rental_data_2018_2022.json') as f:
    rental_data = json.load(f)

with open('us_sales_data_2018_2022.json') as f:
    sales_data = json.load(f)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<string:dataset>')
def get_data(dataset):
    if dataset == 'rental':
        return jsonify(rental_data)
    elif dataset == 'sales':
        return jsonify(sales_data)
    elif dataset == 'average_mortgage':
        return jsonify(average_mortgage)
    elif dataset == 'median_hhi':
        return jsonify(median_hhi)
    elif dataset == 'unemployment_data':
        return jsonify(unemployment_data)
    else:
        return jsonify({'error': 'Dataset not found!'})

if __name__ == '__main__':
    app.run(debug=True)





# ////OTHER
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('average_mortgage_2018_2022.json') as f:
    average_mortgage = json.load(f)

with open('median_hhi_2018_2022.json') as f:
    median_hhi = json.load(f)

with open('unemployment_data_2018_2022.json') as f:
    unemployment_data = json.load(f)

with open('us_rental_data_2018_2022.json') as f:
    rental_data = json.load(f)

with open('us_sales_data_2018_2022.json') as f:
    sales_data = json.load(f)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<string:dataset>')
def get_data(dataset):
    if dataset == 'rental':
        return jsonify(rental_data)
    elif dataset == 'sales':
        return jsonify(sales_data)
    elif dataset == 'average_mortgage':
        return jsonify(average_mortgage)
    elif dataset == 'median_hhi':
        return jsonify(median_hhi)
    elif dataset == 'unemployment_data':
        return jsonify(unemployment_data)
    else:
        return jsonify({'error': 'Dataset not found!'})

if __name__ == '__main__':
    app.run(debug=True)






from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('mortgage_rate_data_2018_2022.json') as f:
    average_mortgage = json.load(f)

with open('median_hhi__data_2018_2022.json') as f:
    median_hhi = json.load(f)

with open('unemployment_data_2018_2022.json') as f:
    unemployment_data = json.load(f)

with open('us_rental_prices_data_2018_2022.json') as f:
    rental_data = json.load(f)

with open('us_home_sales_data_2018_2022.json') as f:
    sales_data = json.load(f)

with open('us_home_value_data_2018_2022.json') as f:
    value_data = json.load(f)


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<string:dataset>')
def get_data(dataset):
    if dataset == 'rental':
        return jsonify(rental_data)
    elif dataset == 'sales':
        return jsonify(sales_data)
    elif dataset == 'home_value':  # Change this to match HTML dropdown value
        return jsonify(value_data)
    elif dataset == 'average_mortgage':
        return jsonify(average_mortgage)
    elif dataset == 'median_hhi':
        return jsonify(median_hhi)
    elif dataset == 'unemployment_data':
        return jsonify(unemployment_data)
    else:
        return jsonify({'error': 'Dataset not found!'})


if __name__ == '__main__':
    app.run(debug=True)

