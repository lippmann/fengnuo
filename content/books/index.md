---
title: 译的书
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;900&family=IBM+Plex+Mono:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">

<style>
/* ── Quartz chrome reset ── */
.sidebar,.page-header,.page-footer,footer,hr,
.breadcrumb-container,h1.article-title,.content-meta,.tags,
.left.sidebar,.right.sidebar,.backlinks,.graph{display:none!important}
#quartz-body{display:block!important;padding:0!important;margin:0!important;gap:0!important}
.center{all:unset!important;display:block!important;width:100%!important;padding:0!important;margin:0!important}
article.popover-hint{padding:0!important;max-width:100%!important;margin:0!important}
h1>a,h2>a{display:none!important}
.tl a,.tl a.internal{color:inherit!important;text-decoration:none!important;border-bottom:none!important;background:transparent!important;padding:0!important;border-radius:0!important;font-weight:inherit!important}

/* ── Tokens ── */
:root{
  --ink:   #0c0a08;
  --paper: #f5f0e8;
  --gold:  #b8935a;
  --dim:   #6b6257;
  --rule:  #242018;
  --card:  #141210;
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

/* ── Keyframes ── */
@keyframes fadeUp{
  from{opacity:0;transform:translateY(28px)}
  to  {opacity:1;transform:translateY(0)}
}
@keyframes fadeIn{
  from{opacity:0}
  to  {opacity:1}
}

/* ── Shell ── */
.tl{
  background:var(--ink);
  min-height:100vh;
  color:var(--paper);
  font-family:'IBM Plex Mono',monospace;
}

/* ── Top nav bar ── */
.tl-nav{
  position:fixed;
  top:0;left:0;right:0;
  z-index:100;
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:20px 48px;
  background:linear-gradient(to bottom,rgba(12,10,8,.96) 60%,transparent);
}
.tl-nav-home{
  font-family:'Noto Serif SC',serif;
  font-size:15px;
  font-weight:900;
  color:var(--paper);
  text-decoration:none;
  letter-spacing:.02em;
  opacity:.8;
  transition:opacity .2s;
}
.tl-nav-home:hover{opacity:1}
.tl-nav-links{
  display:flex;
  gap:28px;
}
.tl-nav-links a{
  font-size:10px;
  letter-spacing:.18em;
  color:var(--dim);
  text-decoration:none;
  text-transform:uppercase;
  transition:color .2s;
}
.tl-nav-links a:hover{color:var(--paper)}
.tl-nav-links a.here{color:var(--gold)}

/* ── Hero ── */
.tl-hero{
  position:relative;
  min-height:100vh;
  display:flex;
  align-items:flex-end;
  padding:0 48px 80px;
  overflow:hidden;
}
/* Giant background 译 */
.tl-hero-bg{
  position:absolute;
  top:50%;right:-2vw;
  transform:translateY(-50%);
  font-family:'Noto Serif SC',serif;
  font-size:52vw;
  font-weight:900;
  line-height:1;
  color:transparent;
  -webkit-text-stroke:1px rgba(184,147,90,.06);
  user-select:none;
  pointer-events:none;
  animation:fadeIn 2s ease both;
  animation-delay:.3s;
  letter-spacing:-.05em;
}
/* subtle grain overlay */
.tl-hero::before{
  content:'';
  position:absolute;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.035'/%3E%3C/svg%3E");
  background-size:200px;
  opacity:.4;
  pointer-events:none;
  z-index:1;
}
.tl-hero-content{
  position:relative;
  z-index:2;
  max-width:680px;
  animation:fadeUp .9s cubic-bezier(.22,1,.36,1) both;
  animation-delay:.1s;
}
.tl-hero-eyebrow{
  font-size:10px;
  letter-spacing:.24em;
  color:var(--gold);
  font-weight:300;
  margin-bottom:24px;
  display:flex;
  align-items:center;
  gap:12px;
}
.tl-hero-eyebrow::before{
  content:'';
  display:block;
  width:32px;height:1px;
  background:var(--gold);
  opacity:.6;
}
.tl-hero-title{
  font-family:'Noto Serif SC',serif;
  font-size:clamp(52px,8vw,96px);
  font-weight:900;
  line-height:1.05;
  letter-spacing:.04em;
  color:var(--paper);
  margin-bottom:20px;
}
.tl-hero-sub{
  font-size:11px;
  letter-spacing:.14em;
  color:var(--dim);
  font-weight:300;
  margin-bottom:40px;
}
.tl-hero-rule{
  width:48px;height:1px;
  background:var(--gold);
  opacity:.4;
  margin-bottom:20px;
}
.tl-hero-desc{
  font-family:'Noto Serif SC',serif;
  font-size:14px;
  font-weight:300;
  line-height:2;
  color:rgba(245,240,232,.55);
  max-width:420px;
}

/* ── Scroll cue ── */
.tl-scroll{
  position:absolute;
  bottom:40px;left:48px;
  z-index:2;
  display:flex;
  align-items:center;
  gap:10px;
  font-size:9px;
  letter-spacing:.2em;
  color:var(--dim);
  animation:fadeUp .8s ease both;
  animation-delay:.8s;
}
.tl-scroll-line{
  width:32px;height:1px;
  background:var(--dim);
  animation:scrollPulse 2.4s ease-in-out infinite;
}
@keyframes scrollPulse{
  0%,100%{width:32px;opacity:.4}
  50%{width:48px;opacity:.8}
}

/* ── Books section ── */
.tl-section{
  padding:96px 48px;
  border-top:1px solid var(--rule);
}
.tl-section-label{
  font-size:9px;
  letter-spacing:.24em;
  color:var(--dim);
  text-transform:uppercase;
  margin-bottom:64px;
  display:flex;
  align-items:center;
  gap:16px;
}
.tl-section-label::after{
  content:'';flex:1;height:1px;
  background:var(--rule);
}

/* Book grid */
.bk-grid{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:48px 32px;
}
.bk-card{
  display:flex;
  flex-direction:column;
  gap:16px;
  text-decoration:none;
  color:inherit;
  cursor:pointer;
  animation:fadeUp .7s cubic-bezier(.22,1,.36,1) both;
}
.bk-card:nth-child(1){animation-delay:.05s}
.bk-card:nth-child(2){animation-delay:.1s}
.bk-card:nth-child(3){animation-delay:.15s}
.bk-card:nth-child(4){animation-delay:.2s}
.bk-card:nth-child(5){animation-delay:.25s}
.bk-card:nth-child(6){animation-delay:.3s}
.bk-card:nth-child(7){animation-delay:.35s}
.bk-card:nth-child(8){animation-delay:.4s}

.bk-num{
  font-size:9px;
  letter-spacing:.16em;
  color:var(--dim);
  font-weight:300;
}
.bk-cover-wrap{
  position:relative;
  aspect-ratio:2/3;
  overflow:hidden;
  border-radius:2px;
  background:var(--card);
  box-shadow:0 4px 24px rgba(0,0,0,.5),0 1px 4px rgba(0,0,0,.4);
  transition:transform .35s cubic-bezier(.22,1,.36,1),
             box-shadow .35s ease;
}
.bk-card:hover .bk-cover-wrap{
  transform:translateY(-8px) scale(1.01);
  box-shadow:0 20px 48px rgba(0,0,0,.7),0 4px 12px rgba(184,147,90,.12);
}
.bk-cover{
  width:100%;height:100%;
  object-fit:cover;
  display:block;
  transition:transform .5s cubic-bezier(.22,1,.36,1);
  filter:brightness(.95) saturate(.9);
}
.bk-card:hover .bk-cover{
  transform:scale(1.04);
  filter:brightness(1) saturate(1);
}
.bk-tag{
  position:absolute;
  bottom:10px;left:10px;
  font-size:8px;
  letter-spacing:.12em;
  background:rgba(12,10,8,.82);
  color:var(--gold);
  padding:3px 8px;
  border-radius:1px;
  backdrop-filter:blur(6px);
  border:1px solid rgba(184,147,90,.2);
}

/* Hover glow */
.bk-cover-wrap::after{
  content:'';
  position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 0%,rgba(184,147,90,.1),transparent 70%);
  opacity:0;
  transition:opacity .35s ease;
  pointer-events:none;
}
.bk-card:hover .bk-cover-wrap::after{opacity:1}

