from flask import Flask, render_template, request, jsonify
from expression_engine import ExpressionEngine

app = Flask(__name__)

# Initialize our ontology graph engine (no parameters needed)
engine = ExpressionEngine()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/get_question")
def get_question():
    # Extract frontend UI request parameters
    lang = request.args.get("lang", "darija")
    
    # The underlying engine determines difficulty automatically via SRS profile metrics.
    question_data = engine.get_question(language=lang, user_id="demo_user")
    
    return jsonify(question_data)

@app.route("/api/update_srs", methods=["POST"])
def update_srs():
    data = request.json
    
    # Process student response history directly into the Description Logic graph state
    engine.update_srs(
        user_id="demo_user", 
        scenario_id=data.get("situation_id"), 
        is_correct=data.get("correct")
    )
    return jsonify({"status": "success"})

if __name__ == "__main__":
    # Bound to port 8080 to prevent standard macOS airplay access denial issues
    app.run(debug=True, port=8080)