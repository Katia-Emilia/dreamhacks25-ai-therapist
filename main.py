from flask import Flask, render_template, request,session, redirect, url_for
from core import handle_user_mood, start_fake_video_call_and_listen
from voice_mode import voice_mode
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.permanent_session_lifetime = timedelta(minutes=1)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        agreement = request.form.get("agreement")
        name = request.form.get("name")
        mode = int(request.form.get("mode"))

        if agreement != "y" and agreement != "admin code 110308":
            return render_template("index.html", error="You must agree to continue.")

        if mode == 2:
            start_fake_video_call_and_listen(mode)
            return "Video chat session ended."
        elif mode == 3:
            voice_mode(name, mode)
            return "Voice chat session ended."
        else:
            return redirect(url_for("chat", name=name, mode=mode))

    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    name = request.args.get("name")
    mode = int(request.args.get("mode"))

    if "conversation" not in session:
        session["conversation"] = []

    if request.method == "POST":
        user_input = request.form.get("user_input").lower()
        if "ok thank you for the session" in user_input:
            session.clear()
            return render_template("chat.html", name=name, mode=mode, goodbye=True)

        # Assume handle_user_mood returns a string
        thea_response = handle_user_mood(user_input, mode, detected_emotion=None)

        # Append to conversation
        session["conversation"].append({"user": user_input, "thea": thea_response})
        session.modified = True  # Make sure session updates are saved

    return render_template("chat.html", name=name, mode=mode, conversation=session.get("conversation", []))

if __name__ == "__main__":
    
    app.run(debug=True)
