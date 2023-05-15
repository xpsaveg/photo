import request
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from flask import Flask,render_template,request
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)

# data base
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    class User(UserMixin, db.Model):
        __tablename__ = 'User'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique=True)
        password = db.Column(db.String(100))
        phone = db.Column(db.String(100))
        city = db.Column(db.String(1000))

    db.session.commit()
    db.create_all()



class MyModelView(ModelView):
    def is_accessible(self):

            return True

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))



@app.route("/", methods=["GET", "POST"])
def add():
    user=User.query.all()
    return render_template("login.html")


     # return render_template("register.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name= request.form.get("name")
        password= request.form.get("password")
        city= request.form.get("city")
        phone = request.form.get("phone")
        new=User(
            name=name,
            password=password,
            city=city,
            phone=phone,

        )

        db.session.add(new)
        db.session.commit()

    return render_template("register.html")
if __name__==("__main__"):
    app.run(debug=True)
