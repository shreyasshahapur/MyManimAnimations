from manim import *


class BasicGraph(VMobject):
    """An undirected graph. Which focuses on aesthetics for teaching purposes.
    Parameters
    ----------
    vertices
        A dictionary containing the vertices names and positions (2D list).
    edges
        A list of edges, specified as tuples ``(u, v)`` where both ``u``
        and ``v`` are the vertices names.
    label_type
        Specifies whether or not the vertices are labeled; if ``None`` vertices
        are unlabeled. If not, it specifies the mobject class of the label
        (default is ``Text``).
    label_default
        A dictionary specifying the default attributes of ``label_type``.
    label_config
        A dictionary containing the vertices names and corresponding attributes
        to that label. It builds on top of the attributes contained in
        label_default.
    vertex_default
        Specifies a mobject instance which will display the vertices.
    vertex_config
        A dictionary containing the vertices names and corresponding mobject
        instance which will display that vertex.
    vertex_and_label_scale
        Scales the size of the vertices and labels together.
    edge_default
        Specifies a mobject instance which will display the edges.
    edge_config
        A dictionary containing the edges and corresponding mobject instance
        which will display that edge.
    .. note::
        If label ``font=futura`` then it will automatically center the text
        for aesthetics. Individual capital letters were centered with reference
        to a circle of ``radius=0.5``.
    Examples
    --------
    First, we create an unlabeled graph.
    .. manim:: UnlabeledGraph
        class UnlabeledGraph(Scene):
            def construct(self):
                graph = BasicGraph(
                    vertices={"A": [0, 0], "B": [1, 0], "C": [1, 1],
                              "D": [0, 1], "E": [-1, 1]},
                    edges=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
                            ("A", "E"), ("D", "E")],
                    label_type=None,
                    vertex_default=Dot()
                )
                self.add(graph)
    We can similarly create labeled graphs.
    .. manim:: LabeledGraph
        class LabeledGraph(Scene):
            def construct(self):
                graph = BasicGraph(
                    vertices={"A": [0, 0], "B": [2, 0], "C": [2, 2],
                              "D": [0, 2], "E": [-1, 1]},
                    edges=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
                           ("A", "E"), ("E", "D")],
                    vertex_and_label_scale=0.75
                )
                self.add(graph)
    We can change certain vertices and edges.
    .. manim:: ChangeConfigs
        class ChangeConfigs(Scene):
            def construct(self):
                graph = BasicGraph(
                    vertices={"A": [0, 0], "B": [2, 0], "C": [2, 2],
                              "D": [0, 2], "E": [-1, 1]},
                    edges=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
                            ("A", "E"), ("E", "D")],
                    vertex_and_label_scale=0.75,
                    edge_config={("A", "B"): DashedLine(),
                                 ("B", "C"): Line(color=BLUE)},
                    vertex_config={"E": Dot(radius=0.3),
                                   "D": Square(side_length=0.7, fill_opacity=1,
                                               fill_color=BLACK)},
                    label_config={"E": {"color": BLACK}},
                )
                self.add(graph)
    We can add nodes and edges to the graph.
    .. manim:: AddingToGraph
        class AddingToGraph(Scene):
            def construct(self):
                vertices = {"A": [0, 0], "B": [2, 0], "C": [0, 2], "D": [2, 2]}
                edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
                g1 = BasicGraph(
                    vertices=vertices,
                    edges=edges,
                    vertex_and_label_scale=0.8,
                )
                self.play(Write(g1))
                self.wait()
                vertices["E"] = [-1, 1]
                vertices["F"] = [1, -2]
                edges.append(("E", "A"))
                edges.append(("E", "C"))
                edges.append(("F", "A"))
                edges.append(("F", "B"))
                g2 = BasicGraph(
                    vertices=vertices,
                    edges=edges,
                    vertex_and_label_scale=0.8,
                )
                BasicGraph.basic_transform_expand(self, g1, g2)
    """

    def __init__(self,
                 vertices={},
                 edges=[],
                 label_type=Text,
                 label_default={"font": "futura"},
                 label_config={},
                 vertex_default=Circle(color=BLUE, radius=0.5, fill_opacity=1,
                                       fill_color=BLACK),
                 vertex_config={},
                 vertex_and_label_scale=1,
                 edge_default=Line().set_stroke(width=6),
                 edge_config={},
                 **kwargs
                 ):
        VMobject.__init__(self, **kwargs)

        # turns the positions into an np array
        vertices = {vertex: np.array(pos + [0]) for vertex, pos in vertices.items()}

        # adds edges
        for (v1, v2) in edges:
            if (v1, v2) in edge_config:
                edge_image = edge_config[(v1, v2)]
            else:
                edge_image = edge_default.copy()
            edge_image.put_start_and_end_on(vertices[v1], vertices[v2])
            self.add(edge_image)

        # Text(letter, font="futura") centered with reference to a circle of radius=0.5
        FUTURA_CENTERING_POS = {
            "A": 0.04 * UP, "B": 0.03 * RIGHT, "C": 0.04 * LEFT, "D": 0.04 * RIGHT,
            "E": 0.01 * DOWN, "F": 0.02 * RIGHT + 0.01 * DOWN, "G": ORIGIN,
            "H": 0.004 * RIGHT, "I": ORIGIN, "J": 0.035 * LEFT, "K": 0.025 * RIGHT,
            "L": 0.025 * RIGHT, "M": 0.02 * UP, "N": ORIGIN, "O": ORIGIN,
            "P": 0.035 * RIGHT + 0.01 * DOWN, "Q": ORIGIN, "R": 0.03 * RIGHT,
            "S": ORIGIN, "T": 0.03 * DOWN, "U": 0.02 * DOWN, "V": 0.045 * DOWN,
            "W": 0.05 * DOWN, "X": 0.01 * DOWN, "Y": 0.03 * DOWN, "Z": ORIGIN
        }

        # adds vertices and labels
        for v in vertices:
            if v in vertex_config:
                vertex_image = vertex_config[v]
            else:
                vertex_image = vertex_default.copy()

            vertex_image.scale(vertex_and_label_scale).shift(vertices[v])
            self.add(vertex_image)

            if label_type is not None:
                if v in label_config:
                    label_attr = label_default.copy()
                    label_attr.update(label_config[v])
                    label_image = label_type(text=v, **label_attr)
                else:
                    label_image = label_type(text=v, **label_default)

                label_image.move_to(FUTURA_CENTERING_POS[v])\
                    .scale(vertex_and_label_scale, about_point=ORIGIN).shift(vertices[v])
                self.add(label_image)

    # transforms graph g1 to g2 (only for removing and adding to the graph)
    @staticmethod
    def basic_transform(self, g1, g2, run_time_in=1, run_time_out=1):
        self.play(FadeIn(g2), run_time=run_time_in)
        self.play(FadeOut(g1), run_time=run_time_out)

    # for adding elements to graph
    @staticmethod
    def basic_transform_expand(self, g1, g2, run_time_in=1, run_time_out=0.05):
        BasicGraph.basic_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)

    # for removing elements from graph
    @staticmethod
    def basic_transform_contract(self, g1, g2, run_time_in=0.05, run_time_out=1):
        BasicGraph.basic_transform(self, g1, g2, run_time_in=run_time_in, run_time_out=run_time_out)