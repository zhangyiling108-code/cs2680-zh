(function () {
  const root = document.documentElement;
  const body = document.body;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* 存储不可用时忽略 */ } },
  };

  // 深浅色
  const savedTheme = store.get("cs2680-theme");
  if (savedTheme) root.dataset.theme = savedTheme;
  const themeBtn = document.querySelector(".theme");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    const dark = root.dataset.theme
      ? root.dataset.theme === "dark"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    store.set("cs2680-theme", root.dataset.theme);
  });

  const slides = Array.from(document.querySelectorAll(".slide"));
  if (!slides.length) { body.classList.add("home-page"); return; }

  // 显示模式：对照 / 中文 / 原版
  const modeBtns = document.querySelectorAll(".seg button");
  const setMode = (m) => {
    body.dataset.mode = m;
    modeBtns.forEach((b) => b.classList.toggle("on", b.dataset.mode === m));
    store.set("cs2680-mode", m);
  };
  setMode(store.get("cs2680-mode") || "both");
  modeBtns.forEach((b) => b.addEventListener("click", () => setMode(b.dataset.mode)));

  // 目录高亮
  const tocLinks = new Map(Array.from(document.querySelectorAll(".toc a")).map((a) => [a.getAttribute("href").slice(1), a]));
  let current = slides[0];
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      current = e.target;
      tocLinks.forEach((a) => a.classList.remove("on"));
      const a = tocLinks.get(e.target.id);
      if (a) { a.classList.add("on"); a.scrollIntoView({ block: "nearest" }); }
    });
  }, { rootMargin: "-30% 0px -60% 0px" });
  slides.forEach((s) => io.observe(s));

  // 键盘翻页
  document.addEventListener("keydown", (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey || /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    const i = slides.indexOf(current);
    let next = null;
    if (e.key === "ArrowRight" || e.key === "j") next = slides[Math.min(i + 1, slides.length - 1)];
    if (e.key === "ArrowLeft" || e.key === "k") next = slides[Math.max(i - 1, 0)];
    if (e.key === "Escape") lightbox.hidden = true;
    if (next) { e.preventDefault(); next.scrollIntoView(); current = next; }
  });

  // 原图放大
  const lightbox = document.querySelector(".lightbox");
  const lbImg = lightbox.querySelector("img");
  document.querySelectorAll(".orig img").forEach((img) => img.addEventListener("click", () => {
    lbImg.src = img.src; lbImg.alt = img.alt; lightbox.hidden = false;
  }));
  lightbox.addEventListener("click", () => { lightbox.hidden = true; });
})();
