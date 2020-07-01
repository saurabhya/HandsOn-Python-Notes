
class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        current = self.head
        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return current

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False


'''
    The most music player software allows users to add songs to
    a playlist. Upon hitting the play button, all the songs in
    the main playlist are played one after the other. Sequential
    playing of the songs can be implemented with queues because
    the first song to be queued is the first song that is to be
    played. This aligns with the FIFO acronym. We will implement
    our own playlist queue to play songs in the FIFO manner.


    Our media player queue will only allow for the addition of
    tracks and a way to play all the tracks in the queue. In a
    full-blown music player, threads would be used to improve
    how the queue is interacted with, while the music player
    continues to be used to select the next song to be played,
    paused, or even stopped. The track class will simulate a
    musical track.
'''
from random import randint

class Track:
    def __init__(self, title = None):
        self.title = title
        self.length = randint(5, 10)
        '''
            Each track holds a reference to the title of the song and also
            the length of the song. The length of the song is a random number
            between 5 and 10. The random module in python provides the randint
            function to enable us to generate the random numbers. The class
            represents any Mp3 track or file that contains music. The random
            length of a track is used to simulate the number of seconds it takes
            to play a song or a track.
        '''
import time
class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.size > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)

track1 = Track("White whistle")
track2 = Track("Butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

print(track1.length)
print(track2.length)

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()