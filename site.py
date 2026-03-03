from flask import Flask, request, jsonify, render_template
import src.playerList as playerList
import src.selection as selection
import src.roles as roles

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    text = data.get("text", "")

    playerList.playerList.clear()
    playerList.playerRoleList.clear()

    playerList.town_members.clear()
    playerList.coven_members.clear()
    playerList.town_roles.clear()
    playerList.all_evil_roles.clear()
    playerList.all_roles.clear()

    playerList.playerList.extend([line.strip() for line in text.splitlines() if line.strip()])

    selection.Coven = roles.Coven()
    selection.Apoc = roles.Apoc()
    selection.Neutral = roles.Neutral()
    selection.Town = roles.Town()

    selection.StartNewGame()

    output = ""
    for k, v in playerList.playerRoleList.items():
        color = "white"
        if v in playerList.coven:
            color = "magenta"
        if v in playerList.apoc:
            color = "red"
        if v in playerList.neutral:
            color = "yellow"
        if v in playerList.town:
            color = "green"
        output += f'<span style="color:{color}">{k}: {v}</span><br>'

    output += "\n"

    output += selection.pirate() or ""
    output += "\n"
    output += selection.alchemy() or ""
    output += "\n"
    output += selection.exe() or ""
    output += "\n"
    output += selection.admirer() or ""


    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(debug=True)