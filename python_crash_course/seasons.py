from datetime import date, datetime
import sys
import inflect

# --- DEFINING CONSTANTS --- #
HOURS = 24
MINUTES = 60


def main():

    p = inflect.engine()

    # --- CONVERT THE NUMBER OF MINUTES RETURNED INTO WORDS WITHOUT THE "AND" --- #
    words = p.number_to_words(calculate_date_difference(), andword="")

    # --- PRINT THE RESULTING WORD IN A SENTENCE MIMICING THE RENT SONG --- #
    print(f"{words.capitalize()} minutes")


def get_birthday():
    """
    Gets the user's birthday and validates the input.\n
    Returns the birthday in %Y-%m-%d format.
    """

    # --- ASK FOR THE USERS BIRTHDAY --- #
    birthday = input("What is your birtday? Format YYYY-MM-DD: ")

    # --- TRY IF THE DATE INPUT IS A VALID DATE. RETURN AS A STRING IF VALID --- #
    # --- THE BIRTHDAY STRING WOULD LOOK LIKE SUCH "1991-04-12 00:00:00" --- #
    try:
        birthday = datetime.strptime(birthday, "%Y-%m-%d")
        return str(birthday)

    # --- IF IT IS NOT VALID, PRINT AN ERROR MESSAGE AND EXIT THE PROGRAM --- #
    except ValueError:
        print("Sorry, that is in the incorrect format. Try again!")
        sys.exit(-1)


def calculate_date_difference():
    """Calculates the difference between today's date and the users birthday as an integar (in minutes)."""

    # --- RETURN THE DIFFERENCE BETWEEN TODAY'S DATE AND THE DATE PART OF THE BIRTHDAY AS A STRING --- #
    # --- THE DIFFERENCE STRING WOULD LOOK LIKE SUCH "100 days, 00:00:00" --- #
    difference = str(date.today() - date.fromisoformat(get_birthday()[:-9]))

    # --- TRY IF THE STRING CONTAINS NUMBERS I.E. MORE THAN 1 DAY SINCE TODAY --- #
    # --- CONVERT THE NUMBERS (WHICH ARE DAYS) TO MINUTES AND RETURN THAT --- #
    try:
        return int(difference[:-14]) * HOURS * MINUTES

    # --- IF THE DATE IS TODAY OR YESTERDAY, RETURN 1 DAY --- #
    except ValueError:
        return 1 * HOURS * MINUTES


if __name__ == "__main__":
    main()
