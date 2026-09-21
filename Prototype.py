# NEURA v1.0 - Prototype Interpreter
# Founder & Lead Architect: Usman - Multan, Pakistan
# The first Agent-Native, Multi-Human-Language Lang

import re

# --- OMNI-LINGUAL DICTIONARY (Ultimate Feature) ---
KEYWORD_MAP = {
    'socho': 'think',
    'karo': 'do',
    'behtar': 'evolve',
    'banao': 'evolve',
    'agar': 'if',
    'fail': 'fail',
    'zaban': 'language',
    'maqsad': 'goal',
    'jawaab': 'respond',
    'do': 'do',
}

class Agent:
    def __init__(self, name, props):
        self.name = name
        self.props = props
        self.memory = []
        print(f"[NEURA] Agent '{self.name}' zinda ho gaya. Maqsad: {props.get('maqsad','')}")

    def socho(self, thought):
        # This is where LLM reasoning will plug in later
        print(f"[{self.name}] Socho (think): {thought}")
        self.memory.append(thought)
        return f"thinking about: {thought}"

    def karo(self, action):
        print(f"[{self.name}] Karo (do): {action}")
        # Simulate success/failure for self-evolution
        if "fail" in action:
            self.behtar_bano()
        else:
            print(f"--> Action successful: {action}")

    def behtar_bano(self):
        print(f"[{self.name}] Behtar Bano! (Self-Evolving...)")
        print(f"--> Agent is rewriting its own logic to be better.")

def parse_neura(code):
    # Simple parser for v0.1
    code = code.lower()
    # Extract agent
    match = re.search(r'agent\s+(\w+)\s*\{([^}]+)\}', code, re.DOTALL)
    if not match:
        print("NEURA Error: 'agent' block nahi mila")
        return

    agent_name = match.group(1)
    body = match.group(2)

    # Get maqsad
    maqsad_match = re.search(r'maqsad\s*:\s*[\'"]([^\'"]+)', body)
    props = {'maqsad': maqsad_match.group(1) if maqsad_match else 'No goal'}

    agent = Agent(agent_name, props)

    # Find socho block
    socho_match = re.search(r'socho\s*\{([^}]+)\}', body)
    if socho_match:
        agent.socho(socho_match.group(1).strip())

    # Find karo block
    karo_match = re.search(r'karo\s*\{([^}]+)\}', body)
    if karo_match:
        agent.karo(karo_match.group(1).strip())

# --- RUN YOUR FIRST NEURA PROGRAM ---
if __name__ == "__main__":
    code = """
    agent MultanBot {
      zaban: urdu, english
      maqsad: 'Dukan ke liye bot'
      socho { customer kya chahta hai? }
      karo { jawaab do }
    }
    """
    parse_neura(code)
