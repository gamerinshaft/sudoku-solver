import math
import copy
import data

def instead_None_to_nums(data):
    data_buff = data
    for x in range(9):
        for y in range(9):
            if gnum(x,y,data_buff) is None:
                data_buff[math.floor(y/3)][math.floor(x/3)][y%3][x%3] = list(range(1,10))
    return data_buff

def is_correct_value_in_frame(data):
    for x in range(9):
        for y in range(9):
            for c in range(1,10):
                if not c in get_own_col(x,y,data):
                    return False
                if not c in get_own_row(x,y,data):
                    return False
    return True
def is_no_array_in_frame(data):
    for x in range(9):
        for y in range(9):
            if type(gnum(x,y,data)) is list:
                return False
    return True

def print_map(data, *args):
    map = ""
    for y in range(9):
        if y % 3 == 0:
            map += "-------------------------\n"
        for x in range(9):
            if x % 3 == 0:
              map += "| "
            if type(gnum(x,y,data)) is list:
              map += "* "
            else:
                if args and x == args[0] and y == args[1]:
                    map += str(gnum(x,y,data)) + "!"
                else:
                    map += str(gnum(x,y,data)) + " "
            if x == 8:
              map += "|\n"
    map += "-------------------------\n"

    print(map)

def print_frame_of_map(f):
    map = "---------\n"
    for i in range(3):
        map += "| "
        for j in range(3):
            if f[i][j] is None or type(f[i][j]) is list:
                map += "* "
            else:
                map += str(f[i][j])
                map += " "
        map += "|\n"
    map += "---------\n"
    print(map)

def print_line_of_map(line):
    map = "---------------------\n"
    map += "| "
    for i in range(len(line)):
        if type(line[i]) is list:
            map += "* "
        else:
            map += str(line[i]) + " "
    map += "|\n---------------------\n"
    print(map)

def get_own_frame(x,y,data):
    px = math.floor(x/3)
    py = math.floor(y/3)
    return data[py][px]

def get_own_row(x,y,data):
    array = []
    px = math.floor(x/3)
    py = math.floor(y/3)
    for i in range(3):
        array += data[py][i][y%3]
    return array

def get_own_col(x,y,data):
    array = []
    px = math.floor(x/3)
    py = math.floor(y/3)
    for i in range(3):
        for j in range(3):
            array.append(data[i][px][j][x%3])
    return array

def is_exist_number_in_frame(value, frame):
    for row in range(len(frame)):
      for i in range(3):
          if frame[row][i] is type(frame[row][i]) is list:
              continue
          if frame[row][i] == value:
              return True
    return False

def is_exist_number_in_line(value, line):
    for i in range(len(line)):
        if line[i] == value:
            return True
    return False

def is_duplicate_in_frame(frame):
    b = []
    for y in range(3):
        for x in range(3):
            if type(frame[x][y]) is not list:
                if frame[x][y] in b:
                    return True
                else:
                    b.append(frame[x][y])
    return False

def is_duplicate_in_line(line):
    b = []
    for i in range(9):
        if type(line[i]) is not list:
            if line[i] in b:
                return True
            else:
                b.append(line[i])
    return False

def check_reservation(frame):
    b = []
    r = []
    already_check_value = []
    list_count = 0
    for y in range(3):
        for x in range(3):
            if type(frame[y][x]) is list:
                list_count +=1
            b.append(frame[y][x])
    for i in range(9):
        if type(b[i]) is list:
            if list_count > b.count(b[i]) and len(b[i]) == b.count(b[i]) and b[i] not in already_check_value:
                rd = {"value": b[i], "position": []}
                for x in range(9):
                    if b[i] == b[x]:
                        rd["position"].append({"x": x%3, "y": math.floor(x/3)})
                r.append(rd)
                already_check_value.append(b[i])
    # if r:
        # print_frame_of_map(frame)
        # print(r)
    return r

def check_number_in_frame(value, frame, x, y):
    for i in range(len(frame)):
        for j in range(len(frame[i])):
            if x%3 == i and y%3 == j:
                continue
            elif type(frame[j][i]) is list:
                if value in frame[j][i]:
                    return False
            else:
                if frame[j][i] == value:
                    return False
    # print_frame_of_map(frame)
    # print("Hit with frame Check!")
    return True

def check_number_in_line(value, line, x, y, matrix):
    for i in range(len(line)):
        if matrix == "row":
            if x == i:
                continue
        else:
            if y == i:
                continue
        if type(line[i]) is list:
                if value in line[i]:
                    return False
        else:
                if line[i] == value:
                    return False
    # print_line_of_map(line)
    # print("Hit with " + str(matrix) + " check!")
    return True

def find_array_in_map(data, dx, dy):
    for y in range(9):
        for x in range(9):
            if y >= dy and x > dx:
                v = gnum(x,y,data)
                if type(v) is list:
                    return {"x": x, "y": y, "list": v}
    return False

