from model import llm
from model import vending_machine
from time import sleep

def router(decision):
    if decision == "ReAct":
        return
    if decision == "Sleep":
        sleep(1000)

def simulate_vending_machine_actions():
    pass

def main():
    while True:
        decision = llm.invoke("What should I do next? (ReAct/Sleep)")
        router(decision)


if __name__ == "__main__":
    main()
