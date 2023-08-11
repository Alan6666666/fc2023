# fc2023
对地2023飞控组的

## 关于main.py

目前连接了标靶识别部分，但由于尚未连接数字识别，故标靶识别无返回值，main中循环无法终止，请手动结束程序

## TODO：

### 航点
- [x] 完成四旋翼接线和飞行前配置
- [x] 使用四旋翼测试航点（mp自带）
- [x] 编写航点程序主体
- [x] 在SITL中测试程序
- [x] 完成比赛机电装
- [x] 使用比赛机测试航点程序
- [x] 调参和基础航线测试
- [ ] 编写更多函数功能块
- [ ] 编写和测试靶标坐标解算

### 视觉
- [x] 完成O3与程序的对接
- [ ] 完成数字的识别
- [ ] 完成标靶识别与数字识别的对接

### 实机测试
- [x] 测试两个数传同时运行下的数据稳定性
- [ ] 测试调参后航线飞行效果
- [ ] 整合视觉运行投弹航线
