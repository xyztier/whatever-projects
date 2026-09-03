import random
import training_data_names as Namesets
#      ^^^^^^^^^^^^^^^^^^^ the name here must be the same name as the other file

NEXT_LETTER_ERROR_ATTEMPTS : int = 100

#CONTINUE_TOKEN : str = "Y"
#BREAK_TOKEN : str = "N"

START_TOKEN : str = "^"
NULL_TOKEN : str = "$"

WEIGHT_INCREMENT : int = 1

order : int = 3

min_char_length : int = 3
max_char_length : int = 10


chain : dict[str, dict] = {}


def _build_chain() -> None:
    for name in Namesets.names:
        current_name : str = ""

        for i in range(order):
            current_name += START_TOKEN
        current_name += name.lower()

        for i in range(len(current_name) - order):
            name_key : str = ""

            for j in range(order):
                name_key += current_name[i + j]

            next_letter : str = current_name[i + order]

            #print(i + order)
            #print(len(current_name))

            if ((i + order) == (len(current_name) - order)) and (i != min_char_length):
                next_letter = NULL_TOKEN
                #print("CALLED")

            if name_key not in chain:
                chain[name_key] = {}

            if next_letter not in chain[name_key]:
                chain[name_key][next_letter] = WEIGHT_INCREMENT
            else:
                chain[name_key][next_letter] = chain[name_key][next_letter] + WEIGHT_INCREMENT
                
            
def _get_next_letter(name_key : str) -> str:
    possible_next_letters : dict[str, int] = chain[name_key]

    letters : list[str] = list(possible_next_letters.keys())
    weights : list[int] = list(possible_next_letters.values())

    #print(letters, weights)

    next_letter = random.choices(letters, weights)[0]

    return next_letter


def generate_name() -> str:
    character_count : int = 0
    generated_name : str = ""

    name_key : str = ""
    for _i in range(order):
        name_key += START_TOKEN

    while character_count < max_char_length:
    
        if name_key not in chain:
            break

        next_letter : str = _get_next_letter(name_key)

        if next_letter == NULL_TOKEN:
            if character_count > min_char_length:
                break
            else:
                attempts = 0
                
                while next_letter == NULL_TOKEN:
                    next_letter = _get_next_letter(name_key)
                    
                    attempts += 1
                    if attempts > NEXT_LETTER_ERROR_ATTEMPTS:
                        raise RuntimeError("Name generation exceeded 100 attempts.")

        generated_name += next_letter
        name_key = name_key[1:] + next_letter
        character_count += 1

    return generated_name.capitalize()


#print("(Higher = more realistic name, but recommended is 3, because training data isn't enough. Probably.)")
#order = int(input("Enter level of Order: "))
#min_char_length = int(input("Enter minimum name length: "))
#max_char_length = int(input("Enter maximum name length: "))

#for num in [order, min_char_length, max_char_length]:
    #if num <= 0:
        #print("An entered value is smaller than or equal to 0. Don't do that.")
        #print("Chain is now empty, and you can't generate a name.")
        #break

_build_chain()


if __name__ == "__main__":
    print(generate_name())
    #pass

#print(chain)


#while 1:
    #print("Generated name: %s" % _generate_name())
    #sentinel = input("Continue? %s/%s: " % (CONTINUE_TOKEN, BREAK_TOKEN))
    
    #if sentinel.upper() == CONTINUE_TOKEN:
        #continue
    #elif sentinel.upper() == BREAK_TOKEN:
        #break
    
    #break

