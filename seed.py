from server import app
# import csv

from model import Member, connect_to_db, db


def load_family_members():
    """Retrieve family member information."""

    Member.query.delete()

    for row in open('data/seed_data_sample_plain'):
        strip_row = row.strip()
        split_row = strip_row.split('|')

        member_id = split_row[0].strip()

        first_name = split_row[1].strip()

        last_name = split_row[2].strip()

        if split_row[3].strip() is not None:
            eng_title = split_row[3].strip()
        else:
            eng_title = None

        if split_row[4].strip() is not None:
            alt_name = split_row[4].strip()
        else:
            alt_name = None

        if split_row[5].strip() is not None:
            lineage = split_row[5].strip()
        else:
            lineage = None

        if split_row[6].strip() == 1:
            deceased = split_row[6].strip()
        else:
            deceased = 0

        if split_row[7].strip() is not None:
            image_url = split_row[7].strip()
        else:
            image_url = None

        if split_row[8].strip() is not None:
            parents = split_row[8].strip()
        else:
            parents = None

        if split_row[9].strip() is not None:
            string_list_of_child_member_ids = split_row[9].strip()  # produces a string
            list_of_child_member_ids = string_list_of_child_member_ids.split()  # produces a list from the string

            children = [Member(member_id=int(num)) for num in list_of_child_member_ids]
        else:
            children = None

        if split_row[10].strip() is not None:
            string_list_of_spouse_member_ids = split_row[10].strip()
            list_of_spouse_member_ids = string_list_of_spouse_member_ids.split()

            spouse = [Member(member_id=int(num)) for num in list_of_spouse_member_ids]
        else:
            spouse = None

        try:
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
        except:
            import pdb; pdb.set_trace()

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # Create all tables if they haven't been created
    db.create_all()

    # Import different types of data
    load_family_members()
