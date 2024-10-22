import json
import csv
#从文件输入json数据
with open('data.json', 'r') as f:
    input = f.read()
# 读取json数据
data = json.loads(input)
# 读取json数据中的data
data = data['PageList']['Items']
# 写入CSV文件的表头
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['活动名称', '活动状态', '签到状态', '时间', '活动ID'])

# 循环读取data中的每一条数据,并输出到CSV文件中
for item in data:
    if item is None:
        continue
    name = item['ActivityName']
    activityId = item['ActivityId']
    Examstatus = item['ExamStatus']
    SignD = item['SignD']
    time = item['ActivityTime']
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, Examstatus, SignD, time, activityId])

