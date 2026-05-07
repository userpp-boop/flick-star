def calculate_acceleration(engine_force, velocity, mass, drag_coeff, friction_coeff):
    speed = abs(velocity)
    direction = 1 if velocity >= 0 else -1
    drag_force = drag_coeff * speed**2
    friction_force = friction_coeff * mass * 9.81
    if speed > 0:
        resistance = (drag_force + friction_force) * direction
    else:
        resistance = 0
        if abs(engine_force) > 0:
            resistance = friction_force * (1 if engine_force > 0 else -1)
    net_force = engine_force - resistance
    if speed == 0 and abs(resistance) > abs(engine_force): net_force = 0
    return net_force / mass
