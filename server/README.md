# 弹幕阅读器（服务器）

### 这是啥
用来加载弹幕，读取弹幕，与chrome插件联动的服务器。负责出声

### 路径
- load?url=xxx: 监听加载事件，参数为视频url
- read?time=xxx 监听阅读事件，参数为当前播放进度（秒）
- stop 监听暂停事件

### 使用
1. 启用google cloud tts服务([启用文档](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries))。
2. 使用venv环境
3. 使用`pip install -r requirements.txt`安装依赖
4. 使用`python entry.py`开启服务器