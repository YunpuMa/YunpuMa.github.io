---
layout: page
permalink: /grants/
title: Grants
description: Research funding and grants.
nav: true
nav_order: 4
---

<style>
  .post-title {
    font-family: 'Libre Baskerville', serif;
    font-weight: 700;
    letter-spacing: 0.01em;
  }
  .post-description {
    font-size: 0.82rem;
    font-variant: small-caps;
    letter-spacing: 0.1em;
    color: var(--global-text-color-light);
    margin: 0.4rem 0 0;
  }
  .post-header {
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2rem;
  }
  .grant-list {
    display: grid;
    gap: 1rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .grant-item {
    position: relative;
    display: grid;
    grid-template-columns: 8.5rem 1fr;
    gap: 1.2rem;
    align-items: start;
    padding: 1.05rem 0 1.15rem;
  }
  .grant-time {
    color: rgba(78, 111, 163, 0.72);
    font-size: 0.9rem;
    font-weight: 500;
    line-height: 1.45;
  }
  html[data-theme=dark] .grant-time {
    color: rgba(124, 160, 197, 0.78);
  }
  .grant-content {
    min-width: 0;
  }
  .grant-heading {
    display: flex;
    gap: 0.45rem;
    align-items: baseline;
    margin: 0 0 0.45rem;
  }
  .grant-name {
    margin: 0;
    color: var(--global-text-color);
    font-size: 1.12rem;
    font-weight: 700;
    line-height: 1.4;
  }
  .grant-link {
    display: inline-flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: center;
    color: var(--global-theme-color);
    font-size: 0.95rem;
    line-height: 1;
    text-decoration: none;
    box-shadow: none;
  }
  .grant-link:hover,
  .grant-link:focus-visible {
    color: var(--global-theme-color);
    text-decoration: none;
    box-shadow: none;
  }
  .grant-media-toggle {
    display: inline-flex;
    flex: 0 0 auto;
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
  .grant-media-toggle:hover,
  .grant-media-toggle:focus-visible {
    color: var(--global-theme-color);
  }
  .grant-funding {
    margin-bottom: 0.4rem;
    color: var(--global-text-color);
    font-size: 0.98rem;
    font-weight: 500;
    line-height: 1.62;
  }
  .grant-funding p:last-child {
    margin-bottom: 0;
  }
  .grant-description {
    color: var(--global-text-color-light);
    font-size: 0.98rem;
    line-height: 1.68;
  }
  .grant-description p:last-child {
    margin-bottom: 0;
  }
  .grant-media {
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition:
      grid-template-rows 240ms ease,
      opacity 180ms ease,
      margin-top 240ms ease;
    margin-top: 0;
  }
  .grant-media.is-open {
    grid-template-rows: 1fr;
    opacity: 1;
    margin-top: 0.85rem;
  }
  .grant-media-inner {
    overflow: hidden;
  }
  .grant-media img {
    display: block;
    width: min(100%, 560px);
    height: auto;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
  }
  .grant-description a,
  .grant-description a:hover,
  .grant-description a:focus-visible {
    color: var(--global-theme-color);
    text-decoration: none;
    box-shadow: none;
  }
  .grant-item:hover,
  .grant-item:hover .grant-content {
    background: transparent;
    box-shadow: none;
    transform: none;
  }
  @media (max-width: 576px) {
    .grant-item {
      grid-template-columns: 1fr;
      gap: 0.35rem;
    }
    .grant-time {
      font-size: 0.84rem;
    }
  }
</style>

<div class="grants">
  <ol class="grant-list">
    {% for grant in site.data.grants %}
      <li class="grant-item">
        {% assign grant_date = grant.time | append: "-01" %}
        <div class="grant-time">{{ grant_date | date: "%b %Y" }}</div>
        <div class="grant-content">
          <div class="grant-heading">
            <h2 class="grant-name">{{ grant.name }}</h2>
            {% if grant.link %}
              <a class="grant-link" href="{{ grant.link }}" aria-label="{{ grant.name }} link" target="_blank" rel="noopener noreferrer">
                <i class="bi bi-box-arrow-up-right" aria-hidden="true"></i>
              </a>
            {% endif %}
            {% if grant.image %}
              <button
                class="grant-media-toggle"
                type="button"
                aria-label="Show image for {{ grant.name }}"
                aria-expanded="false"
                aria-controls="grant-media-{{ forloop.index }}"
              >
                <i class="bi bi-image" aria-hidden="true"></i>
              </button>
            {% endif %}
          </div>
          <div class="grant-funding">{{ grant.funding | markdownify }}</div>
          {% if grant.description %}
            <div class="grant-description">{{ grant.description | markdownify }}</div>
          {% endif %}
          {% if grant.image %}
            <div class="grant-media" id="grant-media-{{ forloop.index }}">
              <div class="grant-media-inner">
                <img src="{{ grant.image | relative_url }}" alt="{{ grant.image_alt | default: grant.name }}">
              </div>
            </div>
          {% endif %}
        </div>
      </li>
    {% endfor %}
  </ol>
</div>

<script>
  document.querySelectorAll(".grant-media-toggle").forEach((button) => {
    const media = document.getElementById(button.getAttribute("aria-controls"));

    if (!media) return;

    button.addEventListener("click", () => {
      const isOpen = media.classList.toggle("is-open");
      const title = button.closest(".grant-content").querySelector(".grant-name").textContent;

      button.setAttribute("aria-expanded", String(isOpen));
      button.setAttribute("aria-label", `${isOpen ? "Hide" : "Show"} image for ${title}`);
    });
  });
</script>
