'''
Implement any one of the following Expert System

Information management
Hospitals and medical facilities
Help desks management
Employee performance evaluation
Stock market trading
Airline scheduling and cargo schedules
'''

# ---------------- EXPERT SYSTEM CLASS ----------------
class ExpertSystem:
    def __init__(self):
        self.facts = {}   # store facts
        self.rules = {}   # store rules

    # add facts
    def add_fact(self, fact, value):
        self.facts[fact] = value

    # add rules
    def add_rule(self, rule, condition):
        self.rules[rule] = condition

    # inference
    def infer(self):
        for rule, condition in self.rules.items():
            if all(self.facts.get(fact) == value for fact, value in condition.items()):
                return rule
        return "No matching rule found"


# ---------------- DRIVER CODE ----------------
expert = ExpertSystem()

# ----------- TAKE FACTS FROM USER -----------
n = int(input("Enter number of facts: "))

for i in range(n):
    fact = input(f"Enter fact {i+1} name: ")
    value = input(f"Enter value for {fact} (True/False): ").lower() == "true"
    expert.add_fact(fact, value)

# ----------- TAKE RULES FROM USER -----------
r = int(input("\nEnter number of rules: "))

for i in range(r):
    rule_name = input(f"\nEnter rule {i+1} decision/output: ")
    cond_count = int(input("How many conditions for this rule? "))

    conditions = {}
    for j in range(cond_count):
        fact = input(f"Enter condition fact {j+1}: ")
        value = input(f"Enter value for {fact} (True/False): ").lower() == "true"
        conditions[fact] = value

    expert.add_rule(rule_name, conditions)

# ----------- INFERENCE -----------
decision = expert.infer()

print("\nDecision:", decision)

# Enter number of facts: 3
# Enter fact 1 name: login_issue
# Enter value for login_issue (True/False): True

# Enter fact 2 name: urgent
# Enter value for urgent (True/False): True

# Enter fact 3 name: network_issue
# Enter value for network_issue (True/False): False

# Enter number of rules: 3

# Enter rule 1 decision/output: Assign to Senior Support
# How many conditions for this rule? 2
# Enter condition fact 1: login_issue
# Enter value for login_issue (True/False): True
# Enter condition fact 2: urgent
# Enter value for urgent (True/False): True

# Enter rule 2 decision/output: Assign to Network Team
# How many conditions for this rule? 1
# Enter condition fact 1: network_issue
# Enter value for network_issue (True/False): True

# Enter rule 3 decision/output: Assign to General Support
# How many conditions for this rule? 1
# Enter condition fact 1: login_issue
# Enter value for login_issue (True/False): True

# Decision: Assign to senior support