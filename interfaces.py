"""Messing around with Python interfaces."""

class Team:
    def __init__(self, members):
        self.__members = members

    def __repr__(self):                                 # great for debugging, etc.
        return "Team({!r})".format(self.__members)

    def __len__(self):                                  # necessary for the len() method
        return len(self.__members)

    def __contains__(self, member):                     # doesn't seem to be necessary
        return member in self.__members

    def __iter__(self):                                 # makes the objects iterable
        return iter(self.__members)

# instantiate as an example
indians = Team(["ramirez", "gomes", "brantley"])

# sized protocol
print(len(indians))

# container protocol
print("ramirez" in indians)
print("gomes" in indians)
print("santana" not in indians)

# iterable protocol
for member in indians:
    print(member)

# representation protocol
print(indians)
