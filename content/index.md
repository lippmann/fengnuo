---
title: 冯诺
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200;300;400;900&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
/* ── Quartz chrome 隐藏 ── */
body[data-slug="index"] .sidebar,
body[data-slug="index"] .page-header,
body[data-slug="index"] .page-footer,
body[data-slug="index"] footer,
body[data-slug="index"] hr { display: none !important; }
body[data-slug="index"] #quartz-root,
body[data-slug="index"] #quartz-root > .page { display: block !important; padding: 0 !important; margin: 0 !important; }
body[data-slug="index"] .center { all: unset; display: block; width: 100%; }
body[data-slug="index"] article.popover-hint { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }

:root {
  --ink: #1A1814;
  --ink-mid: #6B6560;
  --ink-faint: #B8B0A8;
  --paper: #F5F0E8;
  --rule: #D8D0C6;
  --accent: #8B4A3C;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.fn-wrap {
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  font-family: 'IBM Plex Mono', monospace;
  color: var(--ink);
  padding: 0 32px;
}

.fn-page {
  width: 100%;
  max-width: 860px;
  padding: 52px 0 48px;
  display: flex;
  flex-direction: column;
}

/* ── Two-column layout ── */
.fn-main {
  display: grid;
  grid-template-columns: 210px 1fr;
  align-items: start;
}

/* ── Left: hand-drawn speech balloon ── */
.fn-left {
  display: flex;
  flex-direction: column;
  padding-right: 24px;
}

/* SVG hand-drawn border — rendered as background */
.fn-balloon {
  position: relative;
  border: 1.5px solid var(--ink);
  border-radius: 16px 4px 14px 5px / 5px 14px 4px 16px;
  padding: 32px 36px 36px;
  background: var(--paper);
  overflow: visible;
  height: 100%;
  min-height: 480px;
  display: flex;
  flex-direction: column;
}

/* Decorative quote mark */
.fn-balloon::before {
  content: '\300C';
  position: absolute;
  bottom: 20px;
  right: 24px;
  font-family: 'Noto Serif SC', serif;
  font-size: 96px;
  font-weight: 900;
  color: var(--ink);
  opacity: 0.04;
  line-height: 1;
  pointer-events: none;
  z-index: 0;
}

/* Hand-drawn tail using SVG polygon — positioned absolutely */
.fn-tail-svg {
  position: absolute;
  left: -1px;
  top: 40px;
  width: 44px;
  height: 28px;
  overflow: visible;
  pointer-events: none;
  z-index: 4;
}

.fn-says-label {
  font-size: 9px;
  letter-spacing: 0.22em;
  color: var(--ink-faint);
  font-weight: 300;
  margin-bottom: 24px;
  text-transform: lowercase;
  position: relative;
  z-index: 1;
}
.fn-says-label em { font-style: normal; color: var(--accent); }

.fn-feed {
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 1;
}

.fn-entry {
  padding: 18px 0;
  border-bottom: 1px solid var(--rule);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.fn-entry:first-child { padding-top: 0; }
.fn-entry:last-child { border-bottom: none; padding-bottom: 0; }

.fn-entry-text {
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  font-weight: 300;
  line-height: 2;
  color: var(--ink);
  letter-spacing: 0.04em;
}

.fn-entry-date {
  font-size: 9px;
  color: var(--ink-faint);
  letter-spacing: 0.16em;
  font-weight: 300;
  text-align: right;
}

/* ── Right column: balloon ── */
.fn-right {
  position: relative;
  padding-left: 40px;
}

.fn-portrait {
  width: 100%;
  aspect-ratio: 3/4;
  overflow: hidden;
  position: relative;
  margin-bottom: 12px;
}

.fn-portrait img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 8%;
  mix-blend-mode: multiply;
  display: block;
}

/* Name below portrait */
.fn-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 28px;
  font-weight: 900;
  letter-spacing: 0.14em;
  color: var(--ink);
  margin-bottom: 10px;
  line-height: 1;
}

.fn-cursor {
  display: inline-block;
  width: 2px;
  height: 12px;
  background: var(--accent);
  margin-left: 2px;
  vertical-align: middle;
  animation: blink 1.2s step-end infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

.fn-intro {
  font-family: 'Noto Serif SC', serif;
  font-size: 11px;
  font-weight: 300;
  line-height: 1.9;
  color: var(--ink-faint);
  letter-spacing: 0.04em;
  margin-bottom: 22px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--rule);
}

/* ── Nav links: clean, simple ── */
.fn-nav-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.fn-nav-section { display: flex; flex-direction: column; gap: 2px; }

