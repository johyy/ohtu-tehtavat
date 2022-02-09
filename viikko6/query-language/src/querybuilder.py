from matchers import And, HasAtLeast, PlaysIn, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All):
        self._matcher = matcher

    def build(self):
        return self._matcher
    
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
    
    def oneOf(self, apu1, apu2):
        return QueryBuilder(Or(apu1, apu2))

