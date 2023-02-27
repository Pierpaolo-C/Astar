from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock
from node import Node
from a_star import AStar



    

# This is the main class of the program. 
# It inherits from Kivy's GridLayout class, and has several properties and methods
class Grid(GridLayout):
    rows = 35
    cols = 35
    speed = NumericProperty(0.0)
    running = BooleanProperty(False)

    #  This method is called when an instance of the Grid class is created.
    #  It sets up the grid by creating and adding Node widgets to the GridLayout.
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        # Add the grid of nodes to the right side of the layout
        self.nodes = []
        for row in range(self.rows):
            self.nodes.append([])
            for col in range(self.cols):
                node = Node(row, col)
                node.bind(on_release=self.node_clicked)
                self.add_widget(node)
                self.nodes[row].append(node)
        self.start_node = None
        self.end_node = None
        self.barrier_nodes = set()
        self.algorithm = None
        self.path = None
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_up=self.on_keyboard_up)

    # This method is called when a Node widget is clicked.
    # It sets the start or end node if one hasn't been set already, adds or removes a barrier node,
    # or does nothing if the clicked node is already the start or end node.
    def node_clicked(self, node):
        if not self.start_node:
            self.start_node = node
            self.start_node.color = Node.START_COLOR
        elif not self.end_node:
            self.end_node = node
            self.end_node.color = Node.END_COLOR
        else:
            if node in self.barrier_nodes:
                self.barrier_nodes.remove(node)
                node.color = Node.EMPTY_COLOR
            elif node == self.start_node or node == self.end_node:
                pass
            else:
                self.barrier_nodes.add(node)
                node.color = Node.BARRIER_COLOR
    # This method is called when the "Start" button is clicked. 
    # It creates an instance of the AStar class, passing in the current state of the grid, and sets up a clock to run the algorithm at regular intervals.
    def start_algorithm(self):
        if self.running:
            return
        self.algorithm = AStar(self.nodes, self.start_node, self.end_node, self.barrier_nodes)
        self.running = True
        Clock.schedule_interval(self.step_algorithm, self.speed)

    # This method is called by the clock set up in start_algorithm().
    # It runs one step of the A* algorithm, and stops the clock and draws the path when the algorithm finishes.
    def step_algorithm(self, dt):
        if self.algorithm.finished:
            self.path = self.algorithm.reconstruct_path()
            self.draw_path()
            self.running = False
            return False
        else:
            self.algorithm.step()
            return True
        
    # This method is called when the A* algorithm finishes. 
    # It sets the color of each node in the path to a different color, so that it's easy to see the path the algorithm found.
    def draw_path(self):
        if not self.path:
            return
        for node in self.path:
            if node != self.start_node and node != self.end_node:
                node.color = Node.PATH_COLOR
    
    # This method is called when enter button is pressed. 
    # It resets the state of the grid and stops the algorithm if it's running.
    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node = self.nodes[row][col]
                node.color = Node.EMPTY_COLOR
        self.start_node = None
        self.end_node = None
        self.barrier_nodes = set()
        self.algorithm = None
        self.path = None
        self.running = False

    # This method is called to allow the user to interact with the keyboard
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None
    
    # This method is called when the user interact with the app.
    # Spacebar will start the algorithm, enter will reset it.
    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'spacebar':
            print("space")
            self.start_algorithm()
        elif keycode[1] == 'enter':
            self.reset()
        return True
    
    def on_menu_button_pressed(self):
        print("BUTTON")
        self.menu_widget.opacity = 0

# This is the main class of the program, and is responsible for creating the Grid instance
class AStarApp(App):
    #This method is called by the App class to create the UI. It simply returns an instance of the Grid class.
    def build(self):
        return Grid()

if __name__ == '__main__':
    AStarApp().run()
