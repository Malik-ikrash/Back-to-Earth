import pygame

class State(object):
    def __init__(self,window,state_dict,first_state):
        self.done = False
        self.background = True
        self.window = window
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.state_dict = state_dict
        self.name_state = first_state
        self.state = self.state_dict[self.name_state]

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flipping_states(self):
        current_state = self.name_state
        next_state = self.state.next_state
        self.state.done = False
        self.name_state = next_state
        self.background = True
        self.state = self.state_dict[self.name_state]


    def update(self, time):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flipping_states()
        self.state.update(time)

    def draw(self):
        if self.background:
            self.window.fill('black')
            self.state.draw(self.window)
            self.background = False
        else:
            self.state.draw(self.window)

    def run(self):
        while not self.done:
            time = self.clock.tick(self.fps)
            self.draw()
            self.event_loop()
            self.update(time)
            pygame.display.update()
    
