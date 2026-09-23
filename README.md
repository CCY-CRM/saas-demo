# AI Interior Design SaaS Demo

A static multi-page demo of an AI-assisted interior design workflow, covering project management, modeling, requirements, layouts, style development, rendering, delivery, materials, team management, and design tools.

## Online demo

- Platform demo: https://ccy-crm.github.io/saas-demo/
- Requirements framework: https://ccy-crm.github.io/saas-demo/requirements-framework.html

## Local preview

Serve this directory with any static HTTP server, then open `index.html`.

The built-in sample floor plan works without a backend. Real AI floor-plan recognition requires a separate API service. Copy `proxy_server.example.py` to `proxy_server.py`, set `AI_API_KEY`, and expose its URL through `window.SAAS_API_BASE`. Never put an API key in HTML or browser-side JavaScript.
