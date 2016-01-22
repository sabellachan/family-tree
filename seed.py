from server import app
import csv

key = os.environ['key']

def load_family_members():
    """Retrieve what activities are available within what parks and load into database. Refers to Park_Activity."""

    Member.query.delete()

    for row in open('data/seed_data'):
        row = row.rstrip()
        # row.split() brings back a list of pairs
        # unpack the row of the CSV = row.split()

        member = Member(activity_id=activity_id, rec_area_id=rec_area_id)

        db.session.add(member)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # Create all tables if they haven't been created
    db.create_all()

    # Import different types of data
    load_family_members()