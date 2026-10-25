import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { satteri } from '@astrojs/markdown-satteri';
import productLayoutPlugin, { loadCatalogNames } from './src/plugins/rehype-product.mjs';

export default defineConfig({
  site: 'https://peptidesofchina.com',
  markdown: {
    processor: satteri({
      hastPlugins: [productLayoutPlugin({ catalog: loadCatalogNames() })],
    }),
  },
  integrations: [sitemap()],
});
