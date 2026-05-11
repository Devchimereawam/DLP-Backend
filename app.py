from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route('/api/students', methods=['POST'])
def register_student():

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    course = data.get('course')

    if not name or not email or not course:
        return jsonify({
            "message": "All fields are required"
        }), 400

    student = {
        "id": len(students) + 1,
        "name": name,
        "email": email,
        "course": course
    }

    students.append(student)

    return jsonify({
        "message": "Student registered successfully",
        "student": student
    }), 201


@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)


if __name__ == '__main__':
    app.run(debug=True)