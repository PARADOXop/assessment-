class hulk:
    def smash(self):
        return "I smash"

class banner:
    def speak(self):
        return "I've got the brains!"


class smarthulk(hulk, banner):
    pass

s1 = smarthulk()
print(s1.smash(), "and", s1.speak())