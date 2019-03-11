import os.path
import sys
import glob


def gen_txt_lst(dir_path):
    txt_lst = [os.path.basename(x) for x in glob.glob(os.path.join(dir_path, '*.txt'))]
    inner_dir_lst = [x for x in glob.glob(os.path.join(dir_path, '*')) if os.path.isdir(x)]
    for inner_dir in inner_dir_lst:
        txt_lst.extend(gen_txt_lst(inner_dir))
    return txt_lst


def main(args):
    all_txt_lst = gen_txt_lst(args[0])
    print('txt_lst = {}'.format(all_txt_lst))


if __name__ == '__main__':
    main(sys.argv[1:])
