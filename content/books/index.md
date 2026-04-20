---
title: 译的书
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;900&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
/* ── Reset Quartz chrome on subpages ── */
body[data-slug="books/index"] .sidebar,
body[data-slug="books/index"] .page-header,
body[data-slug="books/index"] .page-footer,
body[data-slug="books/index"] footer,
body[data-slug="books/index"] hr { display: none !important; }
body[data-slug="books/index"] #quartz-body { display: block !important; padding: 0 !important; margin: 0 !important; gap: 0 !important; }
body[data-slug="books/index"] .center { all: unset !important; display: block !important; width: 100% !important; padding: 0 !important; margin: 0 !important; }
body[data-slug="books/index"] article.popover-hint { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
body[data-slug="books/index"] .breadcrumb-container,
body[data-slug="books/index"] h1.article-title,
body[data-slug="books/index"] .content-meta,
body[data-slug="books/index"] .tags { display: none !important; }
body[data-slug="books/index"] h1 > a,
body[data-slug="books/index"] h2 > a { display: none !important; }
body[data-slug="books/index"] .pg a,
body[data-slug="books/index"] .pg a.internal {
  color: inherit !important; text-decoration: none !important;
  border-bottom: none !important; background-color: transparent !important;
  padding: 0 !important; border-radius: 0 !important;
  transition: none; font-weight: inherit !important;
}

:root {
  --c-bg:     #ffffff;
  --c-text:   #09090b;
  --c-sub:    #52525b;
  --c-muted:  #71717a;
  --c-border: #e4e4e7;
  --c-hover:  #f4f4f5;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── Outer shell ── */
.pg {
  background: var(--c-bg);
  min-height: 100vh;
  color: var(--c-text);
  font-family: 'Noto Serif SC', serif;
  display: flex;
  justify-content: center;
  padding: 0 24px;
}
.pg-inner {
  width: 100%;
  max-width: 900px;
  display: flex;
  gap: 64px;
  padding: 64px 0 96px;
  align-items: flex-start;
}

/* ── Sidebar ── */
.pg-sidebar {
  width: 160px;
  flex-shrink: 0;
  position: sticky;
  top: 48px;
}
.pg-site-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 18px;
  font-weight: 900;
  color: var(--c-text);
  text-decoration: none;
  display: block;
  margin-bottom: 32px;
  letter-spacing: -0.01em;
}
.pg-site-name:hover { opacity: 0.7; }
.pg-nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.pg-nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--c-muted);
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  font-weight: 300;
  transition: background 0.15s, color 0.15s;
  margin: 0 -10px;
}
.pg-nav-item:hover { background: var(--c-hover); color: var(--c-text); }
.pg-nav-item.active { color: var(--c-text); font-weight: 500; }
.pg-nav-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  opacity: 0.5;
}
.pg-nav-item.active .pg-nav-icon { opacity: 1; }

/* ── Main content ── */
.pg-main { flex: 1; min-width: 0; }
.pg-header {
  margin-bottom: 40px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--c-border);
}
.pg-eyebrow {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  color: var(--c-muted);
  font-weight: 300;
  margin: 0 0 10px;
}
.pg-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 24px;
  font-weight: 900;
  color: var(--c-text);
  margin: 0 0 6px;
  letter-spacing: 0.04em;
}
.pg-count {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  color: var(--c-muted);
  font-weight: 300;
  letter-spacing: 0.08em;
}

