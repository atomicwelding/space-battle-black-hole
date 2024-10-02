from IEntity import *



class BlackHole(IEntity):
    def __init__(self, mass = 1., R_S = 1.):
        super().__init__(img_path = 'black-hole.png',
                         mass = mass, # blackhole will be centered and isn't moving
                         rr = 0, rtheta = 0,
                         rdot = 0, thetadot = 0)
        self.R_S = R_S

    def update(self, scene, radial_acceleration, dt):
        pass
