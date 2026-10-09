---
title: ''
summary: ''
date: 2026-10-09
type: landing

sections:
  - block: hero
    content:
      announcement:
        text: "预览版 · 内容摘自学校个人主页，图片与组员信息待补"
      title: "FLIP 课题组"
      text: |-
        **多相流 · 人工举升 · 智能生产**<br>
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
        - name: 多相流理论建模和数值模拟
          description: 井筒与管线多相流动理论建模、瞬态多相流模型与数值模拟。
          icon: hero/beaker
          gradient: from-blue-500 to-sky-600
          topics: [瞬态多相流模型, 气液两相流型转化, 复杂井筒多相流]
          url: research/#multiphase
        - name: 人工举升装备和工艺
          description: 电潜泵、柱塞、悬梁泵、气举等人工举升装备与工艺，以及采油系统优化设计。
          icon: hero/cog-6-tooth
          gradient: from-indigo-500 to-blue-700
          topics: [电潜泵, 柱塞气举, 悬梁泵, 气举]
          url: research/#artificial-lift
        - name: 深水及非常规采油工程
          description: 深海电潜泵油气混输、气井排水采气与煤岩气采气工艺等。
          icon: hero/globe-asia-australia
          gradient: from-cyan-600 to-teal-700
          topics: [深海油气混输, 气井积液, 煤岩气采气工艺]
          url: research/#deepwater
        - name: 深度学习算法在油气开采领域运用
          description: 油气田生产数据挖掘、工况诊断与异常检测、管道内检测数据智能识别。
          icon: hero/cpu-chip
          gradient: from-slate-600 to-slate-800
          topics: [工况诊断, 异常检测, 漏磁内检测, 智能优化]
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
        <div>{{< placeholder label="待补：负责人照片" h="220" >}}{{< /placeholder >}}</div>
        <div class="md:col-span-3 prose dark:prose-invert max-w-none">

        **朱建军**，博士，副教授；学术型硕导、博士生导师、工程博导；校青年拔尖人才。

        长期从事多相流动理论建模、人工举升采油系统优化设计，以及油气田生产数据挖掘。入选 Elsevier 与斯坦福大学全球前2%科学家榜单（单年度，2025–2026）。

        [查看完整简介 →]({{< u "team/#pi" >}}) &nbsp; [Google Scholar →](https://scholar.google.com/citations?user=sfsM2TUAAAAJ&hl=en)

        </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    id: news
    content:
      title: 新闻动态
      text: |-
        {{< placeholder label="待补：课题组新闻" h="120" >}}学校个人主页上没有新闻条目。请提供近期新闻（标题、日期、简短说明、可选配图），上线后按时间倒序显示。{{< /placeholder >}}
    design:
      columns: '1'
---
