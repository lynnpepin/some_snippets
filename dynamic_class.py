# TODO
# This is a problem I've wanted a snippet for, but have not solved yet!
# WIP!!!
class ExampleGamepad:
    """
    An example of a gamepad.
    
    We want to keep track of an arbitrary number of buttons (A, B, etc.),
    and how they changed in the past tick.
    
    E.g. "A was pressed this tick, A is held, A was released this tick"
    
    In a platformer, this may correspond to:
     * Start a jump
     * Continue to rise
     * When A is released, cut upwards velocity.
       (Violates physics, but allows for greater control of jump height!)
    
    This code should be easy and quick to extend for an arbitrary number of keys,
    but we also *don't* want to use dicts extensively.
    (E.g. we'd prefer to do gamepad.A_just_pressed rather than gamepad["A_just_pressed"]
    """
    def __init__(self, A = ["K_SPACE"], B = ["K_LSHIFT"])
        """
        :param A: List of str, representing keys that count as "A"
        :param B: List of str, representing keys that count as "B"
        
        This is similar to how PyGame represents keys, but can't actually be run.
        """
        # A_keys used to map keys to variables
        self.A_keys = A
        self.B_keys = B
        # A_pressed should be True while A is pressed
        self.A_pressed = False
        self.B_pressed = False
        # A_just_pressed should be True the first tick A is pressed
        self.A_just_pressed = False
        self.B_just_pressed = False
        # A_released should be True the first tick A is pressed
        self.A_released = False
        self.B_released = False
        # Imagine repeating this for every key!
    
    def pressed_keys(self, keys=[""]):
        """
        :param keys: List of string, representing keys that have been pressed.
        """
        
        for key in keys:
            if A_keys 
