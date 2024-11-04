import ontoweaver

node = ("Source:1", "Source", {"p1":"z"})

edge = ("Link:0", "Source:1", "Target:2", "Link", "")

class Source(ontoweaver.base.Node):
    pass
class Target(ontoweaver.base.Node):
    pass
class Link(ontoweaver.base.Edge):
    @staticmethod
    def source_type():
        return Source
    @staticmethod
    def target_type():
        return Target

serializer = ontoweaver.serialize.All()

s = Source.from_tuple(node, serializer)
l =   Link.from_tuple(edge, serializer)

assert(str(s) == "Source:1Source{'p1': 'z'}")
assert(str(l) == "Link:0Source:1Target:2Link")


serializer = ontoweaver.serialize.ID()

s = Source.from_tuple(node, serializer)
l =   Link.from_tuple(edge, serializer)

assert(str(s) == "Source:1")
assert(str(l) == "Link:0Source:1Target:2")


serializer = ontoweaver.serialize.IDLabel()

s = Source.from_tuple(node, serializer)
l =   Link.from_tuple(edge, serializer)

assert(str(s) == "Source:1Source")
assert(str(l) == "Link:0Source:1Target:2Link")

