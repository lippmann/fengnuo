---
title: 译的书
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;700;900&family=IBM+Plex+Mono:ital,wght@0,200;0,300;0,400;1,300&display=swap" rel="stylesheet">

<style>
/* ── Quartz chrome reset (scoped to books/index for specificity) ── */
body[data-slug="books/index"] .sidebar,
body[data-slug="books/index"] .page-header,
body[data-slug="books/index"] .page-footer,
body[data-slug="books/index"] footer,
body[data-slug="books/index"] hr,
body[data-slug="books/index"] .breadcrumb-container,
body[data-slug="books/index"] h1.article-title,
body[data-slug="books/index"] .content-meta,
body[data-slug="books/index"] .tags,
body[data-slug="books/index"] .left.sidebar,
body[data-slug="books/index"] .right.sidebar,
body[data-slug="books/index"] .backlinks,
body[data-slug="books/index"] .graph{display:none!important}
body[data-slug="books/index"] #quartz-root{display:block!important;padding:0!important;margin:0!important;max-width:none!important;width:100%!important}
body[data-slug="books/index"] #quartz-body{display:block!important;padding:0!important;margin:0!important;gap:0!important;max-width:none!important;width:100%!important}
body[data-slug="books/index"] .center{all:unset!important;display:block!important;width:100%!important;max-width:none!important;padding:0!important;margin:0!important}
body[data-slug="books/index"] article.popover-hint{padding:0!important;max-width:100%!important;margin:0!important;width:100%!important}
body[data-slug="books/index"] h1>a,
body[data-slug="books/index"] h2>a{display:none!important}
.bk a,.bk a.internal{color:inherit!important;text-decoration:none!important;border-bottom:none!important;background:transparent!important;padding:0!important;border-radius:0!important;font-weight:inherit!important}

/* ── Light theme (default) ── */
.bk {
  --bg:      #ffffff;
  --surface: #f4f4f5;
  --paper:   #09090b;
  --dim:     #52525b;
  --muted:   #71717a;
  --rule:    #e4e4e7;
  --gold:    #c9a96e;
  --gold-d:  #8a6f3e;
  --paper-dim:     rgba(9,9,11,.55);
  --paper-faint:   rgba(9,9,11,.45);
  --author-span:   rgba(9,9,11,.5);
  --nav-gradient:  linear-gradient(to bottom, rgba(255,255,255,.97) 70%, transparent);
  --cover-overlay: linear-gradient(135deg, rgba(0,0,0,.02), transparent 60%);
  --hero-stroke:   rgba(0,0,0,.03);
  --shadow-sm:     0 2px 8px rgba(0,0,0,.08), 0 12px 40px rgba(0,0,0,.1), 0 1px 0 rgba(0,0,0,.04);
  --shadow-hover:  0 6px 24px rgba(0,0,0,.12), 0 24px 64px rgba(0,0,0,.16), 0 0 32px rgba(201,169,110,.06);
}

/* ── Dark theme ── */
.bk.is-dark {
  --bg:      #0e0c0a;
  --surface: #161310;
  --paper:   #f0ebe2;
  --dim:     #7a7268;
  --muted:   #453f38;
  --rule:    #211e1a;
  --gold:    #c9a96e;
  --gold-d:  #8a6f3e;
  --paper-dim:     rgba(240,235,226,.5);
  --paper-faint:   rgba(240,235,226,.45);
  --author-span:   rgba(240,235,226,.5);
  --nav-gradient:  linear-gradient(to bottom, rgba(14,12,10,.97) 70%, transparent);
  --cover-overlay: linear-gradient(135deg, rgba(201,169,110,.04), transparent 60%);
  --hero-stroke:   rgba(201,169,110,.05);
  --shadow-sm:     0 4px 16px rgba(0,0,0,.5), 0 20px 60px rgba(0,0,0,.7), 0 1px 0 rgba(255,255,255,.05);
  --shadow-hover:  0 8px 32px rgba(0,0,0,.6), 0 32px 80px rgba(0,0,0,.8), 0 0 40px rgba(201,169,110,.08);
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}

