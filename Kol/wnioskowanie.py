import re

text = open("/AI/Zaj2/baza-wiedzy-negacja.txt")

initials = text.read().split("fakty")

text.close()

initialRules, initialFacts = tuple(initials)

rules = [tuple(s2.split(',') for s2 in re.sub(r'\d+\.', '', s.replace("~~", "").replace(" ", "")).split("->"))
         for s in initialRules.split('\n') if s]


def deduce(hypothesis, facts):
    """Funkcja wykonuje wnioskowanie w przód."""
    if hypothesis in facts:
        return True
    changed = True
    while changed:
        changed = False

        for requirements, results in rules:
            if any(r in facts for r in results):
                continue

            if any((r not in facts) ^ r.startswith('~') for r in requirements):
                continue

            changed = True
            for result in results:
                facts.add(result)

    return hypothesis in facts


def deduceRight(hypothesis, facts):
    """Funkcja wykonuje wnioskowanie w tył."""
    if hypothesis in facts:
        return True

    for requirements, results in rules:
        if hypothesis not in results:
            continue

        if any(not deduceRight(r.replace('~', ''), facts) ^ r.startswith('~') for r in requirements):
            continue

        for result in results:
            facts.add(result)

        return True

    return False


for hypothesis in sorted(set(r.replace('~', '') for r in sum(list(sum(list(r), []) for r in rules), []))):
    if deduceRight(hypothesis, set(s.strip() for s in initialFacts.split(','))):
        print(hypothesis, "jest spełnione")
    else:
        print(hypothesis, "nie jest spełnione")