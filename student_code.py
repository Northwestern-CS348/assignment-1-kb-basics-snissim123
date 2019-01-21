import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        if type(fact) == Fact and not self.facts.count(fact):
            self.facts.append(fact)
        elif type(fact) == Rule and not self.rules.count(fact):
            self.rules.append(fact)
       
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        valid = False
        bindings = ListOfBindings()
        for elem in self.facts:
            miniBindings = match(elem.statement, fact.statement)
            if miniBindings:
                valid = True
                bindings.add_bindings(miniBindings)

        if valid:
            return bindings
        else:
            return False
