# 高级工程数学课程讲义

本站使用仓库根目录的 MineruPress 工具链和 MkDocs Material 模板。`resources/pdfs/` 是原始讲义，`resources/mineru/` 是 MinerU 解析结果，`docs/` 是导出的 Markdown 和图片，`site/` 是生成的静态站点。

在本目录运行：

```sh
../.venv/bin/minerupress export book.yml
../.venv/bin/mkdocs build --strict
../.venv/bin/mkdocs serve
```

重新上传 PDF 解析需要先在 `.env` 填入 MinerU API Token，再显式加载此文件：

```sh
../.venv/bin/python -c 'from dotenv import load_dotenv; load_dotenv(".env", override=True); from minerupress.cli import main; main()' fetch book.yml
```

该命令会上传所有配置的 PDF，并重建导出内容。`.env` 含密钥，不应提交或发布。新的解析结果可能需要调整 `book.yml` 中的章节边界，并检查公式与图片。

Cloudflare Pages 凭据保存在本目录的 `.env`，当前站点为 https://engineering-math-2026.pages.dev/。部署前请先在本地预览并确认内容，随后再执行发布。

Git 保存源 PDF、章节 Markdown、图片以及重新导出所需的 MinerU content list 和图片；原始解析包中重复的 PDF 和其他临时结果不纳入版本控制。
