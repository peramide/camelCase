def main():
    camelCase = input("camelCase: ")
    print(snake_case(camelCase))


def snake_case(camelCase):
    variable_name = ""
    for i in camelCase:

        if i.isupper() == True:
            variable_name += "_" + i
        else:
            variable_name += i

    return variable_name.lower()
                



if __name__ == "__main__":
    main()