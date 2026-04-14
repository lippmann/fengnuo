---
title: 编的程
---

# 编的程

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400&display=swap" rel="stylesheet">

<style>
.timeline {
  margin-top: 48px;
  position: relative;
  padding-left: 80px;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 52px;
  top: 0;
  bottom: 0;
  width: 0.5px;
  background: #E0D8CE;
}
.timeline-item {
  position: relative;
  margin-bottom: 40px;
}
.timeline-dot {
  position: absolute;
  left: -32px;
  top: 6px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #C0B5A8;
  margin-left: -2.5px;
}
.timeline-year {
  position: absolute;
  left: -80px;
  top: 2px;
  font-size: 12px;
  color: #B0A496;
  font-weight: 300;
  letter-spacing: 0.1em;
  font-family: 'Noto Serif SC', serif;
}
.project-name {
  font-size: 16px;
  font-weight: 400;
  color: #2C2C2C;
  font-family: 'Noto Serif SC', serif;
  margin-bottom: 6px;
}
.project-desc {
  font-size: 13px;
  color: #6A6258;
  font-weight: 300;
  line-height: 1.7;
  margin-bottom: 8px;
}
.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.tag {
  font-size: 10px;
  padding: 2px 8px;
  border: 0.5px solid #D8D0C4;
  border-radius: 2px;
  color: #8A8078;
  font-weight: 300;
  letter-spacing: 0.05em;
}
.tag-type {
  border-color: #C4956A;
  color: #C4956A;
}
.project-github {
  font-size: 11px;
  color: #B0A496;
  text-decoration: none;
  margin-top: 6px;
  display: inline-block;
}
.project-github:hover { color: #8B4A3C; }
@media (max-width: 480px) {
  .timeline { padding-left: 60px; }
  .timeline::before { left: 40px; }
  .timeline-year { left: -60px; font-size: 11px; }
}
</style>

<div class="timeline">

<!-- 示例项目 — 请替换为真实数据 -->
<div class="timeline-item">
  <span class="timeline-year">2025</span>
  <div class="timeline-dot"></div>
  <div class="project-name">译稿管理 Plugin</div>
  <p class="project-desc">原文/译文双栏对照、术语表与进度追踪。</p>
  <div class="project-tags">
    <span class="tag tag-type">Obsidian Plugin</span>
    <span class="tag">TypeScript</span>
    <span class="tag">Obsidian API</span>
  </div>
  <a class="project-github" href="https://github.com/YOUR_GITHUB_USERNAME" target="_blank">→ GitHub</a>
</div>

</div>

---

> 项目使用以下 frontmatter 格式管理：
>
> ```yaml
> ---
> title: 译稿管理 Plugin
> year: 2025
> type: Obsidian Plugin
> tags: [TypeScript, Obsidian API]
> github: https://github.com/xxx
> description: 原文/译文双栏对照、术语表与进度追踪。
> ---
> ```
