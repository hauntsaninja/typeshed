from serial.serialutil import SerialBase

class Serial(SerialBase):
    def open(self) -> None: ...
    def read(self, size: int = ...) -> bytes: ...
    @property
    def in_waiting(self) -> int: ...
    def reset_input_buffer(self) -> None: ...
    def reset_output_buffer(self) -> None: ...
    @property
    def cts(self) -> bool: ...
    @property
    def dsr(self) -> bool: ...
    @property
    def ri(self) -> bool: ...
    @property
    def cd(self) -> bool: ...
    def set_buffer_size(self, rx_size: int = ..., tx_size: int | None = ...) -> None: ...
    def set_output_flow_control(self, enable: bool = ...) -> None: ...
    @property
    def out_waiting(self) -> int: ...
    def cancel_read(self) -> None: ...
    def cancel_write(self) -> None: ...
