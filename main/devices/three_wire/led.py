class Led:
    def __init__(self, brain, port: str):
        """
        Initializes a new LED instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """

        self.state: bool = False
        self.port_type: str = "three_wire"

        if brain.request_port(port, self.port_type):
            self.port = port
        else:
            raise Exception("Port already in use.")


    def on(self) -> None:
        """
        Turns the LED on.

        :return: None
        """

        self.state = True
    

    def off(self) -> None:
        """
        Turns the LED off.

        :return: None
        """

        self.state = False
    

    def value(self) -> int:
        """
        Gets the value of the LED.

        :return: The value of the LED.
        """

        if self.state:
            return 1
        
        return 0
    

    def set(self, is_set: bool) -> None:
        """
        Sets the value of the LED.

        :return: None
        """

        self.state = is_set