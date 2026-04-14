---
title: 写的文
---

# 写的文

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400&display=swap" rel="stylesheet">

<style>
.articles-list {
  margin-top: 48px;
  display: flex;
  flex-direction: column;
  gap: 0;
}
.article-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 24px 0;
  border-bottom: 0.5px solid #E0D8CE;
  text-decoration: none;
}
.article-item:first-child { border-top: 0.5px solid #E0D8CE; }
.article-meta {
  display: flex;
  align-items: center;
  gap: 12px;
}
.article-platform {
  font-size: 11px;
  letter-spacing: 0.1em;
  color: #8B4A3C;
  font-family: 'Noto Serif SC', serif;
  font-weight: 300;
}
.article-date {
  font-size: 11px;
  color: #C0B5A8;
  font-weight: 300;
}
.article-title {
  font-size: 16px;
  font-weight: 400;
  color: #2C2C2C;
  font-family: 'Noto Serif SC', serif;
  line-height: 1.5;
  transition: color 0.2s;
}
.article-item:hover .article-title { color: #8B4A3C; }
.article-excerpt {
  font-size: 13px;
  color: #8A8078;
  font-weight: 300;
  line-height: 1.6;
}
</style>

<div class="articles-list">

<!-- 示例文章 — 请替换为真实数据 -->
<a class="article-item" href="https://example.com" target="_blank">
  <div class="article-meta">
    <span class="article-platform">真故研究室</span>
    <span class="article-date">2025-11</span>
  </div>
  <span class="article-title">那些在异国他乡坚持写作的中国人</span>
  <span class="article-excerpt">语言的边界，也是自我的边界。</span>
</a>

</div>

---

> 文章使用以下 frontmatter 格式管理：
>
> ```yaml
> ---
> title: 文章标题
> platform: 真故研究室
> date: 2025-11
> url: https://原文链接
> excerpt: 一句话摘要。
> ---
> ```
