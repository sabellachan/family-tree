from server import app
# import csv

from model import Member, connect_to_db, db


def load_family_members():
    """Retrieve family member information."""

    Member.query.delete()

    for row in open('data/seed_data.xls'):
        strip_row = row.rstrip()
        split_row = strip_row.split()

        # member_id, first_name, last_name, eng_title, alt_name, lineage, deceased, image_url, parents, children, spouse = row.split()
        member_id = split_row[0]

        first_name = split_row[1]

        last_name = split_row[2]

        if split_row[3] is not None:
            eng_title = split_row[3]
        else:
            eng_title = None

        if split_row[4] is not None:
            alt_name = split_row[4]
        else:
            alt_name = None

        if split_row[5] is not None:
            lineage = split_row[5]
        else:
            lineage = None

        if split_row[6] is not None:
            deceased = split_row[6]
        else:
            deceased == 0

        if split_row[7] is not None:
            image_url = split_row[7]
        else:
            image_url = None

        if split_row[8] is not None:
            parents = split_row[8]
        else:
            parents = None

        if split_row[9] is not None:
            children = split_row[9]
        else:
            children = None

        if split_row[10] is not None:
            spouse = split_row[10]
        else:
            spouse = None

    # members = open('data/seed_data.csv')

    # data = csv.reader(members)

    # for row in data:
    # # row is a list
        # member_id, first_name, last_name, eng_title, alt_name, lineage, deceased, image_url, parents, children, spouse = row

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
