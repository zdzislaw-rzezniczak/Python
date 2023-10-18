from przepisy import przepisy


class ModulGlowny:

    def __init__(self):
        pass

    def wyswietl_menu(self):
        print("Wybierz kawę: ")
        for przepis in przepisy:
            print(f'{przepis["id"]} - {przepis["nazwa"]}')


