---
title: 冯诺
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;900&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
/* ── Reset Quartz chrome ── */
body[data-slug="index"] .sidebar,
body[data-slug="index"] .page-header,
body[data-slug="index"] .page-footer,
body[data-slug="index"] footer,
body[data-slug="index"] hr { display: none !important; }
body[data-slug="index"] #quartz-root,
body[data-slug="index"] #quartz-root > .page { display: block !important; padding: 0 !important; margin: 0 !important; }
body[data-slug="index"] .center { all: unset !important; display: block !important; width: 100% !important; }
body[data-slug="index"] article.popover-hint { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
body[data-slug="index"] .page-header { display: none !important; }

/* ── Tokens ── */
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
.hp {
  background: var(--c-bg);
  min-height: 100vh;
  color: var(--c-text);
  font-family: 'Noto Serif SC', serif;
  display: flex;
  justify-content: center;
  padding: 0 24px;
}
.hp-inner {
  width: 100%;
  max-width: 640px;
  padding: 64px 0 96px;
}

/* ── Header ── */
.hp-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 64px;
}
.hp-name {
  font-family: 'Noto Serif SC', serif;
  font-size: 28px;
  font-weight: 900;
  letter-spacing: -0.01em;
  line-height: 1.2;
  color: var(--c-text);
  margin-bottom: 12px;
}
.hp-bio {
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  font-weight: 300;
  color: var(--c-sub);
  line-height: 1.7;
  max-width: 360px;
  margin-bottom: 16px;
}
.hp-nav {
  display: flex;
  align-items: center;
  gap: 0;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 13px;
  font-weight: 400;
}
.hp-nav a {
  color: var(--c-text);
  text-decoration: none;
}
.hp-nav a:hover { text-decoration: underline; text-underline-offset: 3px; }
.hp-nav-sep {
  color: var(--c-muted);
  margin: 0 8px;
  user-select: none;
}
.hp-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  margin-top: 2px;
}
.hp-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 8%;
}

/* ── Section ── */
.hp-section { margin-bottom: 48px; }
.hp-section-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--c-muted);
  margin-bottom: 16px;
}

/* ── Experience list ── */
.exp-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* Each row */
.exp-item {
  display: flex;
  flex-direction: column;
  cursor: pointer;
  border-radius: 12px;
  padding: 6px 8px;
  margin: 0 -8px;
  transition: background 0.15s;
  text-decoration: none;
  color: inherit;
}
.exp-item:hover { background: var(--c-hover) !important; }

.exp-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

/* Icon container */
.exp-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  flex-shrink: 0;
}
.exp-icon-wrap svg,
.exp-icon-wrap img {
  width: 20px;
  height: 20px;
  opacity: 0.75;
}

