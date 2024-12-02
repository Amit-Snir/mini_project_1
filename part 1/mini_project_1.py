
#Defining a main class name "Neuron", costumizing it to have an idle_firing_rate and a throshold for activation
class Neuron:
    def __init__(self, idle_firing_rate=1, threshold=1):
        self.idle_firing_rate = idle_firing_rate
        self.threshold = threshold
        self.actual_firing_rate = 0
# a function to determine weather the neuron fired or not
    def activate(self, stimulus_value=1):
        self.actual_firing_rate = stimulus_value * self.idle_firing_rate
        if self.actual_firing_rate < self.threshold:
            print("neuron didnt fire, threshold wasnt met")
        else:
            print("neuron fired with rate of", self.actual_firing_rate)

#creating a sub class (type a) that is a sensory neuron class
class Sensory(Neuron):
    def __init__(self, idle_firing_rate, threshold, receptor_type):
       super().__init__(idle_firing_rate, threshold)
       self.receptor_type = receptor_type
# a function to determine weather the neuron fired or not based on stimulus match, and detaling what stimuli and power was that
# if neuron didnt fire, mention why
    def Sense_Stimulus(self, stimulus, stimulus_value=1):
        if stimulus == self.receptor_type:
            print("the", self.receptor_type, "receptor received",
                   stimulus,  "with a strength value of", stimulus_value)
            super().activate(stimulus_value)
        else:
            print("Stimuli Doesnt match Receptor")

#sub-sub class (type a) No1, that is a photoreceptor (even though its not a neuron but a receptor cell it will inherite a neuron sub class)
class Photoreceptor(Sensory):
    def __init__(self, idle_fire_rating, threshold, receptor_type="light"):
        super().__init__(idle_fire_rating, threshold, receptor_type)
# only recieves light and can tell what power that light have - none/moderate/strong.
    def light_detector(self, stimulus="light", stimulus_value=1):
        if 0 < stimulus_value < 10:
            print("light level moderate")
        elif stimulus_value > 10:
            print("light level strong")
        else:
            print("no light, neuron didnt fire")

#sub-sub class (type a) No2, a mechanoreceptor
class Mechanoreceptor(Sensory):
    def __init__(self, idle_fire_rating, threshold, receptor_type="pressure"):
        super().__init__(idle_fire_rating, threshold, receptor_type)
#same as the photoreceptor but with pressure, it will tell the amount of power it detects
    def pressure_detection(self, stimulus="pressure", stimulus_value=1):
        if 0 < stimulus_value < 10:
            print("pressure level moderate")
        elif stimulus_value > 10:
            print("pressure level strong")
        else:
            print("no pressure, neuron didnt fire")

#sub class (type b), a motor neuron that can give signals for muscles to contract
class Motor(Neuron):
    def __init__(self, idle_firing_rate, threshold, target_muscle):
       super().__init__(idle_firing_rate, threshold)
       self.target_muscle = target_muscle
# given a stimuli value it will tell if the threshold is met and weather the neuron been activated or not
    def Muscle_control(self, stimulus_value):
        super().activate(stimulus_value)
        if self.actual_firing_rate > self.threshold:
            print("muscle is contracted")
        else:
            print("muscle not conrtacted")

#sub class (type b) No1, a sub class of motor neuron ingaging only a specific type of muscle
class Alpha(Motor):
    def __init__(self, idle_firing_rate, threshold, target_muscle="skeletal muscle"):
        super().__init__(self, idle_firing_rate, threshold, target_muscle="skeletal muscle")
# given a stimulus value it will tell if and in what way was the specific muslce activated
    def Muscle_control(self, stimulus_value):
        super().activate(stimulus_value)
        if self.actual_firing_rate > self.threshold:
            print("skeletal muscle is rapidly and strongly contracted")
        else:
            print("skeletal muscle is not conrtacted")


#sub class (type b) No2, a sub class of motor neuron ingaging only a specific type of muscle 
class Gamma(Motor):
    def __init__(self, idle_firing_rate, threshold, target_muscle="muscle spindle"):
        super().__init__(self, idle_firing_rate, threshold, target_muscle="muscle spindle")
# given a stimulus value it will tell if and in what way was the specific muslce activated
    def Muscle_control(self, stimulus_value):
        super().activate(stimulus_value)
        if self.actual_firing_rate > self.threshold:
            print("muscle spindle is slowly and gradualy contracted")
        else:
            print("muscle spindle is not conrtacted")
