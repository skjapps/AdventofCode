from useful_class import UsefulClass

def day9pt1():
    # Load compressed filesystem
    compressed_fs = list(UsefulClass.read_lines_to_string("assets/txt/day9"))

    # Get the full filesystem
    fileID = 0
    full_fs = []
    for i in range(len(compressed_fs)):
        if i % 2 == 0:
            # print("even")
            for j in range(int(compressed_fs[i])):
                full_fs.append(fileID)
            fileID += 1
        else:
            # print("odd")
            for j in range(int(compressed_fs[i])):
                full_fs.append('.')
    print("Full FS: ", full_fs, "\n")
    full_fs_copy = full_fs.copy()

    # Defrag the filesystem
    defrag_fs_array = []
    for i in range(len(full_fs)):
        # If the item is a number
        if type(full_fs[i]) == int:
            # append the item to defragmented array
            defrag_fs_array.append(full_fs[i])
        # If the item is an empty block
        elif full_fs[i] == "." :
            # move the last item
            last_block = full_fs_copy.pop()
            while full_fs[i] == ".":
                # If the item is a number
                if type(last_block) == int :
                    # move this item to the empty block
                    defrag_fs_array.append(last_block)
                    break
                last_block = full_fs_copy.pop()
        else:
            raise Exception("Logically unreachable...")

    # Clean repeated free block space at end of disk:
    used_space = len(full_fs) - full_fs.count(".")
    # print(used_space)
    # Replace elements from index x to the end with "."
    defrag_fs_array[used_space:] = ['.'] * (len(defrag_fs_array) - used_space)
    print("Defrag FS: ", defrag_fs_array, "\n")

    # Finally, get checksum
    filesystem_checksum = 0
    for i in range(used_space):
        filesystem_checksum += int(defrag_fs_array[i])*i
    print("Filesystem Checksum:", filesystem_checksum)

def day9pt2():
    # Load compressed filesystem
    compressed_fs = list(UsefulClass.read_lines_to_string("assets/txt/day9"))

    # Get the full filesystem
    fileID = 0
    full_fs = []
    for i in range(len(compressed_fs)):
        if i % 2 == 0:
            # print("even")
            for j in range(int(compressed_fs[i])):
                full_fs.append(fileID)
            fileID += 1
        else:
            # print("odd")
            for j in range(int(compressed_fs[i])):
                full_fs.append('.')
    print("Full FS: ", full_fs, "\n")
    full_fs_copy = full_fs.copy()

    # Defrag the filesystem (SMART)
    defrag_fs_array = []
    empty_block_count = 0 # Used in computing available free area
    for i in range(len(full_fs)):
        # If the item is a number
        if type(full_fs[i]) == int:
            # append the item to defragmented array
            defrag_fs_array.append(full_fs[i])
        # While there are empty blocks
        while full_fs[i] == "." :
            # move the last item
            last_block = full_fs_copy.pop()
            while full_fs[i] == ".":
                # If the item is a number
                if type(last_block) == int :
                    # move this item to the empty block
                    defrag_fs_array.append(last_block)
                    break
                last_block = full_fs_copy.pop()
        else:
            raise Exception("Logically unreachable...")

    # Clean repeated free block space at end of disk:
    used_space = len(full_fs) - full_fs.count(".")
    # print(used_space)
    # Replace elements from index x to the end with "."
    defrag_fs_array[used_space:] = ['.'] * (len(defrag_fs_array) - used_space)
    print("Defrag FS: ", defrag_fs_array, "\n")

    # Finally, get checksum
    filesystem_checksum = 0
    for i in range(used_space):
        filesystem_checksum += int(defrag_fs_array[i])*i
    print("Filesystem Checksum:", filesystem_checksum)

# day9pt1()

day9pt2()