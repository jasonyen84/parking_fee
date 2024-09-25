# 應該要有前幾分鐘免費的設定
# 當日最高收費的設定(設定跨日時間)
# 停車場的車輛數量
# 車輛進出紀錄(停車場使用率...)


import datetime


class parking_fee_system:
    def __init__(self):
        self.parking_record = {}  # 車號紀錄
        self.rate = 10  # 每小時10元

    def car_in(self, car_number):
        if car_number in self.parking_record:
            return "錯誤：該車輛已在停車場內"
        self.parking_record[car_number] = {
            "進入時間": datetime.datetime.now(),
            "已付費": False,
        }  # {車號:{進入時間,已付費}}
        return f"車輛 {car_number} 已進入停車場"

    def calculate_fee(self, car_number):  # 計算費用
        if car_number not in self.parking_record:
            return "錯誤：找不到該車輛的停車記錄"
        enter_time = self.parking_record[car_number]["進入時間"]  # 提取進入時間
        parking_time = (
            datetime.datetime.now() - enter_time
        )  # 計算停車時間 = 現在時間 - 進入時間
        parking_hours = parking_time.total_seconds() / 3600  # 轉換成小時
        fee = int(parking_hours * self.rate)  # 計算費用
        return fee

    def pay(self, car_number):  # 繳費
        if car_number not in self.parking_record:
            return "錯誤：找不到該車輛的停車記錄"
        if self.parking_record[car_number]["已付費"]:
            return "錯誤：該車輛已完成繳費"
        fee = self.calculate_fee(car_number)  # 計算費用
        self.parking_record[car_number]["已付費"] = True
        return f"車輛 {car_number} 應繳費用：{fee} 元"

    def car_out(self, car_number):
        if car_number not in self.parking_record:
            return "錯誤：找不到該車輛的停車記錄"
        if not self.parking_record[car_number]["已付費"]:
            return "錯誤：該車輛尚未繳費，無法離開"
        del self.parking_record[car_number]
        return f"車輛 {car_number} 已離開停車場"


# 使用示例
system = parking_fee_system()
print(system.car_in("ABC-1234"))  # 車輛 ABC-1234 已進入停車場
import time

time.sleep(2)  # 模擬停車2秒
print(system.pay("ABC-1234"))  # 車輛 ABC-1234 應繳費用：0 元
print(system.car_out("ABC-1234"))
