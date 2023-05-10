import request
from flask import Flask,render_template,request
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    class User(UserMixin, db.Model):
        _tablename_ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        phone = db.Column(db.String(100), unique=True)
        password = db.Column(db.String(100))
        name = db.Column(db.String(1000))


    class Messages(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        link = db.Column(db.String(2000))
        image = db.Column(db.String(2000))
        description = db.Column(db.String(4000))



    db.session.commit()
    db.create_all()
class MyModelView(ModelView):
    def is_accessible(self):

            return True

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Messages, db.session))


@app.route("/",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        phone=request.form.get("password")
        new=User(
            name=name,
            password=password,
            phone=password,

        )
        db.session.add(new)
        db.session.commit()

    return render_template("register.html")

data={
    "img":"https://images.unsplash.com/photo-1661956601031-4cf09efadfce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80",
    "i": "https://images.unsplash.com/photo-1661956601031-4cf09efadfce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80",

}

rating={
    "img":"good",
    # "i":2
}



@app.route("/")
def start():
    images=data
    return render_template("lessson5.html",img=images)
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        link = request.form.get("link")
        data[name] = link
        return redirect("/")
    return render_template("add.html")

@app.route("/show")
def show():
    key = request.args.get('key')
    for k in rating:
        if k==key:
            return f"{rating[key]}"

    return f" i didnot find a rating for {key}"


if __name__==("__main__"):
    app.run(debug=True)


if __name__==("__main__"):

    app.run(debug=True)
