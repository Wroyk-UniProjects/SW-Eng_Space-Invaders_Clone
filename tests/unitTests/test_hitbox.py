from src import hitbox

if __name__ == '__main__':
    # hitbox nr 1
    hitbox1 = hitbox.Hitbox(5, 5, 5)
    print("\nSize of Hitbox 1: " + str(hitbox1.get_size_hitbox()))
    print("Position of Hitbox 1: " + str(hitbox1.get_hitbox_position()))

    # hitbox nr 2
    hitbox2 = hitbox.Hitbox(10, 10, 5)
    print("\nSize of Hitbox 2: " + str(hitbox2.get_size_hitbox()))
    print("Position of Hitbox 2: " + str(hitbox2.get_hitbox_position()))

    #check collision
    collided = hitbox2.is_touching(hitbox1)
    print("\nthey are colliding: " + str(collided))
    hitbox2.check_collide(hitbox1)
