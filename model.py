"""Model file for Family Tree app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    """Node within the family tree."""

    __tablename__ = "members"

    member_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    eng_title = db.Column(db.String(20), nullable=True)
    viet_title = db.Column(db.String(10), nullable=True)
    alt_name = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(80), nullable=True)

    # parents = should refer to other nodes
    children = db.relationship("Member", backref="parents")

    def __init__(self, data, parents=None, children=None):
        children = children or []
        self.data = data
        self.parents = parents
        self.children = children

    def __repr__(self):
        """Human-readable representation."""

        return "<Member {}".format(self.data)


#############################################################################################
# Connect to database and start app


def connect_to_db(app, db_uri=None):
    """Connect the database to our PostgreSQL app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', db_uri)
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # Allows interactive querying in the shell.

    from server import app
    connect_to_db(app)
    print "Connected to DB."