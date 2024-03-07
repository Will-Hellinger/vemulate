import time


FORWARD: str = "forward"
REVERSE: str = "reverse"
VOLT: str = 'volt'
DEGREES: str = 'degrees'

class GearSetting:
    RATIO_18_1: str = "18:1"
    RATIO_36_1: str = "36:1"
    RATIO_6_1: str = "6:1"


class Motor:
    def __init__(self, brain, port: str, gear_setting: str = "18:1", reverse: bool = False) -> None:
        """
        Initializes a new LED instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """
        self.reverse = reverse

        match gear_setting:
            case "18:1":
                self.rpm = 200
            case "36:1":
                self.rpm = 100
            case "6:1":
                self.rpm = 600
            case _:
                raise Exception("Invalid gear setting.")
        
        self.spinning: bool = False
        self.direction: str = "forward"
        self.motor_rotation: int = 0
        self.voltage: float = 0.0
        self.start_spinning: float = 0.0
        self.port_type: str = "full"

        if brain.request_port(port, self.port_type):
            self.port = port
        else:
            raise Exception("Port already in use.")


    def set_reversed(self, is_reversed: bool) -> None:
        """
        Sets whether the motor is reversed.

        :param is_reversed: Whether the motor is reversed.
        :return: None
        """

        self.reverse = is_reversed
    

    def set_velocity(self, velocity: int) -> None:
        """
        Sets the velocity of the motor.

        :param velocity: The velocity to set.
        :return: None
        """

        self.rpm = velocity
    

    def reset_rotation(self) -> None:
        """
        Resets the rotation of the motor.

        :return: None
        """

        self.motor_rotation = 0
    

    def rotation(self) -> int:
        """
        Gets the rotation of the motor.

        :return: The rotation of the motor.
        """

        return self.motor_rotation
    

    def set_rotation(self, rotation: int) -> None:
        """
        Sets the rotation of the motor.

        :param rotation: The rotation to set.
        :return: None
        """

        if rotation < 0:
            rotation = (rotation * -1)

        if rotation > 360:
            self.motor_rotation = rotation % 360

        self.motor_rotation = rotation
    

    def spin(self, direction: str, volts: float = 10.0, unit: str = VOLT) -> None:
        """
        Spins the motor.

        :return: None
        """

        if unit != VOLT:
            raise Exception("Invalid unit.")
        
        if volts < -12 or volts > 12:
            raise Exception("Invalid voltage.")

        self.voltage = volts
        self.direction = direction
        self.spinning = True
        self.start_spinning = time.time()
    

    def stop(self) -> None:
        """
        Stops the motor.

        :return: None
        """

        if self.spinning:
            rotation_amount = round((time.time() - Motor.start_spinning) * ((Motor.rpm * 360) * 60))

            self.motor_rotation += rotation_amount

            if self.motor_rotation > 360:
                self.motor_rotation = Motor.motor_rotation % 360

        self.spinning = False
    

    def spin_for(self, direction: str, amount: int, unit: str) -> None:
        """
        Spins the motor for a certain amount.

        :direction: The direction to spin the motor.
        :amount: The amount to spin the motor.
        :unit: The unit to spin the motor.
        :return: None
        """

        if unit != DEGREES:
            raise Exception("Invalid unit.")
        
        if (self.motor_rotation + amount) > 360:
            self.motor_rotation = (Motor.motor_rotation + amount) % 360
        else:
            self.motor_rotation += amount

        self.direction = direction
        self.spinning = True

        time_to_spin: float = amount / (self.rpm * 360 * 60)

        print(time_to_spin)

        while time.time() < time_to_spin:
            time.sleep(0.001)
    

    def spin_to_position(self, amount: int, unit: str) -> None:
        """
        Spins the motor to a certain position.

        :amount: The amount to spin the motor.
        :unit: The unit to spin the motor.
        :return: None
        """

        if unit != DEGREES:
            raise Exception("Invalid unit.")
        
        self.motor_rotation = amount
        self.spinning = True

        time_to_spin: float = (self.motor_rotation - amount) / (self.rpm * 360 * 60)

        if time_to_spin < 0:
            time_to_spin = (time_to_spin * -1)

            time_to_spin = 360 - (time_to_spin % 360)

        while time.time() < time_to_spin:
            time.sleep(0.001)