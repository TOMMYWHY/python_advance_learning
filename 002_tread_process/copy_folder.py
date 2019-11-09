import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)

    new_f.close()


def main():
    pass
    # get  folder name
    old_folder_name = input("enter folder name: ")

    # create new folder
    try:
        new_folder_name = old_folder_name + "[_copy]"
        os.mkdir(new_folder_name)
    except Exception:
        pass

    # get all files name listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # create process pool
    pool = multiprocessing.Pool(5)

    # copy to new folder
    for file_name in file_names:
        pool.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
