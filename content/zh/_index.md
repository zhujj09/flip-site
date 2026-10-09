---
title: ''
summary: ''
date: 2026-10-09
type: landing

sections:
  - block: hero
    content:
      announcement:
        text: "预览版 · 在读组员名单待补"
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
          description: 井筒多相流统一模型与漂移流瞬态模型，气井积液预测与模型优选。
          icon: hero/beaker
          gradient: from-blue-500 to-sky-600
          topics: [统一井筒模型, 漂移流瞬态, 积液预测]
          url: research/#multiphase
        - name: 人工举升
          description: 电潜泵气液两相举升机理与增压模型；柱塞气举、射流泵与气举的机理建模和设计计算。
          icon: hero/arrows-up-down
          gradient: from-indigo-500 to-blue-700
          topics: [电潜泵, 柱塞气举, 射流泵与气举]
          url: research/#esp
        - name: 智慧开采
          description: 机理模型与现场数据融合的工况诊断、寿命预测与制度优化；物理信息神经网络快速瞬态计算。
          icon: hero/cpu-chip
          gradient: from-slate-600 to-slate-800
          topics: [智能诊断, 制度优化, PI-DeepONet / XPINN]
          url: research/#ai
    design:
      layout: cards
      css_class: "flip-areas"

  - block: markdown
    id: pi
    content:
      title: 课题组负责人
      text: |-
        <div class="grid md:grid-cols-4 gap-6 items-start not-prose">
        <div><img src="{{< u "uploads/people/zhujianjun.jpg" >}}" alt="朱建军" class="flip-pi-photo"></div>
        <div class="md:col-span-3 prose dark:prose-invert max-w-none">

        **朱建军**，博士，副教授，机械工程学院副院长；学术型硕导、博士生导师、工程博导；校青年拔尖人才。

        长期从事多相流动理论建模、人工举升采油系统优化设计，以及油气田生产数据挖掘。2012–2017 年在美国塔尔萨大学获石油工程博士学位，2017–2019 年任塔尔萨大学人工举升项目组（TUALP）助理研究员，2019 年起任教于中国石油大学（北京）。入选 Elsevier 与斯坦福大学全球前2%科学家榜单（单年度，2025–2026）。

        课题组与东南大学机械工程学院王建立教授（共同负责人，co-PI）共同指导学生。

        [团队与负责人 →]({{< u "team/" >}}) &nbsp; [Google Scholar →](https://scholar.google.com/citations?user=sfsM2TUAAAAJ&hl=en)

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
