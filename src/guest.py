class Guest:
    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age
        self.rooms = []
        

    def guest_has_name(self):
        return self.name
    
    def guest_has_age(self):
        return self.age
    
    def add_room(self, room_1):
        self.rooms.append(room_1)
        return len(self.rooms)


guest_1 = Guest("Troy Barnes", 30)
guest_2 = Guest("Abed Nadir", 31)
guest_3 = Guest("Annie Edison", 29)