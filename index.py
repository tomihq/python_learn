def main():
    print("¡Welcome to my first chatbot with Python!");
    print("Please, select one of the options below: ");
    menu();

def render_menu_items():
    for idx, opt in enumerate(MENU_OPTIONS):
      print(int(idx+1),":", str(opt));
    pass;


def welcome():
    print("¡Welcome!");
    return 'ok';

def call_administrator():
    print("You called an administrator, please hold on...");
    pass;


def no_such_action():
    print("Invalid option selected");
    pass

def menu():
   render_menu_items();
   while True:
        selection = input("Your selection: ")
        function_to_execute = FUNC_MENU_OPTIONS.get(selection, no_such_action)
        function_to_execute();


MENU_OPTIONS = ["Welcome", "Call Administrator", "Salir"];
FUNC_MENU_OPTIONS = {"1": welcome, "2": call_administrator, "3": exit};
main();