  name: Space Weekly Digest

  on:
    schedule:
      - cron: '0 0 * * 1'    # UTC 0:00 周一 = 北京周一 8:00
    workflow_dispatch:

  permissions:
    contents: write

  jobs:
    digest:
      runs-on: ubuntu-latest
      env:
        ENTITIES_DIR: entities-space
        WINDOW_DAYS: "7"
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with:
            python-version: '3.12'
        - run: pip install openai
        - name: 设置日期(北京时区)
          id: date
          run: echo "today=$(date -u -d '+8 hours' +%F)" >> $GITHUB_OUTPUT
        - name: 收集航天数据
          run: python skills/tracking-list/scripts/collect.py --depth default --skip x huggingface arxiv --output
  data.json
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            ENTITIES_DIR: entities-space
            WINDOW_DAYS: "7"
        - name: 生成航天报告(DeepSeek,失败则兜底)
          run: python space_report.py data.json
          env:
            LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
        - name: 提交报告到 repo
          run: |
            git config user.name "ai-digest-bot"
            git config user.email "bot@users.noreply.github.com"
            git add reports/space_*.md
            git commit -m "space digest ${{ steps.date.outputs.today }}" || true
            git push --force
        - name: 发送邮件
          uses: dawidd6/action-send-mail@v3
          with:
            server_address: smtp.163.com
            server_port: 465
            secure: true
            username: Yuebin_Lun@163.com
            password: ${{ secrets.SMTP_PASSWORD }}
            subject: "航天周报 ${{ steps.date.outputs.today }}"
            to: Yuebin_Lun@163.com
            from: "航天周报 <Yuebin_Lun@163.com>"
            body: file://reports/space_report_${{ steps.date.outputs.today }}.md
            convert_markdown: true