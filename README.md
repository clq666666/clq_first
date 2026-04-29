# Enterprise Digital Worker (Multi-Agent System)

## 项目简介
本项目是一个基于多智能体协作（Multi-Agent Collaboration）的企业级数字员工系统。旨在解决企业内部跨部门协作效率低、信息碎片化的问题。

## 核心架构
系统由三个核心 Agent 组成：
1. **Collector Agent (信息采集员)**: 负责从 IM (飞书/钉钉)、Jira 和 Git 仓库实时抓取原始数据。
2. **Analyst Agent (分析专家)**: 利用长上下文能力对数据进行研判，对齐项目进度，识别潜在风险。
3. **Strategist Agent (决策建议员)**: 生成最终的项目报告、代码建议或自动化操作。

## 快速开始
1. 配置 `config/settings.yaml` 中的 API Key。
2. 安装依赖: `pip install -r requirements.txt`
3. 运行主程序: `python main.py`
