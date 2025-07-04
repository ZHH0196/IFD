import matplotlib.pyplot as plt
import matplotlib
# 设置中文字体（适配 Windows）
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False
# 定义时间轴与关键发展方向
years = ['2025', '2026', '2027']
phases = [
    '技术产品化\n• 完善1D-CNN+卡尔曼平台\n• 试点部署\n• 获得首轮融资',
    '平台升级\n• 推出SaaS化平台\n• 行业图谱构建\n• 开始海外试点',
    '生态扩展\n• 工业大模型接入\n• 自主芯片适配\n• 构建开源社区与标准推动'
]

# 创建图表
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(years, [1, 2, 3], marker='o', linewidth=2, color='steelblue')

# 添加每个阶段的描述
for i, txt in enumerate(phases):
    ax.text(i, i+1.1, txt, fontsize=10, ha='center', va='bottom', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# 美化图表
ax.set_ylim(0.5, 3.8)
ax.set_yticks([])
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, fontsize=12)
ax.set_title('Z-AI平台未来三年发展路径图（2025–2027）', fontsize=14, fontweight='bold')
ax.grid(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()
