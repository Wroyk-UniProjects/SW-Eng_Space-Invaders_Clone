from src import hitbox

if __name__ == '__main__':
    # hitbox ( position_x, position_y, width, length )
    hitbox1 = hitbox.Hitbox(0, 0, 5, 5)
    print("\nSize of Hitbox 1: " + str(hitbox1.get_size_hitbox()))
    print("Position of Hitbox 1: " + str(hitbox1.get_hitbox_position()))

    hitbox2 = hitbox.Hitbox(4, 4, 5, 5)
    print("\nSize of Hitbox 2: " + str(hitbox2.get_size_hitbox()))
    print("Position of Hitbox 2: " + str(hitbox2.get_hitbox_position()))

    # check collision
    collided = hitbox2.is_touching(hitbox1)
    print("\nHitboxes colliding: " + str(collided))
