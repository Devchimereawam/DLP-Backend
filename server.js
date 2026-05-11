const express = require("express");

const app = express();

app.use(express.json());

const students = [];

app.post("/api/students", (req, res) => {

    const { name, email, course } = req.body;

    if (!name || !email || !course) {
        return res.status(400).json({
            message: "All fields are required"
        });
    }

    const student = {
        id: students.length + 1,
        name,
        email,
        course
    };

    students.push(student);

    res.status(201).json({
        message: "Student registered successfully",
        student
    });
});

app.get("/api/students", (req, res) => {
    res.json(students);
});

const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});