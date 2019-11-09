import os
import multiprocessing


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # add to queue the result
    queue.put(file_name)


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
    # print(file_names)

    # create process pool
    pool = multiprocessing.Pool(5)

    # create a Queue
    queue = multiprocessing.Manager().Queue()

    # copy to new folder
    for file_name in file_names:
        pool.apply_async(copy_file, args=(queue, file_name, old_folder_name, new_folder_name))

    pool.close()
    # pool.join()

    # display processing
    all_file_num = len(file_names)
    copy_file_count = 0
    while True:
        filename = queue.get()
        # print("copy: %s complete ~!" % filename)
        copy_file_count +=1
        print("\r copying... %.2f%%" % (copy_file_count* 100 / all_file_num),end="" )
        if copy_file_count >= all_file_num:
            break
    print()



if __name__ == '__main__':
    main()
