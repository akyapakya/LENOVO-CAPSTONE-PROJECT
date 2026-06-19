from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "").lower().strip()

    responses = {
        "oop": """
Object-Oriented Programming (OOP) is a programming paradigm based on objects.

The four pillars of OOP are:
• Encapsulation
• Inheritance
• Polymorphism
• Abstraction

Popular OOP languages include Java, C++, and Python.
""",

        "object oriented programming": """
Object-Oriented Programming (OOP) is a programming paradigm based on objects.

The four pillars of OOP are:
• Encapsulation
• Inheritance
• Polymorphism
• Abstraction

Popular OOP languages include Java, C++, and Python.
""",

        "python": """
Python is a high-level, interpreted programming language known for its simplicity and readability.

Applications of Python:
• Web Development
• Artificial Intelligence
• Data Science
• Automation
• Machine Learning
""",

        "java": """
Java is an object-oriented programming language developed by Sun Microsystems.

Key Features:
• Platform Independent
• Secure
• Robust
• Multithreaded
• Object-Oriented
""",

        "machine learning": """
Machine Learning is a branch of Artificial Intelligence that enables systems to learn from data.

Types of Machine Learning:
• Supervised Learning
• Unsupervised Learning
• Reinforcement Learning
""",

        "artificial intelligence": """
Artificial Intelligence (AI) refers to machines performing tasks that normally require human intelligence.

Examples:
• Chatbots
• Recommendation Systems
• Self-Driving Cars
• Voice Assistants
""",

        "data structure": """
A Data Structure is a method of organizing data efficiently.

Common Data Structures:
• Array
• Linked List
• Stack
• Queue
• Tree
• Graph
""",

        "flask": """
Flask is a lightweight Python web framework used to build web applications and APIs.

Advantages:
• Simple
• Flexible
• Easy to Learn
• Lightweight
""",

        "database": """
A database is an organized collection of data.

Popular Databases:
• MySQL
• PostgreSQL
• SQLite
• MongoDB
"""
    }

    response = None

    for keyword, answer in responses.items():
        if keyword in msg:
            response = answer
            break

    if response is None:
        response = """
Welcome to EduMate AI!

I can currently help with:
• OOP
• Python
• Java
• Data Structures
• Artificial Intelligence
• Machine Learning
• Flask
• Databases

Try asking:
• What is OOP?
• Explain Python
• What is Machine Learning?
• What is AI?
"""

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