.bk {
  background: var(--bg);
  color: var(--paper);
  font-family: 'IBM Plex Mono', monospace;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
  transition: background .25s, color .25s;
}

/* ── NAV ── */
.bk-nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 99;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 52px;
  height: 56px;
  background: var(--nav-gradient);
  transition: background .25s;
}
.bk-nav-home {
  font-family: 'Noto Serif SC', serif;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .02em;
  opacity: .7;
  transition: opacity .2s;
}
.bk-nav-home:hover { opacity: 1; }
.bk-nav-links {
  display: flex;
  gap: 28px;
}
.bk-nav-links a {
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--dim);
  transition: color .2s;
}
.bk-nav-links a:hover { color: var(--paper); }
.bk-nav-links a.here { color: var(--gold); }
.bk-theme-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--dim);
  display: flex;
  align-items: center;
  padding: 4px;
  transition: color .2s;
}
.bk-theme-btn:hover { color: var(--paper); }
.bk-theme-btn svg { width: 15px; height: 15px; }

/* ── HERO ── */
.bk-hero {
  min-height: 100vh;
  display: flex;
  align-items: flex-end;
  padding: 0 52px 88px;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--rule);
}
.bk-hero-bg {
  position: absolute;
  right: -4vw; top: 50%;
  transform: translateY(-50%);
  font-family: 'Noto Serif SC', serif;
  font-size: 55vw;
  font-weight: 900;
  line-height: 1;
  color: transparent;
  -webkit-text-stroke: 1px var(--hero-stroke);
  user-select: none;
  pointer-events: none;
  letter-spacing: -.04em;
}
.bk-hero-content {
  position: relative;
  z-index: 2;
  max-width: 600px;
}
.bk-hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 10px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 300;
  margin-bottom: 28px;
}
.bk-hero-eyebrow::before {
  content: '';
  display: block;
  width: 28px; height: 1px;
  background: var(--gold);
  opacity: .6;
}
.bk-hero-title {
  font-family: 'Noto Serif SC', serif;
  font-size: clamp(48px, 7vw, 88px);
  font-weight: 900;
  line-height: 1.05;
  letter-spacing: .04em;
  color: var(--paper);
  margin-bottom: 20px;
}
.bk-hero-count {
  font-size: 10px;
  letter-spacing: .2em;
  color: var(--dim);
  font-weight: 300;
  margin-bottom: 36px;
}
.bk-hero-rule {
  width: 40px; height: 1px;
  background: var(--gold);
  opacity: .35;
  margin-bottom: 20px;
}
.bk-hero-desc {
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  font-weight: 300;
  line-height: 2;
  color: var(--paper-faint);
  max-width: 380px;
}
.bk-hero-scroll {
  position: absolute;
  bottom: 40px; right: 52px;
  z-index: 2;
  writing-mode: vertical-rl;
  font-size: 9px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 10px;
}
.bk-hero-scroll-line {
  width: 1px; height: 40px;
  background: linear-gradient(to bottom, var(--muted), transparent);
}

/* ── BOOK LIST ── */
.bk-list { padding: 0 0 120px; }
.bk-entry {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 540px;
  border-bottom: 1px solid var(--rule);
  position: relative;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
}
.bk-entry:nth-child(even) { direction: rtl; }
.bk-entry:nth-child(even) > * { direction: ltr; }

