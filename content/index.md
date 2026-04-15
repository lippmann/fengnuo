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

/* ── Outer wrap ── */
.fn-wrap {
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  font-family: 'IBM Plex Mono', monospace;
  color: var(--ink);
  padding: 0 32px;
}
.fn-page {
  width: 100%;
  max-width: 900px;
  padding: 48px 0 52px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* ── Header ── */
.fn-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 40px;
}
.fn-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 26px;
  font-weight: 900;
  letter-spacing: 0.12em;
  color: var(--ink);
  text-decoration: none;
}
.fn-title:hover { color: var(--accent); }
.fn-socials {
  display: flex;
  align-items: center;
  gap: 22px;
}
.fn-social {
  font-size: 10px;
  font-weight: 300;
  letter-spacing: 0.14em;
  color: var(--ink-mid);
  text-decoration: none;
  text-transform: lowercase;
  transition: color 0.18s;
  position: relative;
}
.fn-social::after {
  content: '';
  position: absolute;
  bottom: -2px; left: 0;
  width: 0; height: 1px;
  background: var(--accent);
  transition: width 0.18s;
}
.fn-social:hover { color: var(--accent); }
.fn-social:hover::after { width: 100%; }

/* ── Middle: balloon + portrait ── */
.fn-middle {
  display: grid;
  grid-template-columns: 1fr 170px;
  align-items: start;
  margin-bottom: 40px;
}

