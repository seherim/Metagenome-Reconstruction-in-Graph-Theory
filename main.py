import tkinter as tk
import networkx as netx
import matplotlib.pyplot as pyp
import networkx as nx
import numpy as np
import pandas as pd

from networkx.drawing.layout import bipartite_layout


class MainMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        self.DisplayMenu()
    def CloseWindow(self):
        self.root.destroy()
    def OpenGTHome(self):
        self.CloseWindow()
        GTHome()
    def DisplayMenu(self):
        self.root.geometry("900x900")
        self.root.title("Main Menu")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        self.root.configure(bg="Black")
        title_lbl = tk.Label(self.root,text = "Graph Theory", font=('Century Schoolbook',25))
        title_lbl.config(bg="Black", fg="White")
        title_lbl.place(x=110, y=140)
        title_lbl2 = tk.Label(self.root, text="Project", font=('Century Schoolbook', 25))
        title_lbl2.config(bg="Black", fg="White")
        title_lbl2.place(x=110, y=200)
        grp1 = tk.Label(self.root, text="Emaan Ahmed 21K-3441",font=('Century Schoolbook', 12))
        grp2 = tk.Label(self.root, text="Anas Ghazi 21L-5081", font=('Century Schoolbook', 12))
        grp3 = tk.Label(self.root, text="Seher Imtiaz 21K-3363", font=('Century Schoolbook', 12))
        grp1.config(bg="Black", fg="White")
        grp2.config(bg="Black", fg="White")
        grp3.config(bg="Black", fg="White")
        grp1.place(x=650,y=610)
        grp2.place(x=650, y=640)
        grp3.place(x=650, y=670)
        self.ch_btn = tk.Button(self.root, text="Graph Theory \U00002728Wonders\U00002728", font=('Century Gothic', 18),command=self.OpenGTHome)
        self.ch_btn.config(bg="plum4", fg="white")
        self.ch_btn.place(x=275, y=350)
        self.ch_btn.bind("<Enter>", self.on_enter)
        self.ch_btn.bind("<Leave>", self.on_leave)

        self.root.mainloop()

    def on_enter(self, e):
        self.ch_btn.config(bg="thistle4", fg="ghost white")

    def on_leave(self, e):
        self.ch_btn.config(bg="plum4", fg="ghost white")

def buttonhov(button):
    button.bind("<Enter>", lambda e: button.config(bg="thistle4", fg="ghost white"))
    button.bind("<Leave>", lambda e: button.config(bg="plum4", fg="ghost white"))

class GTHome:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        self.obj = Graphing()
        self.DisplayGT()
    def DisplayComplete(self):
        self.root.destroy()
        self.obj.CompleteG()
    def DisplayPartite(self):
        self.root.destroy()
        self.obj.PartiteG()
    def DisplaySimple(self):
        self.root.destroy()
        self.obj.SimpleG()
    def DisplayHavil(self):
        self.root.destroy()
        self.obj.HavilG()
    def DisplaySafe(self):
        self.root.destroy()
        self.obj.SafeNodeG()
    def CloseWindow(self):
        self.root.destroy()
        # self.obj.destroy()
        MainMenu()



    def DisplayGT(self):
        self.root.geometry("900x900")
        self.root.title("Graph Algorithms")
        self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
        self.root.configure(bg="Black")
        title_lbl = tk.Label(self.root,text = "Simulations of Graph Theory algorithms", font=('Century Gothic',25))
        title_lbl.config(bg="Black", fg="lightpink4")
        simple_btn = tk.Button(self.root,text="Simple Graph", font=('Century Gothic',18),command=self.DisplaySimple)
        complete_btn = tk.Button(self.root, text="Complete Graph", font=('Century Gothic', 18),command=self.DisplayComplete)
        partite_btn = tk.Button(self.root, text="Bi And Tri Partite Graph", font=('Century Gothic', 18),command=self.DisplayPartite)
        havil_btn = tk.Button(self.root,text="Havil Hakimi With Graph", font=('Century Gothic', 18),command=self.DisplayHavil)
        safen_btn = tk.Button(self.root,text="Safe Node Walk",font=('Century Gothic', 18),command=self.DisplaySafe)
        buttonhov(simple_btn)
        buttonhov(complete_btn)
        buttonhov(partite_btn)
        buttonhov(havil_btn)
        buttonhov(safen_btn)
        simple_btn.config(bg="plum4", fg="white")
        complete_btn.config(bg="plum4", fg="white")
        partite_btn.config(bg="plum4", fg="white")
        havil_btn.config(bg="plum4", fg="white")
        safen_btn.config(bg="plum4", fg="white")
        title_lbl.pack(pady=30)
        simple_btn.place(x=250, y=150)
        complete_btn.place(x=250, y=250)
        partite_btn.place(x=250, y=350)
        havil_btn.place(x=250, y=450)
        safen_btn.place(x=250, y=550)
        self.root.mainloop()



