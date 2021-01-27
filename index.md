---
layout: home
nav_exclude: true
seo:
  type: 课程
  name: 动手学深度学习
---

# {{ site.tagline }}
<!-- {: .mb-2 } -->
<!-- {{ site.description }} -->

## 课程摘要

| --- | --- |
| 课时  | 2021年 3月 --- 7月 |
| 直播时间 | 北京时间每周六、日下午 1:30 --- 3:00 |
| 直播地址 | [URL](#) |

## 讲师



{% for staffer in site.staffers %}
{{ staffer }}
{% endfor %}


<div style="clear: both;"></div>


{% if site.announcements %}
{{ site.announcements.last }}
[所有公告](announcements.html){: .btn .fs-3 }
{% endif %}




## 课程安排


{% for module in site.modules %}
{{ module }}
{% endfor %}
