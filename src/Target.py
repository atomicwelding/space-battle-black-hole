from Ship import Ship
from IEntity import IEntity
from Player import Player
import numpy as np 


class Target(Ship):
    
    def __init__(self, mass, rr, rdot, thetadot):
        super().__init__(img_path = 'placeholder_target.png',
                         mass = mass, rr = rr, rtheta = np.pi, rdot = rdot, thetadot = thetadot)
