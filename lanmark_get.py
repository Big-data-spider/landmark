import re
import json


def landmark_get():
    content = open('./work_file/422_ChinaCity.kml', 'r', encoding='utf-8')
    T_con = content.read()
    print(type(T_con))

    pattren = r'<name>(\w+|\w+：\w+)</name>'
    res = re.findall(pattren, T_con)
    print(res)

    jstr = json.dumps(res, ensure_ascii=False, indent=4)
    fs = open('./res/res_001.json', 'w', encoding='utf-8')
    fs.write(jstr)
    fs.close()


landmark_get()
