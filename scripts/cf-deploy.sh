#!/bin/bash
# peptidesofchina.com — Cloudflare Pages 部署脚本
# 用法: bash scripts/cf-deploy.sh [production|preview]
set -euo pipefail
cd "$(dirname "$0")/.."

BRANCH="${1:-production}"

echo "=== 1. 构建 ==="
npm run build

echo "=== 2. 部署到 Cloudflare Pages ==="
if [ "$BRANCH" = "production" ]; then
  npx wrangler pages deploy dist --project-name=peptidesofchina --branch=main
else
  npx wrangler pages deploy dist --project-name=peptidesofchina --branch=preview
fi

echo "✅ 部署完成"
echo "生产域名: https://peptidesofchina.com"
