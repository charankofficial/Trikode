from flask import Flask,render_template
app=Flask(__name__)
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/services",methods=["GET"])
def services():
    return render_template("service.html")

@app.route("/services/compliance",methods=["GET"])
def compliance():
    return render_template("compliance_service.html")

@app.route("/services/security",methods=["GET"])
def security():
    return render_template("security_service.html")

@app.route("/services/vapt",methods=["GET"])
def vapt():
    return render_template("vapt_service.html")

@app.route("/services/infrastructure",methods=["GET"])
def infrastructure():
    return render_template("infra_service.html")

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/project",methods=["GET"])
def project():
    return render_template("project.html")

@app.route("/feature",methods=["GET"])
def feature():
    return render_template("feature.html")

@app.route("/quote",methods=["GET"])
def qyote():
    return render_template("quote.html")

@app.route("/testimonial",methods=["GET"])
def testimonial():
    return render_template("testimonial.html")

@app.route("/team",methods=["GET"])
def team():
    return render_template("team.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True)