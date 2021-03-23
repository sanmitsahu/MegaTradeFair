from flask import Flask, render_template, request, flash, redirect
from db_op import insert_db, read_db, update_db, exist_db, graph_exhibitor_industry
from table_details import tabledetails
from initialise_db import initialise_db
from datetime import datetime

initialise_db()

app = Flask(__name__, template_folder='./templates/')
app.secret_key ='python internship'

@app.route('/')
def home():
    return redirect("/dashboard")

@app.route('/view', methods=['GET', 'POST'])
def view_tables():
    if request.method == "POST":
        table_name = request.form.get("fair_tables", None)
        if table_name!=None:
            results = tabledetails(table_name)
            column_names,displayquery = results[0], results[1]
            data = read_db(displayquery)
            return render_template("view.html", table_name = table_name, column_names = column_names, data = data)
    return render_template("view.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def view_dashboard():
    if request.method == "POST":
        table_name = request.form.get("fair_tables", None)
        if table_name!=None:
            results = tabledetails(table_name)
            column_names,displayquery = results[0], results[1]
            data_value = read_db(displayquery)
            graph1values = graph_exhibitor_industry(1)
            labels=[]
            values=[]
            labels_graph1 = [row[0] for row in graph1values]
            values_graph1 = [row[1] for row in graph1values]
            graph2values = graph_exhibitor_industry(2)
            labels_graph2 = [row[0] for row in graph2values]
            values_graph2 = [row[1] for row in graph2values]
            labels.insert(0, labels_graph2)
            values.insert(0, values_graph2)
            labels.insert(0,labels_graph1)
            values.insert(0,values_graph1)

            return render_template("index.html", table_name = table_name, column_names = column_names, data_value = data_value, labels = labels, values = values)
    return render_template("index.html",labels=[],values=[])


@app.route('/add/<tablename>', methods=['GET', 'POST'])
def add(tablename):
    results = tabledetails(tablename)
    column_names = results[0]
    addquery = results[2]
    existquery = results[4]
    index = results[5]
    column_names.pop(0)
    if request.method == 'POST':
        form_data = request.form
        form_values = []
        k = 0
        for i in form_data:
            if column_names[k] in("Pincode", "Gender", "Booking status"):
                form_values.append(int(form_data[i]))
            elif column_names[k] in("Total Amount"):
                form_values.append(float(form_data[i]))
            elif column_names[k] in("Date-Of-Birth","Booking Date", "Booking starts", "Start Date", "End date", "Spend Date"):
                datestr = str(form_data[i])
                temp_date = datetime.strptime(datestr, "%Y-%m-%d")
                strdate = str(temp_date)
                T_index = strdate.index(" ")
                strdate = strdate[0:T_index]
                form_values.append(strdate)
            else:
                form_values.append(form_data[i])
            k += 1
        if exist_db(existquery, form_values, index)==0:
            addrecord = insert_db(addquery,form_values)
            flash('Added the data successfully')
        else:
            flash('Given data already exists in the database.')
        return redirect('/view')
    return render_template('add_data.html', tablename = tablename, column_names = column_names)

@app.route('/edit/<tablename>/<id>', methods = ['GET', 'POST'])
def edit(tablename,id):
    results = tabledetails(tablename)
    column_names = results[0]
    updatequery = results[3]
    column_names.pop(0)
    if request.method == 'POST':
        form_data = request.form
        form_values = []
        k = 0
        for i in form_data:
            if column_names[k] in("Pincode", "Gender", "Booking status"):
                form_values.append(int(form_data[i]))
            elif column_names[k] in("Total Amount","Booking Total Amount"):
                form_values.append(float(form_data[i]))
            elif column_names[k] in("Date-Of-Birth","Booking Date", "Booking starts", "Start Date", "End date", "Spend Date"):
                datestr = str(form_data[i])
                temp_date = datetime.strptime(datestr, "%Y-%m-%d")
                strdate = str(temp_date)
                T_index = strdate.index(" ")
                strdate = strdate[0:T_index]
                form_values.append(strdate)
            else:
                form_values.append(form_data[i])
            k += 1
        form_values.append(int(id))
        addrecord = update_db(updatequery,form_values)
        flash('Updated the data successfully')
        #print(form_values, id, addrecord)
        return redirect('/view')
    return render_template('edit.html', tablename = tablename, record_id = id, column_names = column_names)

if __name__ == '__main__':
    #app.secret_key = 'super secret key'
    app.run(debug=True)

