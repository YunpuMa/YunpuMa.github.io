---
layout: about
title: About
permalink: /

profile:
  align: right
  image: portrait/prof_pic-800.webp
  image_circular: false
  chips:
    - label: Lecturer
      sublabel: LMU Munich
      url: https://www.lmu.de/
    - label: Group Leader
      sublabel: TRESP Lab
      url: https://tresp-lab.github.io/
    - label: Research Scientist
      sublabel: Huawei
      url: https://huaweiresearchcentergermanyaustria.teamtailor.com/
    - label: Member
      sublabel: MCML
      url: https://mcml.ai/

selected_papers: false
social: false

announcements:
  enabled: false
  scrollable: false
  limit: 3

latest_posts:
  enabled: false
---

<style>
  h3.accented {
    border-left: 4px solid var(--global-theme-color);
    padding-left: 0.75rem;
    margin-bottom: 1rem;
  }
  .lead-para {
    font-size: 1.07rem;
    line-height: 1.8;
  }
  .post-header {
    background: rgba(255, 255, 255, 0.4);
    border: none;
    border-radius: 0.75rem;
    padding: 1.5rem 1.75rem 0.75rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 24px rgba(78, 111, 163, 0.06);
  }
  .research-interest-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.65rem;
    margin: 1rem 0 0.5rem;
  }
  @media (max-width: 700px) {
    .research-interest-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  .research-interest-card {
    position: relative;
    display: block;
    padding: 0.75rem 0.9rem;
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(20px) saturate(160%);
    -webkit-backdrop-filter: blur(20px) saturate(160%);
    border: none;
    border-radius: 0.35rem;
    color: var(--global-text-color);
    font-size: 0.92rem;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(78, 111, 163, 0.09);
    transform: translateZ(0) scale(1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .research-interest-card:hover,
  .research-interest-card:focus-visible {
    color: var(--global-text-color);
    text-decoration: none;
    transform: translateZ(0) scale(1.015);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    z-index: 1;
  }
  .research-interest-card::after {
    content: "Click to view relevant papers";
    position: absolute;
    top: 0.55rem;
    right: 0.7rem;
    color: var(--global-text-color-light);
    font-size: 0.68rem;
    opacity: 0;
    pointer-events: none;
    white-space: nowrap;
    transition: opacity 0.2s ease;
  }
  .research-interest-card:hover::after,
  .research-interest-card:focus-visible::after {
    opacity: 0.8;
    transition-delay: 0.5s;
  }
  .research-interest-card i {
    display: block;
    line-height: 1;
    margin-bottom: 0.4rem;
    color: var(--global-theme-color);
    font-size: 1.1rem;
  }
  #affiliation-chips a {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 2px 8px rgba(78, 111, 163, 0.08);
    transform: translateZ(0) scale(1);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }
  #affiliation-chips a:hover {
    transform: translateZ(0) scale(1.06);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.10);
  }
  .profile {
    margin-top: 1.25rem;
  }
  .profile picture {
    aspect-ratio: 4 / 4.25;
    overflow: hidden;
  }
  .profile img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 46%;
  }
  html[data-theme=dark] .post-header {
    background: rgba(255, 255, 255, 0.08);
    border: none;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.15);
  }
  html[data-theme=dark] .research-interest-card {
    background: rgba(255, 255, 255, 0.07);
    border: none;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  }
  html[data-theme=dark] .research-interest-card:hover,
  html[data-theme=dark] .research-interest-card:focus-visible {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  }
  html[data-theme=dark] #affiliation-chips a {
    background: rgba(255, 255, 255, 0.07);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }
  html[data-theme=dark] #affiliation-chips a:hover {
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  }
  .latest-news-table th {
    color: rgba(78, 111, 163, 0.72);
    font-size: 0.9rem;
    font-weight: 500;
    line-height: 1.45;
    width: 20%;
  }
  html[data-theme=dark] .latest-news-table th {
    color: rgba(124, 160, 197, 0.78);
  }
  .latest-news-all {
    font-size: 0.85rem;
    display: block;
    text-align: right;
    margin-top: 0.25rem;
  }
  .news-info {
    display: inline;
    text-decoration: underline dotted;
    text-underline-offset: 3px;
    cursor: help;
    position: relative;
  }
  .news-info:focus-visible {
    outline: none;
  }
  .news-info::after {
    content: attr(data-tooltip);
    display: block;
    position: absolute;
    bottom: calc(100% + 6px);
    left: 50%;
    transform: translateX(-50%);
    width: 380px;
    padding: 6px 10px;
    background: rgba(30, 30, 30, 0.88);
    color: #f0f0f0;
    font-size: 0.78rem;
    font-weight: 400;
    line-height: 1.45;
    border-radius: 5px;
    pointer-events: none;
    white-space: normal;
    text-decoration: none;
    opacity: 0;
    transition: opacity 0.15s ease 0s;
    z-index: 100;
  }
  .news-info:hover::after,
  .news-info:focus-visible::after {
    opacity: 1;
    transition-delay: 0.1s;
  }
  html[data-theme=dark] .news-info::after {
    background: rgba(220, 220, 220, 0.92);
    color: #1a1a1a;
  }
  .news-media-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    border: 0;
    background: transparent;
    color: var(--global-theme-color);
    font-size: 1rem;
    line-height: 1;
    cursor: pointer;
  }
  .news-media-toggle:hover,
  .news-media-toggle:focus-visible {
    color: var(--global-theme-color);
  }
  .news-media {
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition:
      grid-template-rows 240ms ease,
      opacity 180ms ease,
      margin-top 240ms ease;
    margin-top: 0;
  }
  .news-media.is-open {
    grid-template-rows: 1fr;
    opacity: 1;
    margin-top: 0.85rem;
  }
  .news-media-inner {
    overflow: hidden;
  }
  .news-media img {
    display: block;
    width: min(100%, 560px);
    height: auto;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
  }
  /* Ghost atom — right side of post-header */
  .post-header { position: relative; overflow: hidden; }
  .atom-deco {
    position: absolute;
    right: 3.5rem;
    top: 0;
    bottom: 0;
    margin: auto;
    width: 160px;
    height: 160px;
    color: var(--global-theme-color);
    opacity: 0.55;
    pointer-events: none;
    filter: drop-shadow(0 0 16px rgba(78, 111, 163, 0.16));
  }
  .atom-deco svg {
    width: 100%;
    height: 100%;
    transform-origin: 50% 50%;
    transform-box: fill-box;
    animation: atom-spin 32s linear infinite;
    animation-delay: var(--atom-spin-delay, 0s);
    will-change: transform;
  }
  @keyframes atom-spin {
    to {
      transform: rotateZ(360deg);
    }
  }
  @media (prefers-reduced-motion: reduce) {
    #affiliation-chips a { transition: none; }
    .research-interest-card { transition: none; }
    .research-interest-card:hover,
    .research-interest-card:focus-visible { transform: none; }
    .atom-deco svg { animation: none; }
  }
