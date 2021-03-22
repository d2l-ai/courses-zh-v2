---
layout: page
title: 课程公告
nav_exclude: true
description: A feed containing all of the class announcements.
---

# 课程公告

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
