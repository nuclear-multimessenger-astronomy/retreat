from treasure_trail import treasure_trail
import numpy as np

def check_treasure(leg_paces, turn_angles, treasure_position, tolerance=0.99,
                   **trail_kwargs):
    
    final_position = treasure_trail(leg_paces, turn_angles, **trail_kwargs)
    treasure_position = np.asarray(treasure_position, dtype=float)

    offset = treasure_position - final_position
    distance = np.hypot(*offset)
    found = distance <= tolerance

    if found:
        print(f"Congratulations, you found the treasure! It was the friends we made along the way")
    else:
        bearing = np.mod(np.rad2deg(np.arctan2(offset[0], offset[1])), 360.0)
        print(f"No treasure here. It lies {distance:.2f} m away "
              f"on a bearing of {bearing:.0f} deg.")

    return

if __name__ == "__main__":
    leg_paces = np.array([40.0, 25.0, 60.0, 30.0, 15.0, 55.0, 20.0,
                      45.0, 70.0, 35.0, 50.0, 12.0])
    turn_angles = [0.0, 90.0, -135.0, 270.0, 45.0, -60.0, 180.0,
                -315.0, 30.0, 120.0, -45.0, 360.0]

    treasure_position = (-2.2406, -46.8639)

    check_treasure(leg_paces, turn_angles, treasure_position,
                start_bearing=30.0, start_position=(10.0, -5.0),
                pace_length=68.0)