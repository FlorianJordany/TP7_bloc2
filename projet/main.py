# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
from context import mes_routes, config
from projet.mes_routes.client_route import app

session = config.SessionLocal()
app.include_router(mes_routes.mon_router)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} test modification')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/