/* ── Book grid ── */
.bk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 36px 24px;
}
.bk-card {
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  color: inherit;
}
.bk-card:hover .bk-cover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.16); }
.bk-card:hover .bk-name { color: #8B4A3C; }
.bk-cover-wrap {
  position: relative;
  aspect-ratio: 2/3;
  overflow: hidden;
  border-radius: 2px;
  background: var(--c-hover);
}
.bk-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 2px 4px 12px rgba(0,0,0,0.10);
}
.bk-tag {
  position: absolute;
  bottom: 7px;
  left: 7px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  letter-spacing: 0.08em;
  background: rgba(255,255,255,0.88);
  color: #8B4A3C;
  padding: 2px 6px;
  border-radius: 2px;
  backdrop-filter: blur(4px);
}
.bk-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 400;
  color: var(--c-text);
  line-height: 1.5;
  letter-spacing: 0.03em;
  transition: color 0.15s;
}
.bk-year {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px;
  color: var(--c-muted);
  font-weight: 300;
  letter-spacing: 0.1em;
}

/* ── Responsive ── */
@media (max-width: 680px) {
  .pg-inner { flex-direction: column; gap: 32px; }
  .pg-sidebar { width: 100%; position: static; }
  .pg-nav { flex-direction: row; flex-wrap: wrap; }
  .pg-site-name { margin-bottom: 16px; }
  .bk-grid { grid-template-columns: repeat(3, 1fr); gap: 24px 14px; }
}
</style>

<div class="pg">
<div class="pg-inner">

<aside class="pg-sidebar">
  <a class="pg-site-name" href="/">冯诺</a>
  <nav class="pg-nav">
    <a class="pg-nav-item active" href="/books">
      <svg class="pg-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>
      </svg>
      译的书
    </a>
    <a class="pg-nav-item" href="/writing">
      <svg class="pg-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/>
      </svg>
      写的文
    </a>
    <a class="pg-nav-item" href="/projects">
      <svg class="pg-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>
      </svg>
      编的程
    </a>
  </nav>
</aside>

<main class="pg-main">
  <div class="pg-header">
    <p class="pg-eyebrow">WORKS · TRANSLATION</p>
    <h1 class="pg-title">译的书</h1>
    <p class="pg-count">8 部译作</p>
  </div>
  <div class="bk-grid">
    <a class="bk-card" href="https://book.douban.com/subject/37066249/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img2.doubanio.com/view/subject/l/public/s34977060.jpg" alt="错误警报" loading="lazy">
        <span class="bk-tag">社科</span>
      </div>
      <div><div class="bk-name">错误警报</div><div class="bk-year">2024</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/36453354/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34642537.jpg" alt="被互联网辜负的人" loading="lazy">
        <span class="bk-tag">社科</span>
      </div>
      <div><div class="bk-name">被互联网辜负的人</div><div class="bk-year">2023</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/37106144/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34999389.jpg" alt="热点！" loading="lazy">
        <span class="bk-tag">科普</span>
      </div>
      <div><div class="bk-name">热点！</div><div class="bk-year">2024</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/36641005/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34694203.jpg" alt="人物设定创意宝库" loading="lazy">
        <span class="bk-tag">写作</span>
      </div>
      <div><div class="bk-name">人物设定创意宝库</div><div class="bk-year">2023</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/36337285/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34483849.jpg" alt="我所说的话" loading="lazy">
        <span class="bk-tag">小说</span>
      </div>
      <div><div class="bk-name">我所说的话</div><div class="bk-year">2023</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/35067904/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s33873703.jpg" alt="一路微光" loading="lazy">
        <span class="bk-tag">小说</span>
      </div>
      <div><div class="bk-name">一路微光</div><div class="bk-year">2021</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/35018390/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s33610310.jpg" alt="安徒生童话" loading="lazy">
        <span class="bk-tag">童话</span>
      </div>
      <div><div class="bk-name">安徒生童话</div><div class="bk-year">2021</div></div>
    </a>
    <a class="bk-card" href="https://book.douban.com/subject/30323396/" target="_blank">
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img9.doubanio.com/view/subject/l/public/s29866765.jpg" alt="从早「茫」到晚" loading="lazy">
        <span class="bk-tag">绘本</span>
      </div>
      <div><div class="bk-name">从早「茫」到晚</div><div class="bk-year">2018</div></div>
    </a>
  </div>
</main>

</div>
</div>
