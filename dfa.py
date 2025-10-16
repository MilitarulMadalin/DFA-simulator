class DFA:
    def __init__(self, states, alphabet, transition, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.initial_state = initial_state
        self.final_states = final_states

    def process_word(self, word):
        current_state = self.initial_state

        for symbol in word:
            if symbol not in self.alphabet:
                return False
            
            if (current_state, symbol) not in self.transition:
                return False
            
            current_state = self.transition[(current_state, symbol)]
        
        return current_state in self.final_states


def parse_data(lines):
    section = None
    states = []
    alphabet = []
    transition = {}
    initial_state = None
    final_states = []

    for line in lines:
        line = line.strip()

        if not line:
            continue
        if line.startswith("#"):
            section = line
            continue

        if section == "#states":
            states.append(line)
        elif section == "#initial":
            initial_state = line 
        elif section == "#accepting":
            final_states.append(line)
        elif section == "#alphabet":
            alphabet.append(line)
        elif section == "#transitions":
            # Corect: s0:b>s2  ->  src=s0, symbol=b, dst=s2
            src, rest = line.split(":")
            symbol, dst = rest.split(">")
            transition[(src.strip(), symbol.strip())] = dst.strip()
    
    return DFA(states, alphabet, transition, initial_state, final_states)


def main():
    file_path = "dfa.txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    
    dfa = parse_data(lines)

    word = input("Enter a word: ").strip()

    if dfa.process_word(word):
        print("ACCEPTED")
    else:
        print("REJECTED")


if __name__ == "__main__":
    main()
