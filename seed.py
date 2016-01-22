from server import app
import csv

from model import Member, connect_to_db, db


def load_family_members():
    """Retrieve family member information."""

    Member.query.delete()

    members = open('data/seed_data.csv')

    data = csv.reader(members)

    for row in data:
    # row is a list
        member_id, first_name, last_name, eng_title, alt_name, lineage, deceased, image_url, parents, children, spouse = row

        member = Member(member_id=member_id,
                        first_name=first_name,
                        last_name=last_name,
                        eng_title=eng_title,
                        alt_name=alt_name,
                        lineage=lineage,
                        deceased=deceased,
                        image_url=image_url,
                        parents=parents,
                        children=children,
                        spouse=spouse)

        db.session.add(member)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # Create all tables if they haven't been created
    db.create_all()

    # Import different types of data
    load_family_members()