</style>


<h3 class="accented">About Me</h3>

<p class="lead-para">I develop intelligent systems that integrate memory, reasoning, and multimodal understanding to act autonomously in open-ended environments. My goal is to build foundation models and agentic systems that continually learn, collaborate, and adapt to complex real-world tasks.</p>


I am currently a **Lecturer** at [LMU Munich](https://www.lmu.de/), where I work with [Prof. Hinrich Schütze](https://www.cis.lmu.de/~hs/) on agentic AI and foundation models.

I am also a **group leader** at the [TRESP Lab](https://tresp-lab.github.io/) and am affiliated with the [Munich Center for Machine Learning (MCML)](https://mcml.ai/). At TRESP Lab, I co-supervise PhD students with [Prof. Volker Tresp](https://tresp-lab.github.io/) and Prof. Thomas Seidl. Before joining LMU, I was a research scientist at Siemens, working on quantum machine learning for industrial applications.

Beyond these roles, I collaborate with academic and industrial partners including [Prof. Sören Pirk](https://www.vcai-lab.org/), [Prof. Evgeny Kharlamov](https://scholar.google.de/citations?user=-slpMF8AAAAJ&hl=en), and [Prof. Kristian Kersting](https://ml-research.github.io/people/kkersting/), and supervise industry-funded PhD researchers with partners such as Siemens, Huawei, and Bosch.

I received my PhD in Computer Science from LMU Munich under the supervision of Prof. Volker Tresp. My doctoral research connected relational learning with cognition, quantum computing, and causality. Before moving into computer science, I studied theoretical physics and conducted research on gauge/gravity duality at the Max Planck Institute for Physics.

My current research focuses on LLM-based multi-agent systems that communicate, coordinate, and improve through reflection and experience. I am particularly interested in agents that combine language, vision, and structured knowledge, and in translating these capabilities into robust systems for scientific and industrial applications.

<hr style="border:0;border-top:1px solid var(--global-divider-color);margin:1.75rem 0">

<h3 class="accented">Latest News</h3>

<div class="news">
  <div class="table-responsive">
    <table class="table table-sm table-borderless latest-news-table">
      {% assign news_items = site.news | sort: "date" | reverse %}
      {% for item in news_items limit: 5 %}
        <tr>
          <th scope="row">{{ item.date | date: "%b %Y" }}</th>
          <td>{{ item.content | markdownify }}</td>
        </tr>
      {% endfor %}
    </table>
  </div>
  <a class="latest-news-all" href="{{ '/news/' | relative_url }}">View all news &rarr;</a>
</div>

<hr style="border:0;border-top:1px solid var(--global-divider-color);margin:1.75rem 0">

<h3 class="accented">Research Interests</h3>

<div class="research-interest-grid">
  <a class="research-interest-card" href="{{ '/publications/' | relative_url }}#topic:agentic-ai"><i class="bi bi-cpu"></i>Agentic AI</a>
  <a class="research-interest-card" href="{{ '/publications/' | relative_url }}#topic:self-improving"><i class="bi bi-arrow-repeat"></i>Recursive Self-Improvement</a>
  <a class="research-interest-card" href="{{ '/publications/' | relative_url }}#topic:multimodal-learning"><i class="bi bi-eye"></i>Multimodal Learning</a>
  <a class="research-interest-card" href="{{ '/publications/' | relative_url }}#topic:efficient-llms"><i class="bi bi-lightning-charge"></i>Efficient LLMs</a>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    var atom = document.querySelector('.atom-deco');
    if (atom) {
      var now = Date.now() / 1000;
      atom.style.setProperty('--atom-spin-delay', -((now % 32)) + 's');
    }

    document.querySelectorAll(".news-media-toggle").forEach((button) => {
      const media = document.getElementById(button.getAttribute("aria-controls"));

      if (!media) return;

      button.addEventListener("click", () => {
        const isOpen = media.classList.toggle("is-open");

        button.setAttribute("aria-expanded", String(isOpen));
        button.setAttribute("aria-label", `${isOpen ? "Hide" : "Show"} image for BAY.AI PI Meeting`);
      });
    });
  });
</script>
