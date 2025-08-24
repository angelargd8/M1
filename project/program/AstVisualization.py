from graphviz import Digraph
import itertools

def render_ast(root, out_png="output/ast.png"):
    dot = Digraph(graph_attr={"rankdir": "TB"})
    counter = itertools.count()

    def nid():
        return f"n{next(counter)}"

    def label(obj):
        cls = type(obj).__name__
        # muestra campos principales abreviados
        if hasattr(obj, "__dict__"):
            return f"{cls}"
        return str(obj)

    def walk(obj):
        node_id = nid()
        dot.node(node_id, label(obj))
        # hijos: dataclass -> recorremos campos
        if hasattr(obj, "__dict__"):
            for k, v in obj.__dict__.items():
                if v is None: continue
                if isinstance(v, list):
                    list_id = nid()
                    dot.node(list_id, f"{k}[]")
                    dot.edge(node_id, list_id)
                    for it in v:
                        cid = walk(it)
                        dot.edge(list_id, cid)
                else:
                    cid = walk(v)
                    dot.edge(node_id, cid, label=k)
        else:
            # literal simple (int/str/bool) rara vez
            pass
        return node_id

    walk(root)
    dot.render(out_png, format="png", cleanup=True)
    return out_png