class Graphing:
    def CloseWindow(self):
        self.destroy()
        GTHome()

    def SimpleG(self):
        graph = netx.Graph()

        # nodes in the graph
        graphnode = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        graph.add_nodes_from(graphnode)

        E = zip(np.random.choice(list(graphnode), 10), np.random.choice(list(graphnode), 10))
        graph.add_edges_from(E)

        # removes any self loop
        graph.remove_edges_from(netx.selfloop_edges(graph))

        edge = pd.DataFrame([{"s": s} for s in E])
        graph.add_edges_from(edge)

        position = nx.spring_layout(graph, k=1)

        pyp.figure(figsize=(12, 6))
        netx.draw_networkx(graph, position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')

        pyp.title(" Simple Graph ", color='forestgreen', fontsize=18, fontname='Calibri')
        pyp.show()
        GTHome()

    def CompleteG(self):

        graph = netx.Graph()

        # nodes in the graph
        graphnode = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        graph.add_nodes_from(graphnode)

        E = zip(np.random.choice(list(graphnode), 10), np.random.choice(list(graphnode), 10))
        graph.add_edges_from(E)

        # removes any self loop
        graph.remove_edges_from(netx.selfloop_edges(graph))

        cgraph = nx.Graph()
        # code for creating a complete graph
        for node1 in graph.nodes():
            for node2 in graph.nodes():
                if node1 != node2 and not graph.has_edge(node1, node2):
                    cgraph.add_edge(node1, node2)

        position = nx.spring_layout(cgraph, k=1)

        pyp.figure(figsize=(12, 6))
        netx.draw_networkx(cgraph, position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')

        pyp.title(" Complete Graph ", color='forestgreen', fontsize=18, fontname='Calibri')
        pyp.show()
        GTHome()

    def HavilG(self):

        import networkx as nx
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import tkinter as tk
        from tkinter import scrolledtext
        def graphex(gg):
            while True:
                gg = sorted(gg, reverse=True)
                if gg[0] == 0 and gg[-1] == 0:
                    return True

                var = gg[0]
                gg = gg[1:]

                if var > len(gg):
                    return False
                for i in range(var):
                    gg[i] -= 1
                    if gg[i] < 0:
                        return False

        def havelhakimi(degreeseq, text_widget):
            iteration = 0
            text_widget.insert(tk.END, f"Degree Sequence: {degreeseq}\n")
            text_widget.yview(tk.END)
            degreeseq = sorted(degreeseq, reverse=True)
            text_widget.insert(tk.END, f"Degree Sequence: {degreeseq}\n")
            text_widget.yview(tk.END)
            while True:
                degreeseq = sorted(degreeseq, reverse=True)
                if degreeseq[0] == 0 and degreeseq[-1] == 0:
                    return True, degreeseq
                v = degreeseq[0]
                degreeseq = degreeseq[1:]
                if v > len(degreeseq):
                    return False, degreeseq
                for i in range(v):
                    degreeseq[i] -= 1
                    if degreeseq[i] < 0:
                        return False, degreeseq
                iteration += 1
                print(f"Degree Sequence: {degreeseq}")
                degreeseq = sorted(degreeseq, reverse=True)
                text_widget.insert(tk.END, f"Degree Sequence: {degreeseq}\n")
                text_widget.yview(tk.END)

        def open_tkinter_window():
            root = tk.Tk()
            root.title("Havil Hakimi Degree Sequence")
            root.configure(bg="black")
            root.geometry("600x400")
            text_widget = tk.Text(root, width=70, height=40, wrap=tk.WORD, bg="black", fg="forest green",
                                  font=("Calibre", 18))
            text_widget.pack(padx=20, pady=20)
            return root, text_widget

        # Original graph
        graph = nx.Graph()

        # Nodes in the graph
        graph_nodes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        graph.add_nodes_from(graph_nodes)

        # generating random edges
        E = zip(np.random.choice(list(graph_nodes), 10), np.random.choice(list(graph_nodes), 10))
        graph.add_edges_from(E)

        # removing self-loops
        graph.remove_edges_from(nx.selfloop_edges(graph))

        # original degree sequence
        initialdegseqq = list(dict(graph.degree()).values())

        # Open tkinter window
        root, text_widget = open_tkinter_window()

        # Havel-Hakimi process
        exists, new_sequence = havelhakimi(initialdegseqq, text_widget)

        # Close tkinter window
        def close_tkinter_window(root):
            if root:
                root.destroy()

        # initial graph show
        initial_position = nx.spring_layout(graph, k=1)
        plt.figure(figsize=(12, 6))
        nx.draw_networkx(graph, initial_position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')
        plt.title("- Initial Graph -")
        print("Initial Degree Sequence:", initialdegseqq)
        initialseq = "Initial Degree Sequence: " + str(initialdegseqq)
        plt.text(0.5, -0.1, initialseq, ha='center', va='center', transform=plt.gca().transAxes)
        plt.show()

        # Havel-Hakimi process
        # exists, new_sequence = havelhakimi(initialdegseqq, text_widget)

        while exists and not graphex(new_sequence):
            print("Sequence:", new_sequence)
            exists, new_sequence = havelhakimi(new_sequence)

        if exists:
            print("The degree sequence is graphical.")
            print("Constructed Graphical Sequence:", new_sequence)

            # New graph on the modified sequence after Havel-Hakimi
            new_graph = nx.configuration_model(new_sequence, create_using=nx.Graph())

            # Add edges from the original graph to the new graph
            new_graph.add_edges_from(E)

            # Visualize the new graph
            new_position = nx.spring_layout(new_graph, k=1)

            plt.figure(figsize=(12, 6))
            nx.draw_networkx(new_graph, new_position, with_labels=True, node_size=1200, node_color='r',
                             edge_color='gray')
            plt.title("- Graph Constructed Using Havel-Hakimi -")
            finalseq = "Constructed Graphical Sequence: " + str(new_sequence)
            plt.text(0.5, -0.1, finalseq, ha='center', va='center', transform=plt.gca().transAxes)

            plt.show()

        else:
            finalwrong = "The degree sequence is not graphical."
            plt.text(0.4, 0.1, finalwrong, ha='center', va='center', transform=plt.gca().transAxes)

        GTHome()

    def PartiteG(self):
        # hardcoding values for the bipartite (need to change to randomized)
        bp1 = {1, 2, 3, 4, 5}
        bp2 = {6, 7, 8, 9, 10}
        bp3 = {11, 12, 13, 14, 15}

        # forming a random combination
        Ebi = zip(np.random.choice(list(bp1), 10), np.random.choice(list(bp2), 10))

        Ebi = list(Ebi)
        # print(E)

        # printing all the connections/edges
        edge = pd.DataFrame([{"s": bp1, "t": bp2} for bp1, bp2 in Ebi])
        # print(edge)

        # establishing our graph - directed graph
        graph = netx.DiGraph()
        graph.add_nodes_from(bp1, bipartite=0)
        graph.add_nodes_from(bp2, bipartite=2)

        graph.add_edges_from(tuple(x) for x in edge.values)
        # print(graph.edges)

        # for tripartite graphs
        Etri = zip(np.random.choice(list(bp1), 10), np.random.choice(list(bp2), 10), np.random.choice(list(bp3), 10))

        Etri = list(Etri)

        # Printing all the connections/edges for tripartite graph
        edgestri = pd.DataFrame([{"s": s, "t": t, "u": u} for s, t, u in Etri])

        graphtri = netx.DiGraph()
        graphtri.add_nodes_from(bp1, bipartite=0)
        graphtri.add_nodes_from(bp2, bipartite=1)
        graphtri.add_nodes_from(bp3, bipartite=2)
        edges_tri = [(row['s'], row['t']) for _, row in edgestri.iterrows()] + [(row['t'], row['u']) for _, row in
                                                                                edgestri.iterrows()]

        graphtri.add_edges_from(edges_tri)

        positionbp = bipartite_layout(graph, bp1)
        positionbp1 = {node: (1, i) for i, node in enumerate(bp1)}
        positionbp2 = {node: (2, i) for i, node in enumerate(bp2)}
        positionbp3 = {node: (3, i) for i, node in enumerate(bp3)}
        positiontri = {**positionbp1, **positionbp2, **positionbp3}

        # Drawing bipartite graph
        pyp.figure(figsize=(12, 6))
        pyp.subplot(1, 2, 1)
        netx.draw_networkx(graph, positionbp, with_labels=True, node_size=1200, node_color='m', edge_color='r',
                           arrowsize=20)
        pyp.title("Bipartite Graph")

        # Drawing tripartite graph
        pyp.subplot(1, 2, 2)
        netx.draw_networkx(graphtri, positiontri, with_labels=True, node_size=1200, node_color='c', edge_color='b',
                           arrowsize=20)
        pyp.title("Tripartite Graph")

        pyp.show()
        GTHome()

    def SafeNodeG(self):
        GTHome()

MainMenu()
