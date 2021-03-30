---
layout: home
title: 课程安排
---

# 动手学深度学习在线课程

<!-- <div class="responsive-video-container">

<iframe src="//player.bilibili.com/player.html?aid=289532467&bvid=BV1if4y147hS&cid=309491732&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

</div>  -->

## 课程摘要

| --- | --- |
| 课时  | 2021年3月20日 --- （预计）7月 |
| 直播时间 | 北京时间每周六、日下午 1:00 --- 2:30 |
| 直播地址 | [<span style="font-size:140%" class="iconfont icon-livestreaming"></span> 机器之心](https://app6ca5octe2206.h5.xiaoeknow.com/v1/course/alive/l_601cc496e4b05a9e88714463) |
| 视频回放 | [<span style="font-size:140%" class="iconfont icon-bilibili-fill"></span> B站](https://space.bilibili.com/1567748478) |
| 教材 | [<span class="iconfont icon-xiaoshuo-copy"></span> zh-v2.d2l.ai](https://zh-v2.d2l.ai/) |



不论是在学术突破还是在工业应用，
深度学习是人工智能在近十年里进展最为迅速的领域。然而，深度学习模型复杂、参数繁多、而且新模型层出不穷，这给学习带来了难度。

本课程将从零开始教授深度学习。同学们只需要有基础的Python编程和数学基础。我们将覆盖四大类模型：多层感知机、卷积神经网络、循环神经网络、和注意力机制。在此之上，我们将介绍深度学习中的两大应用领域---计算机视觉和自然语言处理---中的典型任务。

本课程的一大特点是不仅讲述模型算法，同时会将每一处细节都讲述如何用PyTorch进行实现。这样同学们可以在真实数据上获得第一手经验。我们将举办四次课程竞赛，让同学们实践学习到的知识如何解决实际问题。

课程内容将紧靠《动手学深度学习》第二版。本书目前已经被近200所大学采用作为教材。我们将在3月20日开始直播。同学们无需注册或缴费就可以参加。敬请期待。




## 讲师

{% for staffer in site.staffers %}
{{ staffer }}
{% endfor %}

<div style="clear: both;"></div>


## 课程公告

{% if site.announcements %}
{{ site.announcements.last }}
[所有公告](announcements.html){: .btn .fs-3 }
{% endif %}


## 课程安排


目前日程安排为暂定安排，会根据实际进度进行调整。部分内容暂时链接到英文版，中文版会随后更新。


{% for module in site.modules %}
{{ module }}
{% endfor %}
