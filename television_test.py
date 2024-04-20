import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert tv._status == False
    assert tv._muted == False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power(tv):
    tv.power()
    assert tv._status == True
    tv.power()
    assert tv._status == False

def test_mute(tv):
    tv.mute()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == False

def test_channel_up(tv):
    tv._status = True
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL
    tv._status = False
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MAX_CHANNEL

def test_channel_down(tv):
    tv._status = True
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL
    tv._status = False
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MIN_CHANNEL

def test_volume_up(tv):
    tv._status = True
    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME
    assert tv._muted == False

def test_volume_down(tv):
    tv._status = True
    tv._volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME
    assert tv._muted == False

    tv._volume = Television.MAX_VOLUME
    tv._muted = True
    tv.volume_down()
    assert tv._volume == Television.MAX_VOLUME
    assert tv._muted == False

    tv._status = False
    tv._volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME
    assert tv._muted == False