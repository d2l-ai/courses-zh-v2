---
layout: home
title: 课程安排
---

# 动手学深度学习在线课程

## 课程摘要

| --- | --- |
| 课时  | 2021年 3月 --- 7月 |
| 直播时间 | 北京时间每周六、日下午 1:30 --- 3:00 |
| 直播地址 | [<span style="font-size:160%" class="iconfont icon-Streaming"></span>](https://app6ca5octe2206.h5.xiaoeknow.com/v1/course/alive/l_601cc496e4b05a9e88714463) |
| 视频回放 | [<span style="font-size:140%" class="iconfont icon-bilibili-fill"></span>](https://space.bilibili.com/1567748478) [<span style="font-size:140%" class="iconfont icon-youtube"></span>](https://www.youtube.com/playlist?list=PLFXJ6jwg0qW-IGzUIasshuMDMkoWzAAbH) |
| 课程讨论 | [<span class="iconfont icon-discourse"></span>](https://discuss.d2l.ai/c/chinese-version/16) |

## 讲师


{% for staffer in site.staffers %}
{{ staffer }}
{% endfor %}


<div style="clear: both;"></div>


<!-- {% if site.announcements %}
{{ site.announcements.last }}
[所有公告](announcements.html){: .btn .fs-3 }
{% endif %}
 -->


## 课程安排


{% for module in site.modules %}
{{ module }}
{% endfor %}