.bk-cover-col {
  position: relative;
  overflow: hidden;
  background: var(--surface);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 64px 80px;
  transition: background .25s;
}
.bk-cover-col::after {
  content: '';
  position: absolute; inset: 0;
  background: var(--cover-overlay);
  pointer-events: none;
}
.bk-cover-img {
  position: relative;
  z-index: 1;
  max-width: 220px;
  width: 100%;
  aspect-ratio: 2/3;
  object-fit: cover;
  display: block;
  box-shadow: var(--shadow-sm);
  border-radius: 2px;
  transition: transform .5s cubic-bezier(.22,1,.36,1), box-shadow .5s ease;
}
.bk-entry:hover .bk-cover-img {
  transform: translateY(-12px) scale(1.02);
  box-shadow: var(--shadow-hover);
}
.bk-info-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 64px 72px;
  border-left: 1px solid var(--rule);
}
.bk-entry:nth-child(even) .bk-info-col {
  border-left: none;
  border-right: 1px solid var(--rule);
}
.bk-num {
  font-size: 9px;
  letter-spacing: .2em;
  color: var(--gold-d);
  margin-bottom: 24px;
  font-weight: 300;
}
.bk-title {
  font-family: 'Noto Serif SC', serif;
  font-size: clamp(24px, 3vw, 36px);
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: .02em;
  color: var(--paper);
  margin-bottom: 6px;
  transition: color .2s;
}
.bk-entry:hover .bk-title { color: var(--gold); }
.bk-original {
  font-style: italic;
  font-size: 12px;
  font-weight: 200;
  color: var(--dim);
  letter-spacing: .04em;
  margin-bottom: 8px;
}
.bk-author {
  font-size: 11px;
  color: var(--dim);
  font-weight: 300;
  letter-spacing: .06em;
  margin-bottom: 32px;
}
.bk-author span { color: var(--author-span); }
.bk-divider {
  width: 32px; height: 1px;
  background: rgba(201,169,110,.25);
  margin-bottom: 28px;
}
.bk-desc {
  font-family: 'Noto Serif SC', serif;
  font-size: 14px;
  font-weight: 300;
  line-height: 2;
  color: var(--paper-dim);
  max-width: 400px;
  margin-bottom: 36px;
}
.bk-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 24px;
  border-top: 1px solid var(--rule);
}
.bk-year {
  font-size: 10px;
  letter-spacing: .16em;
  color: var(--dim);
  font-weight: 300;
}
.bk-link {
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--gold-d);
  transition: color .2s;
  display: flex;
  align-items: center;
  gap: 8px;
}
.bk-link:hover { color: var(--gold); }
.bk-link::after { content: '→'; transition: transform .2s; }
.bk-entry:hover .bk-link::after { transform: translateX(4px); }

