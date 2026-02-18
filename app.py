from flask import Flask, render_template, request
import re, math

app = Flask(__name__)

def calculate_entropy(password):
    charset_size = 0
    if re.search(r"[a-z]", password): charset_size += 26
    if re.search(r"[A-Z]", password): charset_size += 26
    if re.search(r"[0-9]", password): charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset_size += 32
    return len(password) * math.log2(charset_size) if charset_size > 0 else 0

def evaluate_password(password):
    entropy = calculate_entropy(password)
    score = 0
    if len(password) >= 8: score += 2
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 2
    if re.search(r"[^a-zA-Z0-9]", password): score += 2
    if entropy > 50: score += 2
    if entropy > 75: score += 3

    if score <= 3: level, color = "Weak", "red"
    elif score <= 6: level, color = "Decent", "orange"
    elif score <= 9: level, color = "Strong", "blue"
    elif score <= 12: level, color = "Epic", "purple"
    else: level, color = "Legendary", "lime"

    return entropy, score, level, color

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        entropy, score, level, color = evaluate_password(password)
        result = {
            "entropy": f"{entropy:.2f}",
            "score": score,
            "level": level,
            "color": color,
            "bar_width": int((score/15)*100)
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