def gnum(x,y, data):
        return data[math.floor(y/3)][math.floor(x/3)][y%3][x%3]

def test():
    print("\nTest Frames mapping...")
    print_map(data)
    print("Test Frame mapping... 【2,3】")
    print_frame_of_map(get_own_frame(2,3, data))
    print("Test row mapping... 【0,1】")
    print_line_of_map(get_own_row(0,1, data))
    print(check_number_in_line(2, get_own_row(0,1, data), 0,1, "row"))
    print("Test col mapping... 【3,3】")
    print_line_of_map(get_own_col(3,3, data))

data = instead_None_to_nums(data.q5)
# test()

def recursive_resolve_method(d, depth):
    buff_data = copy.deepcopy(d)
    isChange = True
    while isChange:
        isChange = False
        for y in range(9):
            for x in range(9):
                if x % 3 == 0 and y % 3 == 0:
                    f = get_own_frame(x,y, buff_data)
                    cr = check_reservation(f)
                    if cr:
                        for c in cr:
                            for my in range(3):
                                for mx in range(3):
                                    bd = buff_data[math.floor(y/3)][math.floor(x/3)][my][mx]
                                    if type(bd) is list and bd != c["value"]:
                                        # print_frame_of_map(f)
                                        for cv in c["value"]:
                                            # print("value:" + str(c["value"]))
                                            # print("TF:" + str( bd is c["value"]))
                                            # print("mx:" + str(mx) + " my:" + str(my))
                                            # print("buff_data:" + str(bd))
                                            if cv in bd:
                                                bd.remove(cv)
                                                isChange = True
                num = copy.deepcopy(gnum(x,y,buff_data))
                if type(num) is list:
                    if len(num) == 1:
                        # print("Hit with only Num")
                        # print("x:" + str(x) + " y:" + str(y))
                        buff_data[math.floor(y/3)][math.floor(x/3)][y%3][x%3] = num[0]
                        if is_duplicate_in_line(get_own_row(x,y,buff_data)) or is_duplicate_in_line(get_own_col(x,y,buff_data)) or is_duplicate_in_frame(get_own_frame(x,y,buff_data)):
                            return False
                        isChange = True
                        # print_map(buff_data, x,y)
                        # print_map(buff_data)
                    else:
                        for i in range(1,10):
                            if is_exist_number_in_frame(i, get_own_frame(x,y, buff_data)) or is_exist_number_in_line(i, get_own_row(x,y, buff_data)) or is_exist_number_in_line(i, get_own_col(x,y, buff_data)):
                                if type(gnum(x,y,buff_data)) is list and i in gnum(x,y,buff_data):
                                    buff_data[math.floor(y/3)][math.floor(x/3)][y%3][x%3].remove(i)
                                    isChange = True
                            else:
                                if check_number_in_frame(i, get_own_frame(x,y, buff_data), x, y) or check_number_in_line(i, get_own_row(x,y, buff_data), x, y, "row") or check_number_in_line(i, get_own_col(x,y, buff_data), x, y, "col"):
                                    # print("x:" + str(x) + " y:" + str(y))
                                    buff_data[math.floor(y/3)][math.floor(x/3)][y%3][x%3] = i
                                    if is_duplicate_in_line(get_own_row(x,y,buff_data)) or is_duplicate_in_line(get_own_col(x,y,buff_data)) or is_duplicate_in_frame(get_own_frame(x,y,buff_data)):
                                        # print_map(buff_data)
                                        print("koko")
                                        return False
                                    # print("【"+str(x)+","+str(y)+"】")
                                    # print_line_of_map( get_own_row(x,y, buff_data))
                                    # print_line_of_map( get_own_col(x,y, buff_data))
                                    # print_map(buff_data, x,y)
                                    isChange = True
        if not isChange:
            if is_no_array_in_frame(buff_data) and is_correct_value_in_frame(buff_data):
                print("Finish!")
                print_map(buff_data)
                raise
                return False
            else:
                # step1 arrayをみつける
                # step2 arrayの中身を入れ替えまたメソッドを呼ぶ
                cx = -1
                cy = -1
                flag = True
                while flag:
                    array = find_array_in_map(buff_data, cx, cy)
                    if array:
                        cx = array["x"]
                        cy = array["y"]
                        for a in array["list"]:
                            tmp_data = copy.deepcopy(buff_data)
                            tmp_data[math.floor(cy/3)][math.floor(cx/3)][cy%3][cx%3] = a
                            if depth < 4:
                                depth_text = ""
                                for i in range(depth):
                                    depth_text += "■"
                                print(depth_text)
                            recursive_resolve_method(copy.deepcopy(tmp_data), depth+1)
                    else:
                        flag = False
                    # print(str(cx) + "," + str(cy))
print("\n\nTry solving the puzzle!")
print_map(data)
recursive_resolve_method(copy.deepcopy(data), 0)
