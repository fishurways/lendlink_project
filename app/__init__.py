from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = Flask(__name__,
            static_folder="static",
            static_url_path="/static",
            )

class Base(DeclarativeBase):
    pass

# initiate db through SQLAlchemy
app.config["SECRET_KEY"] = "12345678"  # Ganti dengan secret key yang aman
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # Nama database SQLite

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Membuat model untuk tabel pengguna
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String)


# Membuat tabel jika belum ada
with app.app_context():
    db.create_all()

# memanggil template bootsrap5
bootstrap = Bootstrap5(app)