/* Text */
.exp-body { flex: 1; min-width: 0; }
.exp-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 15px;
  font-weight: 500;
  color: var(--c-text);
  line-height: 1.4;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.exp-sub {
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 300;
  color: var(--c-sub);
  margin-top: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.exp-sub-dot {
  color: var(--c-muted);
}

/* Right meta */
.exp-meta {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
  color: var(--c-muted);
  flex-shrink: 0;
  padding-top: 3px;
  white-space: nowrap;
}

/* Hover-expand detail */
.exp-detail {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  padding-left: 56px;
  font-family: 'Noto Serif SC', serif;
  font-size: 13px;
  font-weight: 300;
  color: var(--c-muted);
  line-height: 1.9;
  transition: max-height 0.28s ease, opacity 0.2s ease, padding-bottom 0.28s ease;
  padding-bottom: 0;
}
.exp-item:hover .exp-detail {
  max-height: 100px;
  opacity: 1;
  padding-bottom: 8px;
}

/* ── Says · Timeline Feed ── */
.vb-feed { display: flex; flex-direction: column; }
.vb-entry {
  display: grid;
  grid-template-columns: 28px 1fr;
  gap: 0 12px;
  padding: 0 0 20px;
}
.vb-entry:last-child { padding-bottom: 0; }
.vb-spine {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.vb-dot {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  text-decoration: none;
  color: #fff;
  margin-top: 2px;
  transition: opacity 0.15s, transform 0.15s;
}
.vb-dot:hover { opacity: 0.8; transform: scale(1.08); }
.vb-dot-twitter  { background: #09090b; }
.vb-dot-douban   { background: #07A761; }
.vb-dot-threads  { background: #09090b; }
.vb-dot-weread   { background: #1A7E4A; }
.vb-dot-instagram { background: linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }
.vb-line {
  width: 1px;
  background: var(--c-border);
  flex: 1;
  margin-top: 5px;
  min-height: 10px;
}
.vb-entry:last-child .vb-line { display: none; }
.vb-content { padding-top: 3px; }
.vb-date {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  color: var(--c-muted);
  letter-spacing: 0.06em;
  font-weight: 300;
  margin-bottom: 6px;
}
.vb-text {
  font-family: 'Noto Serif SC', serif;
  font-size: 13.5px;
  font-weight: 300;
  line-height: 1.95;
  color: var(--c-text);
}
.vb-images { display: flex; gap: 5px; margin-top: 9px; flex-wrap: wrap; }
.vb-images img { width: 68px; height: 68px; object-fit: cover; border-radius: 2px; }
.says-more {
  display: block;
  margin-top: 18px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  color: var(--c-muted);
  text-decoration: none;
  text-align: right;
}
.says-more:hover { color: var(--c-text); text-decoration: underline; text-underline-offset: 3px; }
.hp-footer {
  margin-top: 48px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px;
  color: var(--c-muted);
  text-align: right;
}

/* ── Responsive ── */
@media (max-width: 640px) {
  .hp { padding: 0 16px; }
  .hp-inner { padding: 48px 0 72px; }
  .hp-name { font-size: 24px; }
  .hp-avatar { width: 44px; height: 44px; }
}
</style>

<div class="hp">
<div class="hp-inner">

<header class="hp-header">
<div>
  <h1 class="hp-name">冯诺</h1>
  <p class="hp-bio">译者 · 写作者 · 业余开发者</p>
  <nav class="hp-nav">
    <a href="https://www.douban.com/people/L.Revolution/" target="_blank">豆瓣</a>
    <span class="hp-nav-sep">/</span>
    <a href="https://x.com/Surudo1892" target="_blank">X</a>
    <span class="hp-nav-sep">/</span>
    <a href="https://github.com/YOUR_GITHUB_USERNAME" target="_blank">GitHub</a>
  </nav>
</div>
</header>

<section class="hp-section">
<p class="hp-section-label">作品</p>
<ul class="exp-list">

  <li>
  <a class="exp-item" href="/books">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Book / 译 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 19.5A2.5 2.5 0 016.5 17H20"/>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">译的书</div>
        <div class="exp-sub">已出版多部译作<span class="exp-sub-dot"> · </span>人文社科</div>
      </div>
      <div class="exp-meta">Translator</div>
    </div>
    <div class="exp-detail">↳ 翻译人文社科类书籍，已出版多部译作，涵盖社会学、历史、文化等领域。</div>
  </a>
  </li>

  <li>
  <a class="exp-item" href="/writing">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Pen / 写 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 20h9"/>
          <path d="M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">写的文</div>
        <div class="exp-sub">随笔 · 书评<span class="exp-sub-dot"> · </span>当代观察</div>
      </div>
      <div class="exp-meta">Writer</div>
    </div>
    <div class="exp-detail">↳ 关于阅读、思考与当代生活的随笔与书评。</div>
  </a>
  </li>

  <li>
  <a class="exp-item" href="/projects">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Code / 编 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="16 18 22 12 16 6"/>
          <polyline points="8 6 2 12 8 18"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">编的程</div>
        <div class="exp-sub">独立项目<span class="exp-sub-dot"> · </span>开源工具</div>
      </div>
      <div class="exp-meta">Developer</div>
    </div>
    <div class="exp-detail">↳ 业余时间开发的独立项目与开源工具。</div>
  </a>
  </li>

</ul>
</section>

<section class="hp-section">
<p class="hp-section-label">兴趣</p>
<ul class="exp-list">

  <li>
  <a class="exp-item" href="/reading">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Open book / 读 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/>
          <path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">读的书</div>
        <div class="exp-sub">书单与阅读记录</div>
      </div>
    </div>
    <div class="exp-detail">↳ 在读、读过与想读的书单，以及零散的阅读笔记。</div>
  </a>
  </li>

  <li>
  <a class="exp-item" href="/movies">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Film / 影 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/>
          <line x1="7" y1="2" x2="7" y2="22"/>
          <line x1="17" y1="2" x2="17" y2="22"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <line x1="2" y1="7" x2="7" y2="7"/>
          <line x1="2" y1="17" x2="7" y2="17"/>
          <line x1="17" y1="17" x2="22" y2="17"/>
          <line x1="17" y1="7" x2="22" y2="7"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">观的影</div>
        <div class="exp-sub">影单与观后感</div>
      </div>
    </div>
    <div class="exp-detail">↳ 看过与想看的电影列表，偶尔写些观后感。</div>
  </a>
  </li>

  <li>
  <a class="exp-item" href="/music">
    <div class="exp-row">
      <div class="exp-icon-wrap">
        <!-- Music / 乐 icon -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 18V5l12-2v13"/>
          <circle cx="6" cy="18" r="3"/>
          <circle cx="18" cy="16" r="3"/>
        </svg>
      </div>
      <div class="exp-body">
        <div class="exp-title">听的乐</div>
        <div class="exp-sub">歌单与音乐记录</div>
      </div>
    </div>
    <div class="exp-detail">↳ 最近在听的音乐与歌单整理。</div>
  </a>
  </li>

</ul>
</section>

<section class="hp-section">
<p class="hp-section-label">碎碎念</p>

<!-- SAYS_START -->
<div class="vb-feed">
<div class="vb-entry"><div class="vb-spine"><a class="vb-dot vb-dot-twitter" href="https://x.com/Surudo1892/status/2042573393376002534" target="_blank" title="twitter"><svg viewBox="0 0 24 24" fill="currentColor" width="10" height="10"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg></a><div class="vb-line"></div></div><div class="vb-content"><p class="vb-date">2026 · 04 · 10</p><p class="vb-text">Proper lad. Last summer I went to Hong Kong wearing No. 23 shirt to watch our team play against AC Milan in a friendly. Liverpool FC (@LFC) We can confirm Andy Robertson will bring his Reds career to …</p><div class="vb-images"><img src="https://nitter.net/pic/pbs.twimg.com%2Fmedia%2FHFepjb7XAAA9OVg.jpg" loading="lazy" alt=""></div></div></div>
<div class="vb-entry"><div class="vb-spine"><a class="vb-dot vb-dot-twitter" href="https://x.com/Surudo1892/status/2037377311851593733" target="_blank" title="twitter"><svg viewBox="0 0 24 24" fill="currentColor" width="10" height="10"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg></a><div class="vb-line"></div></div><div class="vb-content"><p class="vb-date">2026 · 03 · 27</p><p class="vb-text">Why is the avatar of this subreddit Zhu Yuanzhang? Images That Make You Feel Pain (@ManMilk2) — https://nitter.net/ManMilk2/status/2037258288409031039#m</p><div class="vb-images"><img src="https://nitter.net/pic/media%2FHEXLnbKWcAA1OIv.jpg" loading="lazy" alt=""></div></div></div>
<div class="vb-entry"><div class="vb-spine"><a class="vb-dot vb-dot-twitter" href="https://x.com/Surudo1892/status/2031092860221796511" target="_blank" title="twitter"><svg viewBox="0 0 24 24" fill="currentColor" width="10" height="10"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg></a><div class="vb-line"></div></div><div class="vb-content"><p class="vb-date">2026 · 03 · 09</p><p class="vb-text">Who tf says it’s romantic in books? Atlas Press (@realAtlasPress) “Being poor is only romantic in books.” —Sidney Sheldon — https://nitter.net/realAtlasPress/status/2030690508729614529#m</p><div class="vb-images"><img src="https://nitter.net/pic/media%2FHC5hTtrbwAEVCfl.jpg" loading="lazy" alt=""></div></div></div>
<div class="vb-entry"><div class="vb-spine"><a class="vb-dot vb-dot-twitter" href="https://x.com/Surudo1892/status/2028347298066182629" target="_blank" title="twitter"><svg viewBox="0 0 24 24" fill="currentColor" width="10" height="10"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg></a><div class="vb-line"></div></div><div class="vb-content"><p class="vb-date">2026 · 03 · 02</p><p class="vb-text">支持！ 玩个锤子 (@cccchuizi) 【开工季福利来袭！！！】 为了感谢大家对我们的支持，我们打算免费送一台 Mac Mini256GB + 2000刀PackyAPI额度，助力2026年VibeCoding 和养殖龙虾！ 一等奖：macmini 256GB 一台 二等奖：Packyapi额度100 刀✖️10 人 三等奖：Packyapi额度50 刀✖️20 人 点赞+评论+转发即可参与抽…</p><div class="vb-images"><img src="https://nitter.net/pic/media%2FHCX7AjGbMAAIQuN.jpg" loading="lazy" alt=""></div></div></div>
<div class="vb-entry"><div class="vb-spine"><a class="vb-dot vb-dot-twitter" href="https://x.com/Surudo1892/status/2028075316015468749" target="_blank" title="twitter"><svg viewBox="0 0 24 24" fill="currentColor" width="10" height="10"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.647l7.73-8.835L1.254 2.25H8.08l4.259 5.63L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg></a><div class="vb-line"></div></div><div class="vb-content"><p class="vb-date">2026 · 03 · 01</p><p class="vb-text">This guy just went to pee and his colleagues chose him to be the next Supreme Leader. Visegrád 24 (@visegrad24) BREAKING: Ayatollah Arafi has been appointed as the acting Supreme Leader of Iran, ISNA …</p><div class="vb-images"><img src="https://nitter.net/pic/media%2FHCUTHUsWsAA0p_h.jpg" loading="lazy" alt=""></div></div></div>
</div>
<!-- SAYS_END -->

<a class="says-more" href="/says">查看更多 →</a>
</section>

<footer class="hp-footer">© 2026 冯诺</footer>
</div>
</div>