.bk-info{display:flex;flex-direction:column;gap:5px}
.bk-name{
  font-family:'Noto Serif SC',serif;
  font-size:13px;
  font-weight:400;
  color:rgba(245,240,232,.85);
  line-height:1.5;
  letter-spacing:.03em;
  transition:color .2s;
}
.bk-card:hover .bk-name{color:var(--gold)}
.bk-meta{
  font-size:9px;
  color:var(--dim);
  font-weight:300;
  letter-spacing:.1em;
}

/* ── Footer strip ── */
.tl-foot{
  border-top:1px solid var(--rule);
  padding:32px 48px;
  display:flex;
  align-items:center;
  justify-content:space-between;
}
.tl-foot-home{
  font-family:'Noto Serif SC',serif;
  font-size:13px;
  font-weight:300;
  color:var(--dim);
  text-decoration:none;
  transition:color .2s;
}
.tl-foot-home:hover{color:var(--paper)}
.tl-foot-copy{
  font-size:9px;
  letter-spacing:.12em;
  color:rgba(107,98,87,.5);
}

/* ── Responsive ── */
@media(max-width:900px){
  .bk-grid{grid-template-columns:repeat(3,1fr)}
}
@media(max-width:600px){
  .tl-nav,.tl-hero,.tl-section,.tl-foot{padding-left:24px;padding-right:24px}
  .tl-hero{padding-bottom:64px}
  .bk-grid{grid-template-columns:repeat(2,1fr);gap:32px 20px}
  .tl-hero-bg{font-size:80vw;right:-5vw}
  .tl-nav-links{display:none}
}
</style>

