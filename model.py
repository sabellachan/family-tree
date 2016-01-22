"""Model file for Family Tree app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# association table for parents<->children
children = db.Table('children',
                    db.Column('child_id', db.Integer, db.ForeignKey('member.member_id')),
                    db.Column('parent_id', db.Integer, db.ForeignKey('member.member_id'))
                    )

# association table for spouses
spouses = db.Table('spouses',
                   db.Column('so1_id', db.Integer, db.ForeignKey('member.member_id')),
                   db.Column('so2_id', db.Integer, db.ForeignKey('member.member_id'))
                   )


class Member(db.Model):
    """Node within the family tree."""

    __tablename__ = "members"

    member_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    eng_title = db.Column(db.String(20), nullable=True)
    alt_name = db.Column(db.String(50), nullable=True)
    lineage = db.Column(db.String(15), nullable=True)
    deceased = db.Column(db.Boolean, nullable=True)
    image_url = db.Column(db.String(80), nullable=True)
    parents = db.relationship('Member',
                              secondary=children,
                              primaryjoin=(children.c.child_id == member_id),
                              secondaryjoin=(children.c.parent_id == member_id),
                              backref=db.backref('children', lazy='dynamic'),
                              lazy='dynamic')
    spouse = db.relationship('Member',
                             secondary=spouses,
                             primaryjoin=(spouses.c.so1_id == member_id),
                             secondaryjoin=(spouses.c.so2_id == member_id),
                             backref=db.backref('spouses', lazy='dynamic'),
                             lazy='dynamic')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Member member_id={} first_name={} last_name={}".format(self.member_id,
                                                                        self.first_name,
                                                                        self.last_name)


class User(db.Model):
    """User of family tree website to ensure that it remains private."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return '<User user_id={} email={} first_name={} last_name={}>'.format(self.user_id,
                                                                              self.email,
                                                                              self.first_name,
                                                                              self.last_name)


#############################################################################################
# Connect to database and start app


def connect_to_db(app, db_uri=None):
    """Connect the database to our PostgreSQL app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/familytree'
    #os.environ.get('DATABASE_URL', db_uri)
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # Allows interactive querying in the shell.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
