def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    _, src, dst = parts

    if src == dst:
        return

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())
