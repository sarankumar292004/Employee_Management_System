from flask import Flask, render_template, request, redirect

from database import conn, cursor

app = Flask(__name__)

# home page

@app.route("/")

def home():

    cursor.execute(
        "SELECT * FROM employees"
    )

    employees = cursor.fetchall()

    return render_template(
        "index.html",
        employees=employees
    )

# add employee

@app.route(
    "/add",
    methods=["GET", "POST"]
)

def add_employee():

    if request.method == "POST":

        name = request.form["name"]

        department = request.form["department"]

        salary = request.form["salary"]

        query = """

        INSERT INTO employees
        (name, department, salary)

        VALUES (%s, %s, %s)

        """

        values = (
            name,
            department,
            salary
        )

        cursor.execute(query, values)

        conn.commit()

        return redirect("/")

    return render_template(
        "add_employee.html"
    )

# edit employee

@app.route(
    "/edit/<int:id>",
    methods=["GET", "POST"]
)

def edit_employee(id):

    if request.method == "POST":

        name = request.form["name"]

        department = request.form["department"]

        salary = request.form["salary"]

        query = """

        UPDATE employees

        SET
            name=%s,
            department=%s,
            salary=%s

        WHERE id=%s

        """

        values = (
            name,
            department,
            salary,
            id
        )

        cursor.execute(query, values)

        conn.commit()

        return redirect("/")

    query = """

    SELECT * FROM employees

    WHERE id=%s

    """

    cursor.execute(query, (id,))

    employee = cursor.fetchone()

    return render_template(
        "edit_employee.html",
        employee=employee
    )

# delete employee

@app.route("/delete/<int:id>")

def delete_employee(id):

    query = """

    DELETE FROM employees

    WHERE id=%s

    """

    cursor.execute(query, (id,))

    conn.commit()

    return redirect("/")

if __name__ == "__main__":

    app.run(debug=True)