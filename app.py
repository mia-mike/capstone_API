from flask import Flask, request 
import pandas as pd 
app = Flask(__name__) 

@app.route('/')
def miahomepage():
    return "Hello World"

#mengurutkan judul buku dengan list tertinggi ke terendah
@app.route('/rating_buku')
def ratingbuku():
    books = pd.read_csv('data/books_c.csv')
    pd.crosstab(
    index=books['title'],
    columns='average_rating').sort_values(by='average_rating', ascending=False)
    return books.to_json()  

@app.route('/books_melt')
def books_melt():
    books = pd.read_csv('data/books_c.csv')
    books_melt = books.reset_index().melt(id_vars=['title'])
    books_melt[books_melt['title']=='Inside Job']  
    return books_melt.to_json()    

#mendapatkan buku
@app.route('/ambil_buku')
def ambilbuku():
    data = pd.read_csv('data/books_c.csv')
    return data.to_json()    

# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())
 

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 