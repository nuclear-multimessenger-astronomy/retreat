import numpy as np

def treasure_trail(leg_paces, turn_angles, start_bearing=0.0,
                   start_position=(0.0, 0.0), pace_length=75.0):

    leg_paces = np.asarray(leg_paces, dtype=float)
    bearings_rad = np.deg2rad(start_bearing + np.cumsum(turn_angles)) # compass bearings in radians
    leg_lengths = leg_paces * pace_length / 100.0 # convert paces to metres
    east = np.sum(leg_lengths * np.sin(bearings_rad))
    north = np.sum(leg_lengths * np.cos(bearings_rad))

    final_position = np.asarray(start_position, dtype=float) + [east, north]

    return final_position

if __name__ == "__main__":

    np.set_printoptions(precision=2, suppress=True)

    # 100 paces north, then a right turn and 40 paces east.
    print(treasure_trail([100.0, 40.0], [0.0, 90.0]))
    # [30. 75.]