#
# from django.contrib.contenttypes.models import ContentType
# from django.utils import timezone
#
# from .models import ReadNum, ReadDetail
#
#
# # 传入的对象obj
# def read_statistics_once_read(request, obj):
#     ct = ContentType.objects.get_for_model(obj)
#     # 占位符  pk
#     key = "%s_%s_read" % (ct.model, obj.pk)
#     # 判断可以获得key( obj.pk )   最后返回 key
#     if not request.COOKIES.get(key):
#         if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
#             # 存在记录
#             readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
#         else:
#             # 不存在对应的记录
#             readnum = ReadNum(content_type=ct, object_id=obj.pk)
#             # 找不到创建
#         readnum=ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
#         # 计数加1
#         readnum.read_num += 1
#         readnum.save()
#
#         date = timezone.now().date()
#         if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date).count():
#
#             readDetail =ReadDetail.objects.get(content_type=ct, object_id=obj.pk)
#         else:
#             #没有则 实例化一个
#             readDetail=ReadDetail.objects.get(content_type=ct, object_id=obj.pk)
#         readDetail.read_num += 1
#         readDetail.save()
#     return key


import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail


# 传入的对象obj
def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    # 占位符   ct.model  obj.pk
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数 +1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数 +1
        date = timezone.now().date()
        # 返回一个元组   readDetail, created  #找不到创建
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


# 获取前7天阅读点击量
def get_seven_days_read_data(content_type):
    # 获取当天日期
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        # timedelta差值类型 i就是对应i天  差值i=-1
        date = today - datetime.timedelta(days=i)
        # 前端页面需要字符串
        dates.append(date.strftime('%m/%d'))
        # 得到一天的总共 阅读明细（一条 或者多条  通过数据库聚合计算方法 aggregate 给出求和字段类型read_num 可以通过shell模式 查看得到一个字典 ）
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        # 逻辑判断 false取0 反之取前者
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums
