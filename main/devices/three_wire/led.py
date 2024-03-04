class Led:
    state: bool = False
    port: str = ""


    def __init__(self, brain, port: str):
        """
        Initializes a new LED instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """

        if brain.request_port(port):
            self.port = port
        else:
            raise Exception("Port already in use.")


    @staticmethod
    def on() -> None:
        """
        Turns the LED on.

        :return: None
        """

        Led.state = True
    

    @staticmethod
    def off() -> None:
        """
        Turns the LED off.

        :return: None
        """

        Led.state = False
    

    @staticmethod
    def value() -> int:
        """
        Gets the value of the LED.

        :return: The value of the LED.
        """

        if Led.state:
            return 1
        
        return 0
    

    @staticmethod
    def set(is_set: bool) -> None:
        """
        Sets the value of the LED.

        :return: None
        """

        Led.state = is_set