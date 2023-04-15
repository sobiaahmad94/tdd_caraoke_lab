class Room:
    def __init__(self, input_name, input_room_capacity):
        self.name = input_name
        self.room_capacity = input_room_capacity
        self.songs = []
        self.guests = []

    def room_has_name(self):
        return self.name
    
    def add_song(self, song_1):
        self.songs.append(song_1)
        return len(self.songs)
    
    def check_in_guest(self, guest_3):
        self.guests.append(guest_3)
        return len(self.guests) 
    
    def check_out_guest(self, guest_to_check_out):
        if guest_to_check_out in self.guests:
            self.guests.remove(guest_to_check_out)
            return True
        else:
            return False
        
room_1 = Room("Room A", 50)
room_2 = Room("Room B", 75)
room_3 = Room("Room C", 100)
