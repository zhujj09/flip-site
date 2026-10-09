---
title: ''
summary: ''
date: 2026-10-09
type: landing

sections:
  - block: hero
    content:
      announcement:
        text: "预览版"
      title: "FLIP 课题组"
      text: |-
        **多相流 · 人工举升 · 智慧开采**<br>
        Multiphase Flow · Artificial Lift · Intelligent Production<br>
        中国石油大学（北京）机械工程学院 / 能源装备研究所
      primary_action:
        text: 研究方向
        url: /research/
        icon: hero/arrow-right
      secondary_action:
        text: 加入我们
        url: /join/
    design:
      css_class: "flip-hero"
      css_style: "background-image:url('uploads/hero-placeholder.svg');background-size:cover;background-position:center;"
      spacing:
        padding: ["6rem", 0, "6rem", 0]

  - block: research-areas
    id: research
    content:
      title: 研究方向
      subtitle: ''
      text: ''
      items:
        - name: 多相流
          description: 井筒管流稳态统一模型与瞬态漂移流模型，气井积液判断。
          icon: hero/beaker
          image: research/multiphase.jpg  # 图片在 assets/media/research/，换图直接覆盖同名文件
          gradient: from-blue-500 to-sky-600
          topics: [稳态统一模型, 瞬态漂移流, 积液判断]
          url: research/#wellbore
        - name: 人工举升
          description: 电潜泵气液两相增压模型与诊断；柱塞举升瞬态模型与制度优化；射流泵机理模型与参数优化。
          icon: hero/arrows-up-down
          image: research/lift.jpg  # 图片在 assets/media/research/，换图直接覆盖同名文件
          gradient: from-indigo-500 to-blue-700
          topics: [电潜泵, 柱塞举升, 射流泵]
          url: research/#esp
        - name: 智慧开采
          description: 机理模型与现场数据融合的电潜泵、柱塞井工况智能诊断；管道漏磁内检测数据的缺陷识别与量化。
          icon: hero/cpu-chip
          image: research/smart.jpg  # 图片在 assets/media/research/，换图直接覆盖同名文件
          gradient: from-slate-600 to-slate-800
          topics: [工况智能诊断, 漏磁缺陷识别, 数据样本生成]
          url: research/#mfl
    design:
      layout: cards
      css_class: "flip-areas"

  - block: markdown
    id: pi
    content:
      title: 课题组负责人
      text: |-
        <div class="flip-pi-brief not-prose">
        <img src="{{< u "uploads/people/zhujianjun.jpg" >}}" alt="朱建军" class="flip-pi-brief__photo">
        <div>

        **朱建军**（负责人）副教授、博士生导师，中国石油大学（北京）机械工程学院副院长；课题组与东南大学王建立教授（co-PI）共同指导学生。

        [团队成员 →]({{< u "team/" >}})

        </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    id: news
    content:
      title: 新闻动态
      text: |-
        - **2026-10** 朱建军作「排水采气技术研究进展与成果交流」企业技术交流报告。
        - **2026-09** 朱建军受聘《石油机械》第三届青年编委会委员（聘期 2027–2028）。
        - **2026-09** 朱建军担任第二届高端油气装备技术论坛分论坛主持人。
        - **2026-03** 软件著作权「水平气井瞬态计算软件 V1.0」获登记（2026SR0412776）。
        - **2025-12** 朱建军获 Petroleum Science「荣誉青年编委」。
        - **2025-11** 中国石油迪拜研究院委托项目「智能电潜泵管理系统 V1.0」通过验收。

        [更多新闻 →]({{< u "news/" >}})
    design:
      columns: '1'
---
