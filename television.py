class Television:
    """A class representing a Television."""
    
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize default instance variables."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off."""
        self._status = not self._status

    def mute(self):
        """Mute or unmute the TV."""
        self._muted = not self._muted

    def channel_up(self):
        """Increase the TV channel."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the TV channel."""
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        """Increase the TV volume."""
        if self._status:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
                self._muted = False

    def volume_down(self):
        """Decrease the TV volume."""
        if self._status:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
                self._muted = False

    def __str__(self):
        """Return a string representation of the TV object."""
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"