"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record:tuple)->str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    
    return record[1]


def convert_coordinate(coordinate:str)->tuple:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    return tuple(coordinate)


def compare_records(azara_record:tuple, rui_record:tuple)->bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    azara_coord = get_coordinate(azara_record)
    rui_coord = rui_record[1]
    return convert_coordinate(azara_coord) == rui_coord


def create_record(azara_record:tuple, rui_record:tuple)->tuple|str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    return (azara_record + rui_record) if compare_records(azara_record, rui_record) else 'not a match'


def clean_up(combined_record_group:tuple)->str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    cleaned_recs = []
    for record in combined_record_group:
        treasure = record[0]
        location = record[2]
        coordinate = record[3]
        quadrant = record[4]
        cleaned_recs.append((treasure, location, coordinate, quadrant))
    return '\n'.join(str(ar) for ar in cleaned_recs) + '\n'