.fn-nav-heading {
  font-size: 9px;
  letter-spacing: 0.2em;
  color: var(--ink-faint);
  font-weight: 300;
  text-transform: lowercase;
  margin-bottom: 6px;
}
.fn-nav-heading em { font-style: normal; color: var(--accent); }

.fn-nav-link {
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 400;
  color: var(--ink-mid);
  text-decoration: none;
  letter-spacing: 0.04em;
  line-height: 2.2;
  transition: color 0.15s;
  display: block;
}
.fn-nav-link:hover { color: var(--accent); }

/* ── Footer ── */
.fn-footer {
  margin-top: 40px;
  padding-top: 14px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.fn-social {
  font-size: 10px;
  font-weight: 300;
  letter-spacing: 0.14em;
  color: var(--ink-mid);
  text-decoration: none;
  text-transform: lowercase;
  transition: color 0.2s;
}
.fn-social:hover { color: var(--accent); }

.fn-social-sep { font-size: 10px; color: var(--rule); }

.fn-copy {
  margin-left: auto;
  font-size: 9px;
  color: var(--ink-faint);
  letter-spacing: 0.14em;
  font-weight: 300;
}

/* ── Responsive ── */
@media (max-width: 640px) {
  .fn-wrap { padding: 0 20px; }
  .fn-page { padding: 36px 0 40px; }
  .fn-main { grid-template-columns: 1fr; }
  .fn-left { padding-right: 0; margin-bottom: 36px; }
  .fn-balloon { min-height: auto; }
  .fn-tail-svg { display: none; }
  .fn-right { padding-left: 0; }
}
</style>

<div class="fn-wrap">
<div class="fn-page">
<div class="fn-main">
<div class="fn-left">
<div class="fn-portrait">
<img src="/avatar.png" alt="冯诺">
</div>
<p class="fn-name">冯诺<span class="fn-cursor"></span></p>
<p class="fn-intro">作者 · 译者 · 偶尔写代码</p>
<nav class="fn-nav-block">
<div class="fn-nav-section">
<span class="fn-nav-heading"><em>~/</em>作品</span>
<a class="fn-nav-link" href="/books">译的书</a>
<a class="fn-nav-link" href="/writing">写的文</a>
<a class="fn-nav-link" href="/projects">编的程</a>
</div>
<div class="fn-nav-section">
<span class="fn-nav-heading"><em>~/</em>兴趣</span>
<a class="fn-nav-link" href="/reading">读的书</a>
<a class="fn-nav-link" href="/movies">观的影</a>
<a class="fn-nav-link" href="/music">听的乐</a>
</div>
</nav>
</div>
<div class="fn-right">
<div class="fn-balloon">
<p class="fn-says-label"><em>~/says</em> &nbsp;·&nbsp; 碎的念</p>
<div class="fn-feed">
<div class="fn-entry">
<p class="fn-entry-text">翻译是一种慢下来的阅读。每一个词都要停留，直到它在另一种语言里找到自己的位置。</p>
<span class="fn-entry-date">2026 · 04 · 12</span>
</div>
<div class="fn-entry">
<p class="fn-entry-text">语言是住所，不是工具。你居住在语言里，而不是使用它。</p>
<span class="fn-entry-date">2026 · 03 · 28</span>
</div>
<div class="fn-entry">
<p class="fn-entry-text">最好的译文让人忘记它是译文。最好的写作让人忘记它是写作。</p>
<span class="fn-entry-date">2026 · 03 · 10</span>
</div>
</div>
</div>
<!-- Hand-drawn tail pointing left toward portrait -->
<svg class="fn-tail-svg" viewBox="0 0 44 28" xmlns="http://www.w3.org/2000/svg">
<path d="M43,8 C41,6 42,9 44,14 C38,12 26,10 0,14 C16,16 36,18 42,20 C43,18 45,16 43,8 Z" fill="#F5F0E8" stroke="#1A1814" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
</div>
</div>
<footer class="fn-footer">
<a class="fn-social" href="https://www.douban.com/people/YOUR_DOUBAN_ID" target="_blank">豆瓣</a>
<span class="fn-social-sep">×</span>
<a class="fn-social" href="https://x.com/YOUR_X_HANDLE" target="_blank">x.com</a>
<span class="fn-social-sep">×</span>
<a class="fn-social" href="https://github.com/YOUR_GITHUB_USERNAME" target="_blank">github</a>
<span class="fn-social-sep">×</span>
<a class="fn-social" href="mailto:YOUR_EMAIL_ADDRESS">mail</a>
<span class="fn-copy">© 2026 冯诺</span>
</footer>
</div>
</div>
