---
title: 译的书
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;900&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
.bk-wrap {
  font-family: 'IBM Plex Mono', monospace;
  color: #2C2C2C;
  padding: 0 0 80px;
}
.bk-header {
  margin-bottom: 48px;
  padding-bottom: 24px;
  border-bottom: 1px solid #E0D8CE;
}
.bk-eyebrow {
  font-size: 10px;
  letter-spacing: 0.2em;
  color: #C0B8AE;
  font-weight: 300;
  margin: 0 0 12px;
}
.bk-eyebrow span { color: #8B4A3C; }
.bk-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 28px;
  font-weight: 900;
  color: #1E1A17;
  margin: 0 0 8px;
  letter-spacing: 0.06em;
}
.bk-count {
  font-size: 11px;
  color: #B0A496;
  font-weight: 300;
  letter-spacing: 0.08em;
  margin: 0;
}
.bk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(148px, 1fr));
  gap: 40px 28px;
}
.bk-card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}
.bk-card:hover .bk-cover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.16); }
.bk-card:hover .bk-name { color: #8B4A3C; }
.bk-cover-wrap {
  position: relative;
  aspect-ratio: 2/3;
  overflow: hidden;
  border-radius: 2px;
  background: #EAE4DC;
}
.bk-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 2px 4px 16px rgba(0,0,0,0.12);
}
.bk-tag {
  position: absolute;
  bottom: 8px;
  left: 8px;
  font-size: 9px;
  letter-spacing: 0.1em;
  background: rgba(245,240,232,0.92);
  color: #8B4A3C;
  padding: 3px 7px;
  border-radius: 2px;
  font-weight: 400;
  backdrop-filter: blur(4px);
}
.bk-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.bk-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 400;
  color: #2C2C2C;
  line-height: 1.5;
  letter-spacing: 0.03em;
  transition: color 0.15s;
}
.bk-year {
  font-size: 10px;
  color: #C0B8AE;
  font-weight: 300;
  letter-spacing: 0.1em;
}
@media (max-width: 480px) {
  .bk-grid { grid-template-columns: repeat(3, 1fr); gap: 24px 16px; }
  .bk-name { font-size: 12px; }
}
</style>

<div class="bk-wrap">
<div class="bk-header">
<p class="bk-eyebrow"><span>~/</span>books</p>
<h1 class="bk-title">译的书</h1>
<p class="bk-count">8 部译作</p>
</div>
<div class="bk-grid">
<a class="bk-card" href="https://book.douban.com/subject/37066249/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img2.doubanio.com/view/subject/l/public/s34977060.jpg" alt="错误警报" loading="lazy">
<span class="bk-tag">社科</span>
</div>
<div class="bk-info">
<span class="bk-name">错误警报</span>
<span class="bk-year">2024</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/36453354/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34642537.jpg" alt="被互联网辜负的人" loading="lazy">
<span class="bk-tag">社科</span>
</div>
<div class="bk-info">
<span class="bk-name">被互联网辜负的人</span>
<span class="bk-year">2023</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/37106144/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34999389.jpg" alt="热点！" loading="lazy">
<span class="bk-tag">科普</span>
</div>
<div class="bk-info">
<span class="bk-name">热点！</span>
<span class="bk-year">2024</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/36641005/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34694203.jpg" alt="人物设定创意宝库" loading="lazy">
<span class="bk-tag">写作</span>
</div>
<div class="bk-info">
<span class="bk-name">人物设定创意宝库</span>
<span class="bk-year">2023</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/36337285/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34483849.jpg" alt="我所说的话" loading="lazy">
<span class="bk-tag">小说</span>
</div>
<div class="bk-info">
<span class="bk-name">我所说的话</span>
<span class="bk-year">2023</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/35067904/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s33873703.jpg" alt="一路微光" loading="lazy">
<span class="bk-tag">小说</span>
</div>
<div class="bk-info">
<span class="bk-name">一路微光</span>
<span class="bk-year">2021</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/35018390/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s33610310.jpg" alt="安徒生童话" loading="lazy">
<span class="bk-tag">童话</span>
</div>
<div class="bk-info">
<span class="bk-name">安徒生童话</span>
<span class="bk-year">2021</span>
</div>
</a>
<a class="bk-card" href="https://book.douban.com/subject/30323396/" target="_blank">
<div class="bk-cover-wrap">
<img class="bk-cover" src="https://img9.doubanio.com/view/subject/l/public/s29866765.jpg" alt="从早「茫」到晚" loading="lazy">
<span class="bk-tag">绘本</span>
</div>
<div class="bk-info">
<span class="bk-name">从早「茫」到晚</span>
<span class="bk-year">2018</span>
</div>
</a>
</div>
</div>