<div class="tl">

<!-- Nav -->
<nav class="tl-nav">
  <a class="tl-nav-home" href="/">冯诺</a>
  <div class="tl-nav-links">
    <a href="/books" class="here">译的书</a>
    <a href="/writing">写的文</a>
    <a href="/projects">编的程</a>
  </div>
</nav>

<!-- Hero -->
<section class="tl-hero">
  <div class="tl-hero-bg" aria-hidden="true">译</div>
  <div class="tl-hero-content">
    <p class="tl-hero-eyebrow">WORKS · TRANSLATION</p>
    <h1 class="tl-hero-title">译的书</h1>
    <p class="tl-hero-sub">8 VOLUMES · 2018 — 2024</p>
    <div class="tl-hero-rule"></div>
    <p class="tl-hero-desc">在两种语言之间寻找对等，<br>在两个世界之间架设桥梁。</p>
  </div>
  <div class="tl-scroll">
    <span class="tl-scroll-line"></span>
    SCROLL
  </div>
</section>

<!-- Books -->
<section class="tl-section">
  <p class="tl-section-label">全部译作</p>
  <div class="bk-grid">

    <a class="bk-card" href="https://book.douban.com/subject/37066249/" target="_blank">
      <span class="bk-num">01</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img2.doubanio.com/view/subject/l/public/s34977060.jpg" alt="错误警报" loading="lazy">
        <span class="bk-tag">社科</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">错误警报</span>
        <span class="bk-meta">2024</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/36453354/" target="_blank">
      <span class="bk-num">02</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34642537.jpg" alt="被互联网辜负的人" loading="lazy">
        <span class="bk-tag">社科</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">被互联网辜负的人</span>
        <span class="bk-meta">2023</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/37106144/" target="_blank">
      <span class="bk-num">03</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34999389.jpg" alt="热点！" loading="lazy">
        <span class="bk-tag">科普</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">热点！</span>
        <span class="bk-meta">2024</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/36641005/" target="_blank">
      <span class="bk-num">04</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s34694203.jpg" alt="人物设定创意宝库" loading="lazy">
        <span class="bk-tag">写作</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">人物设定创意宝库</span>
        <span class="bk-meta">2023</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/36337285/" target="_blank">
      <span class="bk-num">05</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s34483849.jpg" alt="我所说的话" loading="lazy">
        <span class="bk-tag">小说</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">我所说的话</span>
        <span class="bk-meta">2023</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/35067904/" target="_blank">
      <span class="bk-num">06</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img3.doubanio.com/view/subject/l/public/s33873703.jpg" alt="一路微光" loading="lazy">
        <span class="bk-tag">小说</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">一路微光</span>
        <span class="bk-meta">2021</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/35018390/" target="_blank">
      <span class="bk-num">07</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img1.doubanio.com/view/subject/l/public/s33610310.jpg" alt="安徒生童话" loading="lazy">
        <span class="bk-tag">童话</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">安徒生童话</span>
        <span class="bk-meta">2021</span>
      </div>
    </a>

    <a class="bk-card" href="https://book.douban.com/subject/30323396/" target="_blank">
      <span class="bk-num">08</span>
      <div class="bk-cover-wrap">
        <img class="bk-cover" src="https://img9.doubanio.com/view/subject/l/public/s29866765.jpg" alt="从早「茫」到晚" loading="lazy">
        <span class="bk-tag">绘本</span>
      </div>
      <div class="bk-info">
        <span class="bk-name">从早「茫」到晚</span>
        <span class="bk-meta">2018</span>
      </div>
    </a>

  </div>
</section>

<!-- Footer -->
<footer class="tl-foot">
  <a class="tl-foot-home" href="/">← 返回主页</a>
  <span class="tl-foot-copy">© 2026 冯诺</span>
</footer>

</div>
