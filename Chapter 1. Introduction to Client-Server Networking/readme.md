# 1. The Building Blocks: Stacks & Libraries
* Các khái niệm cần ghi nhớ:
  * **Protocol stack** _[ngăn xếp giao thức]_, trong đó **simpler network services** _[các dịch vụ mạng đơn giản]_ dc sử dụng làm nền tảng của các dịch vụ phức tạp hơn.

###### [search1.py](./search1.py)
* Cung cấp địa chỉ vào biến `address` sẽ cho biết vĩ độ - kinh độ của vị trí này.
![](../images/chap_01_0.png)

# 2. Application Layers
* Sử dụng package `requests` của Python để gọi API cung cấp tọa độ từ một vị trí `address`.
##### [search2.py](./search2.py)
![](../images/chap_01_1.png)
