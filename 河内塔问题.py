def movetower(height, fromhole, withhole, tohole):
    if height >= 1:
        movetower(height-1, fromhole, tohole, withhole)
        movedisk(height, fromhole, tohole)
        movetower(height-1, withhole, fromhole, tohole)

def movedisk(disk, fromhole, tohole):
    print(f"move disk[{disk}] from{fromhole} to{tohole}")

movetower(8, "#a", "#b", "#c")