/* ── FOOTER ── */
.bk-foot {
  border-top: 1px solid var(--rule);
  padding: 28px 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.bk-foot-back {
  font-size: 11px;
  letter-spacing: .1em;
  color: var(--dim);
  transition: color .2s;
}
.bk-foot-back:hover { color: var(--paper); }
.bk-foot-copy {
  font-size: 9px;
  letter-spacing: .12em;
  color: var(--muted);
}

@media (max-width: 860px) {
  .bk-entry, .bk-entry:nth-child(even) { grid-template-columns: 1fr; direction: ltr; }
  .bk-cover-col { padding: 48px; min-height: 360px; }
  .bk-info-col { padding: 40px 32px; border-left: none !important; border-right: none !important; border-top: 1px solid var(--rule); }
  .bk-nav { padding: 0 24px; }
  .bk-hero { padding: 0 24px 72px; }
  .bk-foot { padding: 24px; }
}
</style>

<div class="bk" id="bk-root">

<nav class="bk-nav">
  <a class="bk-nav-home" href="/">冯诺</a>
  <div class="bk-nav-links">
    <a href="/books" class="here">译的书</a>
    <a href="/writing">写的文</a>
    <a href="/projects">编的程</a>
  </div>
  <button class="bk-theme-btn" id="bk-theme-btn" onclick="bkToggleTheme()" aria-label="切换主题">
    <svg id="bk-icon-sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="display:none">
      <circle cx="12" cy="12" r="4"/>
      <line x1="12" y1="2" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="22"/>
      <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
      <line x1="2" y1="12" x2="4" y2="12"/><line x1="20" y1="12" x2="22" y2="12"/>
      <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
    </svg>
    <svg id="bk-icon-moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
    </svg>
  </button>
</nav>

<section class="bk-hero">
  <div class="bk-hero-bg" aria-hidden="true">译</div>
  <div class="bk-hero-content">
    <p class="bk-hero-eyebrow">Works · Translation</p>
    <h1 class="bk-hero-title">译的书</h1>
    <p class="bk-hero-count">8 Volumes &nbsp;·&nbsp; 2018 — 2024</p>
    <div class="bk-hero-rule"></div>
    <p class="bk-hero-desc">在两种语言之间寻找对等，<br>在两个世界之间架设桥梁。</p>
  </div>
  <div class="bk-hero-scroll">
    <span class="bk-hero-scroll-line"></span>
    Scroll
  </div>
</section>

<section class="bk-list">

  <a class="bk-entry" href="https://book.douban.com/subject/37066249/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img9.doubanio.com/view/subject/l/public/s34975355.jpg" alt="错误警报" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">01 / 08</div>
      <h2 class="bk-title">错误警报</h2>
      <p class="bk-original">False Alarm</p>
      <p class="bk-author"><span>作者</span> 比约恩·隆伯格（Bjørn Lomborg）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">用可信数据挑战全球变暖共识。媒体渲染的气候末日是虚惊一场吗？普通人被迫改变生活方式，各国领导人承诺减排政策，但这些政策真的有效吗？《时代》全球百位最具影响力人物的代表作。</p>
      <div class="bk-footer">
        <span class="bk-year">2024 · 浙江人民出版社</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/36453354/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img3.doubanio.com/view/subject/l/public/s34642537.jpg" alt="被互联网辜负的人" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">02 / 08</div>
      <h2 class="bk-title">被互联网辜负的人</h2>
      <p class="bk-original">The Gentrification of the Internet</p>
      <p class="bk-author"><span>作者</span> 杰西·林格尔（Jessie Lingel）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">互联网如何从DIY反主流文化的空间，变成企业寡头的游乐场？20年间，互联网像遭遇士绅化的老城区，变得光鲜却失去多样性——把最初搭建社区的人扫地出门。</p>
      <div class="bk-footer">
        <span class="bk-year">2023 · 浙江人民出版社 / 潮汐</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/37106144/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img1.doubanio.com/view/subject/l/public/s34999389.jpg" alt="热点！" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">03 / 08</div>
      <h2 class="bk-title">热点！</h2>
      <p class="bk-original">如何一眼辨别真假信息</p>
      <p class="bk-author"><span>作者</span> 尼克·谢里登（Nick Sheridan，1992—2024）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">走入获奖记者谢里登的一天，了解新闻的生产与传播，学会在信息洪流中鉴别真假、追求真相。作者于2024年因病辞世，年仅32岁。锻炼批判性思维，保持理性好奇。</p>
      <div class="bk-footer">
        <span class="bk-year">2024</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/36641005/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img3.doubanio.com/view/subject/l/public/s34694203.jpg" alt="人物设定创意宝库" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">04 / 08</div>
      <h2 class="bk-title">人物设定创意宝库</h2>
      <p class="bk-original">积极特质词汇速查，塑造值得支持的人物</p>
      <p class="bk-author"><span>作者</span> 安杰拉·阿克曼 &amp; 贝卡·普利西</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">全球畅销的故事创作工具书。99种人物积极特质，助你合理调制性格配方，为角色注入生命。小说家、编剧、动漫创作者奉为实用宝典。系列全球累计销量破百万。</p>
      <div class="bk-footer">
        <span class="bk-year">2023</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/36337285/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img1.doubanio.com/view/subject/l/public/s34483849.jpg" alt="我所说的话" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">05 / 08</div>
      <h2 class="bk-title">我所说的话</h2>
      <p class="bk-original">What I Say</p>
      <p class="bk-author"><span>作者</span> 本·贝利·史密斯（Ben Bailey Smith）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">13岁少年在才艺之夜意外表演了一场脱口秀，将话题对准家人和学校，引发轰动。在一系列动人心弦的事件之后，他开始重新思考对他来说什么才是真正重要的。</p>
      <div class="bk-footer">
        <span class="bk-year">2023</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/35067904/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img3.doubanio.com/view/subject/l/public/s33873703.jpg" alt="一路微光" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">06 / 08</div>
      <h2 class="bk-title">一路微光</h2>
      <p class="bk-original">A Lite Too Bright</p>
      <p class="bk-author"><span>作者</span> 塞缪尔·米勒（Samuel Miller）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">18岁少年追查畅销书作家爷爷死前的神秘失踪，踏上横跨美国的火车旅程。一条条支离破碎的线索，一个个环环相扣的陷阱——六十年后致敬《在路上》的青春之作。2018年《出版人周刊》十佳青少年读物。</p>
      <div class="bk-footer">
        <span class="bk-year">2021</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/35018390/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img1.doubanio.com/view/subject/l/public/s33610310.jpg" alt="安徒生童话" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">07 / 08</div>
      <h2 class="bk-title">安徒生童话</h2>
      <p class="bk-original">Hans Christian Andersen</p>
      <p class="bk-author"><span>作者</span> 汉斯·克里斯蒂安·安徒生（1805—1875）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">精选15篇安徒生童话名篇，西班牙著名插画师乔迪·维拉·德尔克洛斯绘制精美插图，丹麦欧登塞安徒生博物馆官方授权图片。致每一个小孩和心里住着小孩的大人。</p>
      <div class="bk-footer">
        <span class="bk-year">2021</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

  <a class="bk-entry" href="https://book.douban.com/subject/30323396/" target="_blank">
    <div class="bk-cover-col">
      <img class="bk-cover-img" src="https://img9.doubanio.com/view/subject/l/public/s29866765.jpg" alt="从早茫到晚" loading="lazy">
    </div>
    <div class="bk-info-col">
      <div class="bk-num">08 / 08</div>
      <h2 class="bk-title">从早「茫」到晚</h2>
      <p class="bk-original">都市上班族的每日渡劫和永恒轮回</p>
      <p class="bk-author"><span>作者</span> 西沃恩·加拉格尔（Siobhán Gallagher）</p>
      <div class="bk-divider"></div>
      <p class="bk-desc">为都市青年而作的互动绘本。多条剧情线，大量内心戏，生动还原都市青年日常的小确丧——从工作日到周末，从挣扎起床到深夜社恐，全球各地青年的精神状态高度相似。</p>
      <div class="bk-footer">
        <span class="bk-year">2018</span>
        <span class="bk-link">豆瓣</span>
      </div>
    </div>
  </a>

</section>

<footer class="bk-foot">
  <a class="bk-foot-back" href="/">← 返回主页</a>
  <span class="bk-foot-copy">© 2026 冯诺</span>
</footer>

</div>

<script>
function bkUpdateIcon(isDark) {
  document.getElementById('bk-icon-sun').style.display  = isDark ? 'block' : 'none';
  document.getElementById('bk-icon-moon').style.display = isDark ? 'none'  : 'block';
}
function bkToggleTheme() {
  var root = document.getElementById('bk-root');
  var isDark = root.classList.contains('is-dark');
  root.classList.toggle('is-dark', !isDark);
  localStorage.setItem('books-theme', isDark ? 'light' : 'dark');
  bkUpdateIcon(!isDark);
}
(function () {
  var saved = localStorage.getItem('books-theme') || 'light';
  if (saved === 'dark') document.getElementById('bk-root').classList.add('is-dark');
  bkUpdateIcon(saved === 'dark');
}());
</script>