/* Speech balloon */
.fn-balloon-wrap {
  position: relative;
  padding-right: 36px;
}
.fn-balloon {
  position: relative;
  border: 1.5px solid var(--ink);
  border-radius: 14px 5px 12px 4px / 4px 12px 5px 14px;
  padding: 28px 32px 28px;
  background: var(--paper);
  overflow: visible;
}
/* Decorative quote */
.fn-balloon::before {
  content: '\300C';
  position: absolute;
  bottom: 12px; right: 18px;
  font-family: 'Noto Serif SC', serif;
  font-size: 80px;
  font-weight: 900;
  color: var(--ink);
  opacity: 0.04;
  line-height: 1;
  pointer-events: none;
}
/* Tail pointing right toward portrait */
.fn-tail-svg {
  position: absolute;
  right: -1px;
  top: 44px;
  width: 40px;
  height: 26px;
  overflow: visible;
  pointer-events: none;
  z-index: 4;
}
.fn-says-label {
  font-size: 9px;
  letter-spacing: 0.22em;
  color: var(--ink-faint);
  font-weight: 300;
  margin-bottom: 20px;
  text-transform: lowercase;
}
.fn-says-label em { font-style: normal; color: var(--accent); }
.fn-feed { display: flex; flex-direction: column; }
.fn-entry {
  padding: 16px 0;
  border-bottom: 1px solid var(--rule);
  display: flex;
  flex-direction: column;
  gap: 8px;
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

/* Portrait */
.fn-portrait-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding-left: 8px;
}
.fn-portrait {
  width: 148px;
  height: 185px;
  overflow: hidden;
}
.fn-portrait img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 8%;
  mix-blend-mode: multiply;
  display: block;
}
.fn-portrait-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 15px;
  font-weight: 900;
  letter-spacing: 0.14em;
  color: var(--ink);
  text-align: center;
}
.fn-cursor {
  display: inline-block;
  width: 2px; height: 12px;
  background: var(--accent);
  margin-left: 2px;
  vertical-align: middle;
  animation: blink 1.2s step-end infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
.fn-portrait-role {
  font-size: 9px;
  color: var(--ink-faint);
  letter-spacing: 0.12em;
  font-weight: 300;
  text-align: center;
  line-height: 2;
}

/* ── Bottom nav ── */
.fn-nav {
  border-top: 1px solid var(--rule);
  display: flex;
  align-items: stretch;
}
.fn-nav-section {
  display: flex;
  align-items: stretch;
  flex: 1;
}
.fn-nav-section + .fn-nav-section {
  border-left: 1px solid var(--rule);
}
.fn-nav-label {
  font-size: 9px;
  letter-spacing: 0.18em;
  color: var(--ink-faint);
  font-weight: 300;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  padding: 16px 10px 16px 8px;
  border-right: 1px solid var(--rule);
  display: flex;
  align-items: center;
  justify-content: center;
}
.fn-nav-links {
  display: flex;
  flex: 1;
}
.fn-nav-link {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px 8px;
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 400;
  color: var(--ink-mid);
  text-decoration: none;
  letter-spacing: 0.06em;
  border-right: 1px solid var(--rule);
  transition: color 0.15s, background 0.15s;
}
.fn-nav-link:last-child { border-right: none; }
.fn-nav-link:hover {
  color: var(--accent);
  background: rgba(139,74,60,0.04);
}

/* ── Footer ── */
.fn-footer {
  margin-top: 28px;
  display: flex;
  justify-content: flex-end;
}
.fn-copy {
  font-size: 9px;
  color: var(--ink-faint);
  letter-spacing: 0.14em;
  font-weight: 300;
}

/* ── Responsive ── */
@media (max-width: 640px) {
  .fn-wrap { padding: 0 20px; }
  .fn-page { padding: 32px 0 40px; }
  .fn-middle { grid-template-columns: 1fr; gap: 32px; }
  .fn-balloon-wrap { padding-right: 0; }
  .fn-tail-svg { display: none; }
  .fn-portrait-col { flex-direction: row; gap: 16px; align-items: center; }
  .fn-portrait { width: 80px; height: 100px; }
  .fn-nav { flex-direction: column; }
  .fn-nav-section + .fn-nav-section { border-left: none; border-top: 1px solid var(--rule); }
  .fn-nav-label { writing-mode: horizontal-tb; padding: 10px 12px; border-right: none; border-bottom: 1px solid var(--rule); }
}
</style>

<div class="fn-wrap">
<div class="fn-page">
<header class="fn-header">
<a class="fn-title" href="/">冯诺</a>
<nav class="fn-socials">
<a class="fn-social" href="https://www.douban.com/people/L.Revolution/" target="_blank">豆瓣</a>
<a class="fn-social" href="https://github.com/YOUR_GITHUB_USERNAME" target="_blank">github</a>
<a class="fn-social" href="https://x.com/YOUR_X_HANDLE" target="_blank">x.com</a>
<a class="fn-social" href="mailto:YOUR_EMAIL_ADDRESS">mail</a>
</nav>
</header>
<div class="fn-middle">
<div class="fn-balloon-wrap">
<div class="fn-balloon">
<p class="fn-says-label"><em>~/says</em> &nbsp;·&nbsp; 碎的念</p>
<div class="fn-feed">
<div class="fn-entry">
<p class="fn-entry-text">Claude Code 简直是人民的大救星，自从用上了它，我已经 vibe coding 了两个 Chrome 插件并提交商店审核。目前正在开发一个手机应用，另外还做了两份新产品的 PRD，等手头上的弄完就推进。谁能想到，在30多岁的高龄，竟然成了一个半路出家的码农。</p>
<span class="fn-entry-date">2026 · 04 · 10</span>
</div>
<div class="fn-entry">
<p class="fn-entry-text">这辈子在语言学习上花的最大的一笔钱，是去年趁半价打折花了 399 美元买了 Pimsleur 终身套餐，可以学习里面的所有 50 多门语言。今天发现已经连续 250 天每天至少学 10 分钟以上，学完了从 Level 1 到 Level 5 的西班牙语。</p>
<span class="fn-entry-date">2026 · 04 · 04</span>
</div>
<div class="fn-entry">
<p class="fn-entry-text">之前就有人讨论为什么 AI 的 logo 都很像 asshole。别的不说，Claude 就特别像我的偶像冯内古特（也是本豆瓣 ID 的灵感来源）小说里出现过的插图，表示的正是 asshole。</p>
<span class="fn-entry-date">2026 · 04 · 01</span>
</div>
</div>
</div>
<svg class="fn-tail-svg" viewBox="0 0 40 26" xmlns="http://www.w3.org/2000/svg">
<path d="M1,7 C3,5 2,8 0,13 C5,11 16,9 40,13 C26,15 7,17 2,19 C1,17 -1,15 1,7 Z" fill="#F5F0E8" stroke="#1A1814" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
</div>
<div class="fn-portrait-col">
<div class="fn-portrait">
<img src="/avatar.png" alt="冯诺">
</div>
<p class="fn-portrait-role">作者<br>译者<br>偶尔写代码</p>
<p class="fn-portrait-name">冯诺<span class="fn-cursor"></span></p>
</div>
</div>
<nav class="fn-nav">
<div class="fn-nav-section">
<span class="fn-nav-label">作品</span>
<div class="fn-nav-links">
<a class="fn-nav-link" href="/books">译的书</a>
<a class="fn-nav-link" href="/writing">写的文</a>
<a class="fn-nav-link" href="/projects">编的程</a>
</div>
</div>
<div class="fn-nav-section">
<span class="fn-nav-label">兴趣</span>
<div class="fn-nav-links">
<a class="fn-nav-link" href="/reading">读的书</a>
<a class="fn-nav-link" href="/movies">观的影</a>
<a class="fn-nav-link" href="/music">听的乐</a>
</div>
</div>
</nav>
<footer class="fn-footer">
<span class="fn-copy">© 2026 冯诺</span>
</footer>
</div>
</div>
